# AnhaltAI Commons PL Hyper

**AnhaltAI** **Commons** **P**ytorch **L**ightning Trainer Framework for **Hyper**
Parameter Optimization

## Summary

This framework provides a Deep Learning Trainer based on PyTorch Lightning with common
usable setup for different
deep learning tasks that supports k-Fold cross-validation to fulfill automated
hyperparameter optimization.
Training runs are planned by using sweeps
from [Weights and Biases (wandb)](https://wandb.ai/site/)
that are created based on the supported configuration files.

The framework is based on the PyTorch Lightning Trainer and provides
extended functionality. It allows models to be trained in a multi-GPU setup, both on a
local machine and in more distributed environments.
Using the functionality of Weights and Biases enables planning, starting, and logging
multiple experiments at once (called sweeps). Offering these features in context forms
the main part of our framework.

The content provided by the framework is intended to simplify comparisons
of AI training experiments.

With its abstract classes the code is not usable in its
base form since some functions have to be implemented by an inheriting class.

The package is accessible on [PyPI](https://pypi.org/project/anhaltai-pl-hyper/) and
compatible with [Python version >=3.10](https://www.python.org/downloads/)

## Contents

- [User Guide](#user-guide)
    - [How to Start](#how-to-start)
    - [Tutorial](#tutorial)
        - [How to extend the implementation for your task](#how-to-extend-the-implementation-for-your-task)
          <details open>
          <summary>Related Links</summary>

            - [Abstract Classes](src/anhaltai_commons_pl_hyper/README.md)
          </details>
        - [Quick Start Using the Example Project to Initialize the Project Structure
          ](#quick-start-using-the-example-project-to-initialize-the-project-structure)
    - [Add Models](#add-models)
        - [Custom Models](#custom-models)
        - [Import Models](#import-models)
    - [Entrypoints](#entrypoints)
        - [Start of a Single Run](#start-of-a-single-run)
        - [Start of a Sweep](#start-of-a-sweep)
    - [Configure logging for multiprocessing](#configure-logging-for-multiprocessing)
    - [Setup Configs](#setup-configs)
      <details open>
      <summary>Related Links</summary>

        - [Config Documentation](docs/config-documentation.md)
        - [Data-Splitting Documentation](docs/data-splitting-documentation.md)
      </details>
    - [Setup Environment Variables](#setup-environment-variables)
        - [Required Environment Variables for Training
          ](#required-environment-variables-for-training)
        - [Additional Environment Variables for Docker
          ](#additional-environment-variables-for-docker)
        - [Additional Environment Variables for Kubernetes
          ](#additional-environment-variables-for-kubernetes)
    - [Logging Metrics](#logging-metrics)
    - [Checkpoints](#checkpoints)
    - [Resume Weights and Biases Sweeps](#resume-weights-and-biases-sweeps)
    - [Build Docker Images](#build-docker-images)
    - [Example for Running Docker Images on Kubernetes](#example-for-running-docker-images-on-kubernetes)
        - [Preparation for Kubernetes or Rancher](#preparation-for-kubernetes-or-rancher)
            - [For a Sweep](#for-a-sweep)
            - [For a Single Run](#for-a-single-run)
        - [Start Training on Kubernetes or Rancher](#start-training-on-kubernetes-or-rancher)
        - [Cleanup after Training on Kubernetes or Rancher](#cleanup-after-training-on-kubernetes-or-rancher)
- [Development Setup](#development-setup)
    - [Install Python Requirements](#install-python-requirements)
    - [Build Package Locally](#build-package-locally)
    - [Unit Tests and Integration Tests](#unit-tests-and-integration-tests)

## User Guide

This chapter is meant for the users of this framework and gives the introduction as
well as further usage possibilities

### How to start

This section provides guidelines for setting up your AI training project using the
framework.

It is intended that you can create your own project for AI training that can have any
directory structure, apart from a few specifications for the use of the framework.

In addition, similar to PyTorch and lightning, the framework is expected to be installed
as python package in order to use or extend its contents.

The framework is published on PyPI and can therefore be installed as package using pip.

````shell
pip install anhaltai-commons-pl-hyper
````

The next section [tutorial](#tutorial) will help you to start a project that uses the
anhaltai-commons-pl-hyper framework.

After completing the tutorial as a quick introduction, you can continue developing your
project using the other sections.

### Tutorial

The tutorial in this section shows how to set up a project at the example of an 2D image
classification training where a model architecture from Hugging Face or a custom model
implementation can be used. The dataset is downloaded from Hugging Face too.

You can work through the chapters of the tutorial in order or read them individually if
your training setup deviates too much from the example.

> **_Hint:_** The tutorial assumes that only one AI training task is prepared for each
> project. After you have familiarized yourself with the framework, you could later
> redesign the project structure to be able to train multiple tasks.

#### How to extend the Implementation for your Task

This section introduces how the implementation of training for a specific task is
intended. Further implementation details will follow in the next sections.

To use this framework for your very specific task you have to extend the provided
abstract classes and functions.

First of all, there is an <b>example project</b> at
`examples/example_classification_project` that
shows a fully functional example of how this framework can be used.

The integration tests in the `tests/integration` directory also show
examples how to use different configurations e.g. for using different tasks and
data splitting on the same code base.

As shown in the example project, you need to extend the implementation of the
following classes by implementing a subclass for each of them if you want to use
its functionality:

- [Trainer](src/anhaltai_commons_pl_hyper/trainer.py)
- [DataModule](src/anhaltai_commons_pl_hyper/data_module.py)
- [TrainingModule](src/anhaltai_commons_pl_hyper/training_module.py)

Detailed information about the extendable classes and custom model
architectures
here: [src/anhaltai_commons_pl_hyper/README.md](src/anhaltai_commons_pl_hyper/README.md)

Additionally, to your `DataModule` subclass you will need to use the data loader
and preprocessing of your datasets for your specific AI learning task.

Proceed to the [next section
](#quick-start-using-the-example-project-to-initialize-the-project-structure) to see
the example project setup.

#### Quick Start using the Example Project to initialize the Project Structure

In this section it is explained how to start a project from the code base of the
example project that uses the framework.

Do the following steps for quick start:

- Have a look at the [example project](examples/example_classification_project)
    - The source code has a package [classification_training
      ](examples/example_classification_project/src/classification_training) that can be
      copied for building Docker images later.
    - It contains a subclass of the [Trainer
      ](src/anhaltai_commons_pl_hyper/trainer.py) class in [classification_trainer.py
      ](examples/example_classification_project/src/classification_training/classification_trainer.py)
      as the centerpiece and entrypoint to use the [pytorch lightning framework
      ](https://lightning.ai/docs/pytorch/stable/)
    - Custom model architectures are implemented in [custom_models
      ](examples/example_classification_project/src/classification_training/custom_models)
      and added to the control structure of the subclass of the TrainingModule class
    - The subclass of the [TrainingModule
      ](src/anhaltai_commons_pl_hyper/training_module.py) class in the
      [classification_training_module.py
      ](examples/example_classification_project/src/classification_training/classification_training_module.py)
      wraps the model to use pytorch lightning
    - To load and transform single instances of a dataset is the subclass of a [torch.
      utils.data.Dataset
      ](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html) implemented in
      the [classification_datasets.py
      ](examples/example_classification_project/src/classification_training/classification_datasets.py)
    - Data transforms and normalization are implemented in the [preprocessing.py
      ](examples/example_classification_project/src/classification_training/preprocessing.py)
    - The subclass of the [DataModule](src/anhaltai_commons_pl_hyper/data_module.py) is
      located in the [classification_data_module.py
      ](examples/example_classification_project/src/classification_training/classification_data_module.py)
      and is responsible for the batched loading and splitting of datasets
    - Hyperparameters are set in the [config for a single run
      ](examples/example_classification_project/configs/single-run.yaml) or in the
      [config for a sweep](examples/example_classification_project/configs/sweep).
      Both cases are used for metric logging with [Weights and Biases
      ](https://wandb.ai/site/).


- To make the example independent of this framework repository create an empty
  directory for a new project on your device.
- Copy the contents of the [example_classification_project
  ](examples/example_classification_project) in your project
  root so that the project root is named, as you want. The `src` folder has
  to be in the project root.
- Navigate in your project root and ensure that you have Python installed.
- optional: Create a virtual python environment for your IDE and activate it for the
  next steps
- Install all needed python packages
    ````shell
    pip install -r requirements.txt
    ````
- Because of copying the files, the imports of the python source code files could be
  broken. Correct the broken imports in each src code file. While doing this
  imports from the public `anhaltai-commons-pl-hyper package` must be used instead of
  the local imports to the [source code](src/anhaltai_commons_pl_hyper) in the example.
- optional: You can change the values of the environment variables inside the `.env`
  file e.g. `WANDB_MODE=online` and set the wandb credentials to be able to see the
  metrics online at https://wandb.ai (
  see [wandb env variable docs
  ](https://docs.wandb.ai/guides/track/environment-variables/))
- more environment variables and configuration parameters are introduced in the next
  sections and can be skipped for now
- important: If you are using Git, it is important to add the `.env` file to the
  `.gitignore` file to exclude it because .env can contain your secrets. (`.env` was not
  added to `.gitignore` previously to provide the example)

- After this very basic setup you can start the training locally by using the
  entrypoints.
    - To start a wandb single run:
    ````shell
    python -u -m src.classification_training.classification_trainer
    ````
    - To start a wandb sweep (multiple runs) run those commands in different
      terminals. You will have to set your wandb credentials first in the env
      variables:
    ````shell
    python -u -m src.classification_training.wandb_utils.sweep_server
    python -u -m src.classification_training.wandb_utils.sweep_agent
    ````
- Once this works, you can build Docker images for this example. Read
  section [Build docker images](#build-docker-images) to do it. You can try out
  the wandb single [run and sweep run options](docs/config-documentation.md).
  Further you can play around with the
  different [data splitting modes](docs/data-splitting-documentation.md).
- After you have understood the provided example you can start to adapt and extend the
  code for your own AI training task.

### Add Models

This section explains how to add a model to the training setup.

The model architecture should be added in such a way, that multiple models
can be selected by the config for different runs on the same data to allow wandb sweep
runs for clean comparisons.

Model name and additional settings can be set in the config. It is allowed to add
further control structures and settings. Refer to the
[config documentation](docs/config-documentation.md) for details about parameters.

#### Custom Models

Custom models have to be an extension
of [torch.nn.Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html) and
have to implement the
forward function. They can be implemented in any Python file and must be added to
your self implemented control structure to select the model by the config.

- Example: [cnn_model.py
  ](examples/example_classification_project/src/classification_training/custom_models/cnn_model.py)
  added to the control structure in the `load_model()` method of the
  [TrainingModule](src/anhaltai_commons_pl_hyper/training_module.py) class:
  [classification_training_module.py
  ](examples/example_classification_project/src/classification_training/classification_training_module.py)

#### Import Models

The model import should be added directly to the control structure in the
`load_model()` method of the
[TrainingModule](src/anhaltai_commons_pl_hyper/training_module.py) class or
outsourced to another python file.

### Entrypoints

This section explains what are entrypoints for a training are
explained and how to modify them.

Having implemented the entrypoints in your own files is essential for the later
step [Build docker images](#build-docker-images).

There are at least two entrypoints to start the training, that
are explained in the subsections below.

For a setup such as given in the [example project
](examples/example_classification_project) the working directory must be the
project root where the entrypoints are called from because of the referenced
location of the config files.

They depend on the two options, how wandb is used:
single [runs](https://docs.wandb.ai/ref/python/run/) and [sweeps
](https://docs.wandb.ai/guides/sweeps/).

#### Start of a Single Run

You have to call the `train()` method of an instance of your [Trainer
](src/anhaltai_commons_pl_hyper/trainer.py) subclass to
start a training.

- Example: [classification_trainer.py
  ](examples/example_classification_project/src/classification_training/classification_trainer.py)

In this case the training is configured by the config for the single run.

- Example: [single-run.yaml
  ](examples/example_classification_project/configs/single-run.yaml)

#### Start of a Sweep

Two functions are needed when running a sweep on multiple devices:
[sweep and agent](https://docs.wandb.ai/guides/sweeps/walkthrough/).

The `main()` function is implemented in the
[SweepServer](src/anhaltai_commons_pl_hyper/wandb_utils/sweep_server.py) class.

You must implement an entrypoint that calls the `main()` method of an instance of
`SweepServer` to start a sweep server from where the sweep agents on other devices
can get the sweep ID over an GET request.

- Example: [sweep_server.py
  ](examples/example_classification_project/src/classification_training/wandb_utils/sweep_server.py)

Sweeps can be resumed, as explained [here](#resume-weights-and-biases-sweeps).

Also, you need to implement an entrypoint that calls the `create_agent()` function to
start a sweep agent that requests the sweep ID from the sweep server. The agent
calls the `train()` method of an instance your `Trainer` subclass. With the
sweep ID he can get the correct run config is get from the running wandb sweep.

- Example: [sweep_agent.py
  ](examples/example_classification_project/src/classification_training/wandb_utils/sweep_agent.py)

### Configure Logging for Multiprocessing:

Learn how to set up console logging when using multiprocessing with PyTorch Lightning
in this section.

It is recommended to set custom logging options for logging to the console or log files
at the very beginning of all entrypoints as shown by the code examples in the section
[Entrypoints](#entrypoints).

Placing the logging format this way enables the logging even when multiprocessing
is used when training with multiple devices and data loader workers.
It prevents the logs from not being output in some cases.

It is possible to make console logs of multiple processes more readable. For example
the following logging setup provides import information for each line such as
timestamp, host name, process ID and log level:

````Python
import logging

log_format = "%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format, datefmt="%Y-%m-%d %H:%M:%S")
````

Those lines are used for the entrypoints of the example project:

- [classification_trainer.py
  ](examples/example_classification_project/src/classification_training/classification_trainer.py)
- [sweep_agent.py
  ](examples/example_classification_project/src/classification_training/wandb_utils/sweep_agent.py)
- [sweep_server.py
  ](examples/example_classification_project/src/classification_training/wandb_utils/sweep_server.py)

The underlying framework lightning provides further options to configure custom
logging to the console: https://lightning.ai/docs/pytorch/stable/common/console_logs.
html.

### Setup Configs

This section gives an overview for the setup of the training configs wandb single run
and sweep config.

The location of the config files can be set with environment variables
`SINGLE_RUN_CONFIG_PATH` and `SWEEP_DIRECTORY` as explained in
[Setup Environment Variables](#setup-environment-variables).

The config documentation can be found [here](docs/config-documentation.md) with
example config files in `examples/example_classification_project/configs`.

Data splitting is a part of the training configuration and has [3 modes
](docs/data-splitting-documentation.md):

- Train
- Train + Test
- Train + Test + Validation

### Setup Environment Variables

This section explains all mandatory and optional environment variables.

Using an ``.env`` file locally in your project root is recommended.

- Example: [.env](examples/example_classification_project/.env)

#### Required Environment Variables for training

The most important environment variables for this training framework are listed here.
Keep in mind that further variables e.g. of Weights and Biases can be compatible to
the framework. For the sake of simplicity, however, we refer to the original sources.

| Variable               | Mandatory, Condition                     | Examples                              | Source                                                                                                 |                                                                                                                                                                | Description |
|------------------------|------------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| CHECKPOINT_DIRECTORY   | No, for checkpointing                    | models                                |                                                                                                        | Local directory to save the checkpoints.                                                                                                                       |             |
| HF_TOKEN               | No, to upload to Hugging Face.           | (secret)                              | [Hugging Face](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables) | Hugging Face token                                                                                                                                             |             |
| HF_USERNAME            | No, to upload to Hugging Face.           | username                              | [Hugging Face](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables) | Hugging Face username                                                                                                                                          |             |
| SINGLE_RUN_CONFIG_PATH | No, for wandb single runs                | configs/single-run.yaml               |                                                                                                        | Local file of the single run config for your single wandb run if not using a sweep.                                                                            |             |
| SWEEP_DIRECTORY        | No, for wandb sweeps                     | configs/sweep                         |                                                                                                        | Local directory of the configs for your wandb sweeps.                                                                                                          |             |
| SWEEP_SERVER_ADDRESS   | No, for wandb sweeps                     | http://localhost:5001                 |                                                                                                        | The address of your hosted sweep server                                                                                                                        |             |
| TRAINER_PATH           | No, for wandb sweeps                     | classification.classification_trainer |                                                                                                        | Python file where your trainer subclass is implemented for your learning task                                                                                  |             |
| WANDB_ANONYMOUS        | No, set to must for integration tests    | allow, never, must                    | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | Let users create anonymous runs with secret urls.                                                                                                              |             |
| WANDB_API_KEY          | No, for wandb online, sweeps             | (secret)                              | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | API KEY of your wandb account.                                                                                                                                 |             |
| WANDB_DISABLE_GIT      | No, set to true for integration tests    | true, false                           | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | Prevent wandb from probing for a git repository and capturing the latest commit / diff.                                                                        |             |
| WANDB_ENTITY           | No, for wandb online, sweeps             | my_company                            | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | Name of the wandb entity. ([https://docs.wandb.ai/ref/python/init/](https://docs.wandb.ai/ref/python/init/))                                                   |             |
| WANDB_MODE             | No, set to offline for integration tests | online, offline                       | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | If you set this to “offline” wandb will save your run metadata locally and not sync to the server. If you set this to disabled wandb will turn off completely. |             |
| WANDB_PROJECT          | No, for using wandb                      | my_project                            | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | Name of the wandb project. ([https://docs.wandb.ai/ref/python/init/](https://docs.wandb.ai/ref/python/init/))                                                  |             |
| WANDB_USERNAME         | No, for wandb online, sweeps             | my_name                               | [wandb](https://docs.wandb.ai/guides/track/environment-variables/)                                     | Username of your wandb account.                                                                                                                                |             |

#### Additional Environment Variables for Docker

Condition: When building or pushing docker images.

| Variable                       | Mandatory, Condition | Examples                 | Sources                                                                                                                         | Description                                                           |
|--------------------------------|----------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| DOCKER_REPOSITORY_SERVER       | No, to push images.  | gitlab.com:5050          | [Docker](https://www.docker.com/products/docker-hub/), [GitLab](https://docs.gitlab.com/ee/user/packages/container_registry/)   | Repository server of of your docker container registry                |
| DOCKER_REPOSITORY_PATH         | No, to push images.  | myprojectGroup/myproject | [Docker](https://www.docker.com/products/docker-hub/), [GitLab](https://docs.gitlab.com/ee/user/packages/container_registry/)   | Repository path of your docker container registry                     |
| DOCKER_TRAINING_IMAGE_NAME     | No, to build images. | 2024.10.dev0             |                                                                                                                                 | Trainer image name for docker build (dev or release)                  |
| DOCKER_SWEEP_SERVER_IMAGE_NAME | No, to build images. | sweep-server             |                                                                                                                                 | Sweep server image name for docker build                              |
| DOCKER_USERNAME                | No, to push images.  | username                 | [Docker](https://docs.docker.com/accounts/create-account/), [GitLab](https://docs.gitlab.com/ee/user/profile/)                  | Username of your docker container registry. GitLab is also supported. |
| DOCKER_TOKEN                   | No, to push images.  | (secret)                 | [Docker](https://docs.docker.com/security/for-developers/access-tokens/), [GitLab](https://docs.gitlab.com/ee/security/tokens/) | Token of your docker container registry.  GitLab is also supported.   |

#### Additional Environment Variables for Kubernetes

Condition: When running docker images in Kubernetes.

Environment variables can be provided as config-maps and secrets on Kubernetes or
Rancher.

- also required are the following Docker env variables explained in section
  [Additional Environment Variables for Docker
  ](#additional-environment-variables-for-docker):
    - DOCKER_REPOSITORY_SERVER
    - DOCKER_USERNAME
    - DOCKER_TOKEN

| Variable                  | Mandatory/Condition  | Examples                 | Source                                                                                      | Description                                           |
|---------------------------|----------------------|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------|
| KUBE_NAMESPACE            | Yes                  | my-training              | [Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) | Your kubernetes namespace                             |
| KUBE_SWEEP_SERVER_ADDRESS | No, for wandb sweeps | http://sweep-server:5001 |                                                                                             | The address of your hosted sweep server on kubernetes |

### Logging Metrics

This section explains the logging of metrics.

The metrics of the runs can be retrieved from the
[Weights and Biases website](https://wandb.ai/).
You can set the config for it via the [run/sweep config](docs/config-documentation.md)
and the login with wandb
[environment variables](#required-environment-variables-for-training).

### Checkpoints

This section explains saving and loading of checkpoints.

The checkpoints are saved to the relative directory path that is given by the [env
variable](#required-environment-variables-for-training)
`CHECKPOINT_DIRECTORY` which is by default `models`.
Subfolders are created for the `best` and `latest` checkpoints
(their existence depends on [run/sweep config](docs/config-documentation.md)).
Inside these folders subfolders with the timestamp of their creation are created.
There you will find the checkpoint directories for your runs named by the wandb run id
of the run that is logged on the [Weights and Biases website](https://wandb.ai/).

The upload of the checkpoints of the trained model to Hugging Face can be configured
in the [run/sweep config](docs/config-documentation.md).

When using [Kubernetes](#example-for-running-docker-images-on-kubernetes) it is possible
to mount this
checkpoint folder as [volume](https://kubernetes.io/docs/concepts/storage/volumes/)
e.g. [Persistent Volumes (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
to be able to retrieve the checkpoints after training.

The training that was started using the framework can be resumed by setting the
checkpoint path in the [config](docs/config-documentation.md) to load the checkpoint.
Important: For sweeps, all runs will start from this checkpoint.

### Resume Weights and Biases Sweeps

Instructions on resuming sweeps are provided in this section.

When the `sweep_id` parameter in the
sweep config is set to the sweep ID of a running
sweep ([refer to config docs](docs/config-documentation.md)) then the sweep will be
resumed to run only the planned runs that have not been started yet.

To be able to resume Weights and Biases (wandb) runs by using SweepServer you will
need to install wandb on your **system interpreter**!
The resume of a sweep is explained in a further section [Setup Configs](#setup-configs).

````shell
pip install wandb
````

### Build Docker Images

This section shows how to build docker images to run your training.

This step depends also on your project specific setup.

You can build **docker images** to run the training. One image is for single
run training and the sweep agent. Another image is for the sweep server. You can
build them with the example shell script that is provided in the example project:

- Must be called from the example project's root
  ````shell
  ./scripts/build_images.sh
  ````

There is another script for the case if you want to build and push to a docker
image repository, if the env variables are set for the docker repository:

- Must be called from the example project's root
  ````shell
  ./scripts/build_and_upload_images.sh
  ````

examples/example_classification_project/scripts/build_and_upload_images_only_sweep_server.sh

Configs explained in [Setup Configs](#setup-configs) will be
baked into the docker image by default. So you can rebuild the SweepServer if you
make changes in the sweep config files e.g. by using this shell script:

- Must be called from the example project's root
  ````shell
  ./scripts/build_and_upload_images_only_sweep_server.sh
  ````

Alternatively you can mount the config
files as volumes (Read further for examples:
[Example for running on Kubernetes](#example-for-running-docker-images-on-kubernetes)).

### Example for Running Docker Images on Kubernetes

This section explains how you can run your built docker images with
[Kubernetes](https://kubernetes.io/docs/home/), after you read the section [Build
docker images](#build-docker-images).

#### Preparation for Kubernetes or Rancher

To be able to run the docker images on Kubernetes as pods you should prepare your
setup first.
The provided example shell script [setup_kubernetes.sh
](examples/example_classification_project/scripts/setup_kubernetes.sh) does the
following:

- creates a Kubernetes namespace if not existing and uses it for the next steps
- recreates a secret named wandb-access for the wandb credentials
- recreates a docker-registry named gitlab-registry for the case that docker images
  are stored on gitlab as Docker registry
- recreates a configmap named sweep-config for further env variables that are
  necessary for the training
- recreates the service for the sweep server to open the port for the
  requests by the agents

Alternatively, you can create your setup (configmaps, secrets and services) manually
or with a adapted shell script.

Working with the example shell script [setup_kubernetes.sh
](examples/example_classification_project/scripts/setup_kubernetes.sh):

- When working on [Rancher](https://www.rancher.com/) then you have to log in to your
  Kubernetes cluster, and you have to create your namespace in you project then because
  kubectl cannot
  create a namespace inside a project. Projects only exist on rancher and not
  in Kubernetes itself.

- Next set the name of the namespace as
  local [env variable](#additional-environment-variables-for-kubernetes) so
  that the shell script can create the contents in the existing namespace.

- Ensure that you have set all env variables that are required for the training
  locally:
  see [Required Environment Variables for training
  ](#required-environment-variables-for-training)

- Additional environment variables for Kubernetes are needed as well:
  see [Additional Environment Variables for Kubernetes
  ](#additional-environment-variables-for-kubernetes)

  You need to be connected to the kubernetes cluster inside the console by using the
  kubernetes config of the cluster.
  The setup shell script will use these env variables to create the
  configmaps, secrets and services for your AI training.

- Then run the setup shell script to create the necessary kubernetes
  resources.:

  ````shell
  ./examples/example_classification_project/scripts/setup_kubernetes.sh
  ````

You can repeat this procedure for multiple clusters and namespaces if you need to
run multiple AI training experiments in parallel.

You can define your .yaml files for Kubernetes to start single runs and sweeps. You
find more details about them in the
next subsections:

- [Kubernetes files for a sweep](#for-a-sweep)
- [Kubernetes files for a single run](#for-a-single-run)

##### For a Sweep:

There are templates for kubernetes yaml files provided in the example
project ``examples/example_classification_project/configs/kubernetes/sweeps`` that
fit to the example Dockerfiles.

> **_Important_** You need to set the docker image urls in those .yaml files to
> point to your built images to use them.

Example files explained:

| File                                           | Description                                                                                                                                                       |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| classification-training-pod.yaml               | Kubernetes config to start a job to launch multiple wandb agents for a sweep. (sweep server needed)                                                               |
| classification-training-with-sweep-server.yaml | Kubernetes config to start a job to launch multiple wandb agents for a sweep. Additionally, starts a sweep server independent from the job usable for the agents. |
| sweep-server-service.yaml                      | Kubernetes config to start a service, so that the agents can send requests to the port of the sweep server.                                                       |
| sweep-server.yaml                              | Kubernetes config to start a sweep server.                                                                                                                        |

To run a sweep, the `SweepServer` needs to run and the sweep configs must be located in
the folder at the environment variable SWEEP_DIRECTORY path.
In the example the sweep config files  ``model.yaml``, ``logging.yaml`` and
``dataset.yaml`` are given in addition to the mandatory ``sweep.yaml``.
The sweep config directory can include any number of yaml files in any number of
subdirectories to offer the possibility to group the parameters. The only
limitation is that `sweep.yaml` lays directly in the sweep
directory and includes the general sweep settings. All the other files contain the
parameters. For example:

- `dataset.yaml` - contains the dataset configuration
- `model.yaml` - contains the model configuration
- `logging.yaml` - contains the logging configuration
- `sweep.yaml` - contains general sweep configuration

Those configs combined follow the structure of
a [wandb sweep config](https://docs.wandb.ai/guides/sweeps/define-sweep-configuration/).

The configs are copied to the docker image by default, so you have to rebuild the
image on every change, which takes much time.
The next lines explain an optional alternative way how to change the parameter
values of the configs without a rebuild of the image.

They configs can be set in
a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
named ``sweep-config-yaml`` and mounted by using a
[volume](https://kubernetes.io/docs/concepts/storage/volumes/)
to replace the default config files.

> **_Caution:_** The configs set in the ConfigMap
> fully replace the previously copied config files! You have to change the values
> inside the ConfigMap for them to take effect.

The ConfigMap must be created in the same
Kubernetes namespace as used for the training.

To create the ConfigMap add the filename and the content of the file
for each config file as key value pairs to the ConfigMap. The filename is used as key
and the file content is to be pasted as value.

The image shows an example for two files:

<img src="docs/imgs/kubernetes-config-map-sweep.png" alt="img scikit-learn cross validation" width="800">

As shown in the ``classification-training-with-sweep-server.yaml`` the ConfigMap is
provided as volume for the sweep server so that all files given in the ConfigMap are
used to fully replace the default ``configs/sweep`` folder:

Shown are the most important lines for the sweep server pod:

````
kind: Pod
metadata:
  name: sweep-server
[...]
spec:
[...]
  containers:
    - name: pytorch-model-sweep-agent
[...]
      volumeMounts:
        - name: sweep-config-yaml
          mountPath: /configs/sweep
[...]
  volumes:
    - name: sweep-config-yaml
      configMap:
        name: sweep-config-yaml
````

For more details, see the
[Kubernetes docs](https://kubernetes.io/docs/concepts/configuration/configmap/).

##### For a Single Run:

There is a templates for a kubernetes yaml file provided in the example
project ``examples/example_classification_project/configs/kubernetes/single-run`` that
fits to the example Dockerfiles.

> **_Important_** You need to set the docker image urls in this .yaml file to
> point to your built images to use them.

Example file explained:

| File                                        | Description                                                             |
|---------------------------------------------|-------------------------------------------------------------------------|
| classification-training-pod-single-run.yaml | Kubernetes config to start a single wandb run. (no sweep server needed) |

The single run config is copied to the docker image by default, so you have to
rebuild the
image on every change, which takes much time.
The next lines explain an optional alternative way how to change the parameter
values of the config without a rebuild of the image.

For the single run it is also possible to provide the ``single-run.yaml`` in a
[ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
e.g. ``single-run-yaml``. The filename ``single-run.yaml`` is used as key
and the file content as value inside the ConfigMap.

As visible in the example ``classification-training-pod-single-run.yaml`` the
ConfigMap is provided as [volume](https://kubernetes.io/docs/concepts/storage/volumes/)
for the container (sweep server is not needed) in which
the training runs.
To be able to only replace the default ``single-run.yaml`` that is located at
``/workspace/configs/single-run.yaml`` in the docker image only the ``single-run.yaml``
key is used from the ConfigMap as volume. The ``subPath``
parameter is necessary for the volume mount to only replace that single file.

> **_Caution:_** The single run config set in the ConfigMap
> fully replaces the previously copied config file! You have to change the values
> inside the ConfigMap for them to take effect.

Shown are the most important lines for the single run job:

````
apiVersion: batch/v1
kind: Job
[...]
      containers:
        - name: pytorch-model-single-run
[...]
          volumeMounts:
            [...]
            - mountPath: /workspace/configs/single-run.yaml
              name: single-run-yaml
              subPath: single-run.yaml
[...]
      volumes:
        [...]
        - name: single-run-yaml
          configMap:
            name: single-run-yaml
            items:
              - key: single-run.yaml
                path: single-run.yaml
````

#### Start Training on Kubernetes or Rancher

If the hyperparameters are set in the config-maps and the Kubernetes yaml files have
been prepared (includes selection of namespace, node, computation resources) then you
can paste the yaml files to Kubernetes or Rancher.

The training will run itself until its finished.

#### Cleanup after Training on Kubernetes or Rancher

If there are any finished jobs and pods on the system then you can delete them,
after you have found the logged metrics by wandb.

It is recommended to keep the rest of the setup of the namespace as it is to be
able to launch more trainings without repeating all preparation steps. In this case the
reduced preparation time clearly shows the benefits of using the framework.

## Development Setup

This chapter is meant for the developers of this framework and shows the basic
project setup to be able to further develop or maintain the framework.

It is recommended to follow the sections in the given order.

### Install Python Requirements

````shell
pip install -r requirements.txt
pip install -r requirements-tests.txt
````

### Set src Folders:

- `src`
- `examples/example_classification_project/src`

### Set test Folders:

- `tests`

### Unit Tests and Integration Tests

- caution: The [example project](examples/example_classification_project) is also
  configured as integration tests. Only change
  the .env and config files if you know what you are doing.

- Test scripts directory: tests
- Integration test scripts directory: tests/integration
- The integration tests in tests/integration are used to show minimal example project
  setups
- All tests have to be run from the project root dir as workdir
- Please do not mark the subdirectories named "src" python as source folders to avoid
  breaking the structure
- To find all code modules during tests the ``pythonpath`` is defined in the
  ``pyproject.toml`` file

This way all tests functions (with prefix "tests") are found and executed from project
root:

````shell
pytest tests
````

### Debug Entrypoints

For a setup such as given in the [example project
](examples/example_classification_project) the working directory must be the
project root where the entrypoints are called from because of the referenced
location of the config files.

Append `examples/example_classification_project/src` as value to the env variable
`PYTHONPATH`.

First change working directory:

````shell
cd examples/example_classification_project
````

You can run the trainer implementation of the provided
[example project](examples/example_classification_project) in single run mode with
this entrypoint:

````shell
python -u -m src.classification_training.classification_trainer
````

Alternatively you can run the sweep the provided
[example project](examples/example_classification_project) with this entrypoints in
two terminals:

You need to set the env variables first, but **don't set those secrets directly in the
example project!** Instead, configure them in your operating system:

- WANDB_USERNAME
- WANDB_API_KEY
- WANDB_ENTITY

````shell
python -u -m src.classification_training.wandb_utils.sweep_server
````

````shell
python -u -m src.classification_training.wandb_utils.sweep_agent
````

### Build Package Locally

````shell
python -m build 
````