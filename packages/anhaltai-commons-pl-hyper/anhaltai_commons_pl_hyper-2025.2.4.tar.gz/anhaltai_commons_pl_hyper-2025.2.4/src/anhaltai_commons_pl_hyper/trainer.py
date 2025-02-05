"""
This module contains the Trainer class. The Trainer class is used to train a model with
the given configuration. The configuration can be passed as a sweep id (through the
SweepServer) or as a config file.
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Literal

import lightning as pl
import numpy as np
import torch
import wandb
import yaml
from lightning.pytorch.callbacks import EarlyStopping
from lightning.pytorch.loggers import WandbLogger
from lightning.pytorch.plugins import (
    HalfPrecision,
    FSDPPrecision,
    MixedPrecision,
    DoublePrecision,
)
from lightning.pytorch.strategies import DDPStrategy, Strategy, FSDPStrategy
from lightning.pytorch.utilities.rank_zero import rank_zero_only
from wandb.sdk.lib import RunDisabled
from wandb.sdk.wandb_run import Run
from yaml import SafeLoader

from anhaltai_commons_pl_hyper.callbacks import (
    SaveBestModelCallback,
    SaveNewestModelCallback,
)
from anhaltai_commons_pl_hyper.config_validation import validate_configuration
from anhaltai_commons_pl_hyper.constants import DataSplittingMode
from anhaltai_commons_pl_hyper.data_module import DataModule
from anhaltai_commons_pl_hyper.dataclasses.callback import (
    HuggingfaceConfig,
    SaveModelConfig,
    MetricConfig,
)
from anhaltai_commons_pl_hyper.dataclasses.config import (
    RunMetadata,
    TrainerConfig,
    DataModuleConfig,
    DatasetConfig,
    DataLoaderConfig,
    PreprocessorConfig,
    CrossValidationConfig,
    TrainingModuleConfig,
    ModelConfig,
    OptimizerConfig,
    LoggingConfig,
)
from anhaltai_commons_pl_hyper.training_module import TrainingModule
from anhaltai_commons_pl_hyper.utils import validate_literal


class Trainer:
    """
    Trainer class used to train a model with the given configuration. The configuration
    can be passed as a sweep id (through the SweepServer) or as a config file.
    """

    def __init__(self):
        self.run_config: dict  # is set in the train() function
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Initialize Trainer")
        self.is_single_run = True

    def _get_run_configuration(self):
        project_name = os.getenv("WANDB_PROJECT", default="uncategorized")

        if len(sys.argv) > 1:
            run_config = None  # run config comes from the sweep
            self.is_single_run = False

        else:
            single_run_config_path = os.getenv(
                "SINGLE_RUN_CONFIG_PATH", default="configs/single-run.yaml"
            )
            with open(single_run_config_path, encoding="utf-8") as config_file:
                run_config = yaml.load(config_file, Loader=SafeLoader)

            run_config["start_time"] = datetime.now().timestamp()
            self.logger.info("Checking configuration")
            validate_configuration(run_config)
            self.logger.info("No missing values in configuration found")

        # Save wandb.config to a local file and load from it -> Reason: This process
        # gets called multiple times and when we use wandb.init() to get wandb.config we
        # start a new run every time. Using resume="allow" already stopped working with
        # 4 workers (unable to sync files). wandb.config is also not callable during
        # training and instead the config file needs to be passed around.
        self._init_wandb_run(
            run_start_config=run_config,
            project_name=project_name,
        )

        with open("tmp/run-config.yaml", encoding="utf-8") as config_file:
            run_config = yaml.load(config_file, Loader=SafeLoader)
        return run_config

    def train(self) -> float | None:
        """
        Starts the training process. It loads the config, initializes wandb and starts
        the training process. Ensure that training at checkpoints continues.

        Returns:
            float|None: validation score or cross validation score if exists
        """

        self.run_config = self._get_run_configuration()
        self.logger.info("run config:\n%s", json.dumps(self.run_config, indent=4))

        if self.run_config["matmul_precision"]:
            # test with medium/high; (empirical) tests are necessary to find best
            # values to speed up training
            torch.set_float32_matmul_precision(self.run_config["matmul_precision"])
        else:
            torch.set_float32_matmul_precision("highest")
        val_score: float | None = None
        if self.run_config["data_splitting_mode"] == DataSplittingMode.CROSS_VALIDATION:
            val_scores: list[float] = []
            self.run_config["fold_val_scores"] = val_scores
            for i in range(self.run_config["n_splits"]):
                self.run_config["fold_id"] = i
                val_score = self._train_model(self.run_config)
                if val_score is not None:
                    val_scores.append(val_score)
                    self.run_config["fold_val_scores"] = val_scores

            if len(val_scores) > 0:
                cross_validation_score: float = float(np.mean(val_scores))
                self._zero_rank_log(
                    "cross_validation_" + self.run_config["metric"]["name"],
                    cross_validation_score,
                )
                val_score = cross_validation_score

        else:
            val_score = self._train_model(self.run_config)
            if (
                self.run_config["data_splitting_mode"] != DataSplittingMode.FINAL
                and val_score is not None
            ):
                self._zero_rank_log(self.run_config["metric"]["name"], val_score)

        if self.is_single_run:
            self._finish_wandb_run()
        return val_score

    @rank_zero_only
    def _finish_wandb_run(self):
        """
        Finish the wandb run on main process
        """
        wandb.finish()

    @rank_zero_only
    def _zero_rank_log(self, key: str, value):
        """
        Log metrics to wandb on main process
        Args:
            key(str): name of the metric
            value(Any): value of the metric
        """
        wandb.log({key: value})

    @rank_zero_only
    def _init_wandb_run(
        self,
        run_start_config: Optional[dict] = None,
        project_name: str = "uncategorized",
    ) -> None:
        """
        Initializes the wandb run. If a default config is given it will be used to
        initialize the run. If a run id is given it will be used to resume the run.
        If both are given the default config will be ignored.

        Args:
            run_start_config: config for wandb run if no run id is given
            project_name: name of the project to log to
        """

        wandb_mode: Literal["online", "offline", "disabled"] = (
            "online"
            if (not run_start_config or "wandb_mode" not in run_start_config)
            else run_start_config["wandb_mode"]
        )
        # use env value if existing
        wandb_mode = validate_literal(
            os.getenv("WANDB_MODE", wandb_mode),
            Literal["online", "offline", "disabled"],
        )

        wandb_anonymous: Literal["never", "allow", "must"] = validate_literal(
            os.getenv("WANDB_ANONYMOUS", "never"), Literal["never", "allow", "must"]
        )

        if run_start_config:
            run_start_config["wandb_mode"] = wandb_mode
            run_start_config["anonymous"] = wandb_anonymous
            run_start_config["offline"] = wandb_mode == "offline"

        self.logger.info("wandb_mode: %s", wandb_mode)
        self.logger.info("wandb_anonymous: %s", wandb_anonymous)

        # The sweep_id is taken from the environment variable WANDB_RUN_ID set by the
        # agent from create_agent
        if not run_start_config:
            run: Run | RunDisabled | None = wandb.init(
                mode=wandb_mode, anonymous=wandb_anonymous
            )

        elif not run_start_config["checkpoint_path"]:
            run = wandb.init(
                config=run_start_config,
                project=project_name,
                mode=wandb_mode,
                anonymous=wandb_anonymous,
            )

        else:
            run_config = torch.load(run_start_config["checkpoint_path"])[
                "hyper_parameters"
            ]["run_config"]
            wandb_mode = (
                "online"
                if ("wandb_mode" not in run_config)
                else run_config["wandb_mode"]
            )
            # use env value if existing
            wandb_mode = validate_literal(
                os.getenv("WANDB_MODE", wandb_mode),
                Literal["online", "offline", "disabled"],
            )

            run_config["wandb_mode"] = wandb_mode
            run_config["anonymous"] = wandb_anonymous
            run_config["offline"] = wandb_mode == "offline"

            self.logger.info("wandb_mode: %s", wandb_mode)
            run = wandb.init(
                config=run_config,
                project=project_name,
                mode=wandb_mode,
                id=run_config["run_id"],
                resume="must",
                anonymous=wandb_anonymous,
            )
        if not run:
            raise ValueError("run has no valid value")
        run_config = dict(wandb.config)
        if not isinstance(run, wandb.sdk.lib.RunDisabled):
            run.name = (
                run_config["model_name"]
                + "-"
                + datetime.now().strftime("%Y-%m-%d_%H-%M")
            )
        run_config["start_time"] = datetime.now().timestamp()

        # overwrite (or set if missing):
        run_config["wandb_mode"] = wandb_mode
        run_config["anonymous"] = wandb_anonymous
        run_config["offline"] = wandb_mode == "offline"

        # Should not happen, but needed for mypy to not throw an error
        if not wandb.run:
            raise ValueError("Wandb run not initialized")

        run_config["run_id"] = wandb.run.id

        if "preprocessor_name" not in run_config:
            run_config["preprocessor_name"] = run_config["model_name"]

        self._create_directory("tmp/run")

        with open("tmp/run-config.yaml", "w", encoding="utf-8") as config_file:
            yaml.safe_dump(run_config, config_file)

    @rank_zero_only
    def _create_directory(self, directory: str) -> None:
        """
        Create a directory if it does not exist

        Args:
            directory: Path of the directory to create
        """

        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)

    @rank_zero_only
    def _get_and_save_dataset_metadata(self, data_module: DataModule) -> None:
        """
        Prepares the data and saves it to a file. This is only done once on the main
        process and the other processes will load the data from the file.

        Args:
            data_module: Datamodule used for training. It is used to prepare the data
        """
        # We use 'public_function=extendable' as foundation, as such a function which
        # should not be extended is private, even if we need it for the trainer.
        # pylint: disable=protected-access
        dataset_metadata = data_module.get_dataset_metadata(data_module._dataset_config)
        with open("tmp/dataset_metadata.yaml", "w", encoding="utf-8") as config_file:
            yaml.safe_dump(dataset_metadata, config_file)

    def _get_dataset_metadata(self) -> dict:
        """
        Loads the prepared data from a file. This method is called on each process to
        load the data.

        Returns: Dictionary with the dataset metadata
        """

        with open("tmp/dataset_metadata.yaml", encoding="utf-8") as label_file:
            dataset_metadata = yaml.load(label_file, Loader=SafeLoader)
        return dataset_metadata

    def get_training_module(
        self,
        training_module_config: TrainingModuleConfig,
        run_config: dict,
        dataset_metadata,
    ) -> TrainingModule:
        """
        Returns the training module used for training. Needs to be implemented in the
        extension class.

        Args:
            training_module_config: Configuration for the training module
            run_config: Config used to train the model for this run
            dataset_metadata: Dictionary with the class labels

        Returns: TrainingModule used for training
        """
        raise NotImplementedError(
            "This method needs to be implemented in an extension class"
        )

    def get_data_module(
        self,
        datamodule_config: DataModuleConfig,
        run_config: dict,
    ) -> DataModule:
        """
        Returns the data module that should be used for training. Needs to be
        implemented in the extension class.

        Args:
            datamodule_config: Configuration for the data module
            run_config: Config used to train the model for this run

        Returns: DataModule used for training
        """
        raise NotImplementedError(
            "This method needs to be implemented in an extension class"
        )

    def _load_early_stopping(
        self, run_config, metric_postfix: str
    ) -> EarlyStopping | None:
        """
        Loads the early stopping configuration from the run config.

        Args:
            metric_postfix: Postfix for the metric name

        Returns: EarlyStopping Callback used for training
        """
        if "early_stopping" not in run_config:
            logging.warning(
                "Early stopping is disabled because it is not in the config"
            )
            return None

        early_stopping_config = run_config["early_stopping"]
        early_stopping = EarlyStopping(
            monitor=early_stopping_config["monitor"] + metric_postfix,
            patience=early_stopping_config["patience"],
            mode=early_stopping_config["mode"],
            min_delta=early_stopping_config.get("min_delta", 1.0),
        )

        return early_stopping

    def _extract_save_config(
        self, run_config: dict, identifier: str
    ) -> SaveModelConfig:
        """
        Extracts the save model config from the run config.

        Args:
            run_config: Config used to train the model for this run
            identifier: Identifier for the model

        Returns: Config used by the save model callback
        """

        huggingface_config = HuggingfaceConfig(
            username=os.getenv("HF_USERNAME", default=""),
            save_enabled=run_config.get("save_to_huggingface", False),
            repo_name=run_config["model_name"],
        )

        return SaveModelConfig(
            run_config=run_config,
            huggingface_config=huggingface_config,
            identifier=identifier,
            save_every_n_steps=run_config["save_every_n_steps"],
        )

    def _extract_metric_config(
        self, run_config: dict, metric_postfix: str
    ) -> MetricConfig:
        """
        Extracts the metric config from the run config.

        Args:
            run_config: Config used to train the model for this run
            metric_postfix: Postfix for the metric name. "_{fold_id}" when
                cross validation is enabled else empty string.

        Returns: Config used by the metric
        """

        return MetricConfig(
            mode=run_config["metric"]["goal"],
            monitor=run_config["metric"]["name"] + metric_postfix,
        )

    def get_callbacks(
        self,
        save_config: SaveModelConfig,
        run_config: dict,
        run_metadata: RunMetadata,
        metric_config: MetricConfig,
    ) -> list | None:
        """
        Returns the callbacks used for training. The callbacks are used to save the best
        model, the newest model and to stop the training early. This method can be
        overwritten to add additional callbacks.
        Args:
            save_config: Config used to save the model
            run_config: Config used to train the model for this run
            run_metadata: Metadata used for training it contains the run_id, model_name,
              start_time and identifier
            metric_config: Config defining the metric used for training

        Returns: List of callbacks used for training
        """

        callbacks: list[pl.Callback] = []

        early_stopping = self._load_early_stopping(
            run_config, run_metadata.metric_postfix
        )

        if run_config["enable_checkpointing"]:
            best_model_checkpoint: SaveBestModelCallback = SaveBestModelCallback(
                config=save_config,
                mode=metric_config.mode,
                monitor=metric_config.monitor,
                callback_name="best",
            )
            callbacks.append(best_model_checkpoint)

            newest_model_checkpoint: SaveNewestModelCallback = SaveNewestModelCallback(
                config=save_config,
                mode=metric_config.mode,
                monitor=metric_config.monitor,
                callback_name="latest",
            )
            callbacks.append(newest_model_checkpoint)

        if early_stopping is not None:
            callbacks.append(early_stopping)

        if len(callbacks) == 0:
            return None

        return callbacks

    def _extract_datamodule_config(self, run_config: dict) -> DataModuleConfig:
        """
        Extracts the datamodule config from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: Config used by the datamodule class
        """

        dataset_config = DatasetConfig(
            path=run_config.get("dataset_path"),
            origin=run_config.get("dataset_origin"),
            data_splitting_mode=run_config["data_splitting_mode"],
            validation_split_ratio=run_config.get("validation_split_ratio", 0.0),
            test_split_ratio=run_config.get("test_split_ratio", 0.0),
        )

        data_loader_config = DataLoaderConfig(
            batch_size=run_config["batch_size"],
            num_workers=run_config["num_workers"],
            persistent_workers=run_config["persistent_workers"],
            pin_memory=run_config["pin_memory"],
        )

        preprocessor_config = self._extract_preprocessor_config(run_config)

        cross_validation_config = CrossValidationConfig(
            enabled=run_config["data_splitting_mode"]
            == DataSplittingMode.CROSS_VALIDATION,
            num_folds=run_config.get("n_splits", 2),
            seed=run_config["random_seed"],
            fold_id=run_config.get("fold_id", 0),
        )

        return DataModuleConfig(
            dataset_config=dataset_config,
            data_loader_config=data_loader_config,
            preprocessor_config=preprocessor_config,
            cross_validation_config=cross_validation_config,
        )

    def _extract_model_config(self, run_config: dict) -> ModelConfig:
        """
        Extracts the model config from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: Config used by the model
        """

        return ModelConfig(
            name=run_config["model_name"],
            type=run_config.get("model_type"),
            parameters=run_config.get("model_parameters", {}),
        )

    def _extract_optimizer_config(self, run_config: dict) -> OptimizerConfig:
        """
        Extracts the optimizer config from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: Config used by the optimizer
        """

        return OptimizerConfig(
            name=run_config.get("optimizer_name"),
            parameters=run_config.get("optimizer_parameters", {}),
        )

    def _extract_preprocessor_config(self, run_config: dict) -> PreprocessorConfig:
        """
        Extracts the preprocessor config from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: Config used by the preprocessor
        """

        return PreprocessorConfig(
            enabled=run_config.get("preprocess_dataset", False),
            name=run_config.get("preprocessor_name"),
            type=run_config.get("preprocessor_type"),
            parameters=run_config.get("preprocessor_parameters", {}),
        )

    def _extract_logging_config(self, run_config: dict) -> LoggingConfig:
        """
        Extracts the logging config from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: Config used by the logging
        """

        return LoggingConfig(
            save_every_n_steps=run_config["save_every_n_steps"],
            log_every_n_steps=run_config["log_every_n_steps"],
        )

    def _extract_run_metadata(self, run_config: dict) -> RunMetadata:
        """
        Extracts the run metadata from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: RunMetadata used by the TrainingModule class
        """

        identifier = (
            datetime.fromtimestamp(run_config["start_time"]).strftime("%Y-%m-%d")
            + "/"
            + str(run_config["run_id"])
        )
        metric_postfix = (
            "_" + str(run_config["fold_id"])
            if run_config["data_splitting_mode"] == DataSplittingMode.CROSS_VALIDATION
            else ""
        )

        return RunMetadata(
            run_id=run_config["run_id"],
            start_time=run_config["start_time"],
            identifier=identifier,
            metric_postfix=metric_postfix,
        )

    def _extract_training_module_config(self, run_config: dict) -> TrainingModuleConfig:
        """
        Extracts the training module config from the run config to be used by the
        training module class.

        Args:
            run_config: Config used to train the model for this run

        Returns: TrainingModuleConfig used by the TrainingModule class
        """

        return TrainingModuleConfig(
            model_config=self._extract_model_config(run_config),
            optimizer_config=self._extract_optimizer_config(run_config),
            preprocessor_config=self._extract_preprocessor_config(run_config),
            logging_config=self._extract_logging_config(run_config),
            run_metadata_config=self._extract_run_metadata(run_config),
        )

    def _extract_trainer_config(self, run_config: dict) -> TrainerConfig:
        """
        Extracts the trainer config from the run config.

        Args:
            run_config: Config used to train the model for this run

        Returns: Config used by the trainer
        """

        return TrainerConfig(
            accelerator=run_config["accelerator"],
            devices=run_config["devices"],
            max_epochs=run_config["max_epochs"],
            accumulate_grad_batches=run_config["accumulate_grad_batches"],
            check_val_every_n_epoch=run_config["check_val_every_n_epoch"],
            checkpoint_path=run_config["checkpoint_path"],
            logging_config=self._extract_logging_config(run_config),
        )

    def get_strategy(self, run_config) -> str | Strategy:
        """
        Get the strategy for training with pl.Trainer.
        This method provides a very basic setup.
        Can be extended by overriding with a subclass.
        Documentation: https://lightning.ai/docs/pytorch/stable/advanced/model_parallel/
        Args:
            run_config: Configuration for the run

        Returns: strategy name or instance of Strategy for the pl.Trainer
        """

        process_group_backend = "gloo" if os.name == "nt" else None

        strategy = run_config.get("strategy", "auto")
        if strategy == "auto":
            return "auto"

        elif strategy == "ddp":
            logging.info("Using strategy DDP for using multiple GPUs")

            return DDPStrategy(
                find_unused_parameters=False,
                process_group_backend=process_group_backend,
            )

        elif strategy == "fsdp":
            # Refer for full setup:
            # https://lightning.ai/docs/pytorch/stable/advanced/model_parallel/fsdp.html
            logging.info("Using strategy FSDP for using multiple GPUs")

            # setting rank to avoid error "Inconsistent compute device ..."
            # because FSDPStrategy().model_to_device() does nothing
            local_rank = int(os.getenv("LOCAL_RANK", 0))
            logging.info("local_rank is %s", local_rank)
            torch.cuda.set_device(local_rank)

            return FSDPStrategy(
                process_group_backend=process_group_backend,
            )

        raise ValueError("Strategy " + strategy + " is not supported")

    def _get_wandb_logger(self, run_config):
        """
        Gets the wandb logger instance that is compatible to the pl.Trainer for logging
        metrics.
        Args:
            run_config: Configuration for the run

        Returns: instance of WandbLogger

        """
        return WandbLogger(
            config=run_config,
            anonymous=run_config["anonymous"],
            offline=run_config["offline"],
        )

    def get_plugins(self, run_config):
        """
        Get plugin(s) for the pl.Trainer.
        This method provides a very basic setup.
        Can be extended by overriding with a subclass.
        Docs: https://lightning.ai/docs/pytorch/stable/extensions/plugins.html
        Args:
            run_config: Configuration for the run
        Returns: list of pytorch lightning Precision plugins

        """

        precision = 32  # default, no plugins needed
        if "precision" in run_config:
            precision = run_config["precision"]
        strategy_name = "auto"  # default
        if "strategy" in run_config:
            strategy_name = run_config["strategy"]
        plugins = None

        expected_half_precision = [
            64,
            32,
            16,
            "bf16",
            "bf16-true",
            "16-true",
            "bf16-mixed",
            "16-mixed",
            "32-true",
            "64-true",
            "transformer-engine",
            "transformer-engine-float16",
        ]

        if precision not in expected_half_precision:
            raise ValueError(
                "Precision " + str(precision) + "not supported yet. It "
                "must be a value of " + str(expected_half_precision)
            )
        # Precision plugins: only one at a time possible
        if "16-true" in str(precision) or precision == "bf16" or precision == 16:
            if strategy_name == "ddp":
                plugins = [HalfPrecision(precision=precision)]  # type: ignore
            elif strategy_name == "fsdp":
                plugins = [FSDPPrecision(precision=precision)]  # type: ignore
        elif "16-mixed" in str(precision):
            if strategy_name == "ddp":

                if run_config["accelerator"] == "cpu":
                    device = "cpu"
                else:
                    device = "cuda"

                plugins = [
                    MixedPrecision(precision=precision, device=device)  # type: ignore
                ]  # type: ignore
            elif strategy_name == "fsdp":
                plugins = [FSDPPrecision(precision=precision)]  # type: ignore
        elif "64" in str(precision):
            if strategy_name == "ddp":
                plugins = [DoublePrecision()]
            elif strategy_name == "fsdp":
                raise ValueError(
                    "Double precision is currently not supported for "
                    "FSDP strategy. Refer to pytorch lightning "
                    "documentation for details."
                )
        return plugins

    def get_trainer(
        self,
        run_config: dict,
        device_count: int,
        limit_val_batches: float,
        metric_config: MetricConfig,
        run_meta: RunMetadata,
        save_config: SaveModelConfig,
        trainer_config: TrainerConfig,
    ):
        """
        Get the pl.Trainer for the AI training.
        A very basic example is provided.
        Can be extended by overriding with a subclass.
        Documentation:
        https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.trainer.trainer.Trainer.html
        Args:
            run_config: Configuration for the run
            device_count: number of cpu/gpu etc. for AI training
            limit_val_batches: number of validation batches
            metric_config: config for metrics
            run_meta: config for the run
            save_config: config for saving the model
            trainer_config: config to setup the trainer

        Returns: configured instance of pl.Trainer

        """
        trainer = pl.Trainer(
            devices=device_count,
            accelerator=trainer_config.accelerator,
            strategy=self.get_strategy(run_config),
            max_epochs=trainer_config.max_epochs,
            check_val_every_n_epoch=trainer_config.check_val_every_n_epoch,
            logger=self._get_wandb_logger(run_config),
            log_every_n_steps=trainer_config.logging_config.log_every_n_steps,
            callbacks=self.get_callbacks(
                save_config, run_config, run_meta, metric_config
            ),
            accumulate_grad_batches=trainer_config.accumulate_grad_batches,
            limit_val_batches=limit_val_batches,
            plugins=self.get_plugins(run_config),
        )
        return trainer

    def _train_model(self, run_config) -> float | None:
        """
        Trains the model with the given config. It uses the wandb logger to log the
        results.

        Args:
            run_config: Config used to train the model for this run

        Returns: validation score of the model. Validation score is the metric defined
          in the config
        """
        trainer_config: TrainerConfig = self._extract_trainer_config(run_config)

        # Selects all available gpus. Only worked for gpu, for cpu this failed
        device_count: int = int(
            -1 if trainer_config.accelerator == "gpu" else trainer_config.devices
        )

        run_meta: RunMetadata = self._extract_run_metadata(run_config)

        save_config: SaveModelConfig = self._extract_save_config(
            run_config, run_meta.identifier
        )
        metric_config: MetricConfig = self._extract_metric_config(
            run_config, run_meta.metric_postfix
        )

        limit_val_batches: float = 1.0  # default
        if run_config["data_splitting_mode"] == DataSplittingMode.FINAL:
            limit_val_batches = 0.0  # no validation on final run

        trainer: pl.Trainer = self.get_trainer(
            run_config=run_config,
            device_count=device_count,
            limit_val_batches=limit_val_batches,
            metric_config=metric_config,
            run_meta=run_meta,
            save_config=save_config,
            trainer_config=trainer_config,
        )

        data_module_config = self._extract_datamodule_config(run_config)
        data_module = self.get_data_module(data_module_config, run_config)

        # Prepare the data (e.g. download) and save the results to a file
        self._get_and_save_dataset_metadata(data_module)

        dataset_metadata = self._get_dataset_metadata()
        training_module_config = self._extract_training_module_config(run_config)
        basic_module = self.get_training_module(
            training_module_config,
            run_config,
            dataset_metadata,
        )

        # Start the Training
        trainer.fit(
            basic_module,
            datamodule=data_module,
            # Load the checkpoint if the path is not empty
            ckpt_path=(
                trainer_config.checkpoint_path
                if trainer_config.checkpoint_path
                else None
            ),
        )

        val_score = None
        if run_config["data_splitting_mode"] != DataSplittingMode.FINAL:
            if metric_config.monitor in trainer.callback_metrics:
                val_score = (
                    trainer.callback_metrics[metric_config.monitor].detach().item()
                )
            else:
                logging.warning(
                    "Could not calculate validation score because "
                    "the metric with the name %s not found",
                    metric_config.monitor,
                )

        # Test with test data independent to the training
        # see lightning.ai/docs/pytorch/stable/common/evaluation_intermediate.html
        if run_config["data_splitting_mode"] != DataSplittingMode.CROSS_VALIDATION:
            trainer.test(ckpt_path="best", datamodule=data_module, verbose=True)

        return val_score


if __name__ == "__main__":
    Trainer().train()
