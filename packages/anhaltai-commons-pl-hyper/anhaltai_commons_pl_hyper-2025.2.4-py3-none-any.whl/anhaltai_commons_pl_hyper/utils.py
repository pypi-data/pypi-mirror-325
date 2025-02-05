from typing import Any, get_args, get_origin, Literal


def validate_literal(value: Any, literal_type):
    """
    Dynamically test if the value is accepted by a given literal_type.
    Args:
        value: any literal value of any type
        literal_type: the given literal type

    Returns:
        value (unchanged) if value is accepted by literal_type, else raise an error
    """
    if get_origin(literal_type) is Literal:
        if value in get_args(literal_type):
            return value
        raise ValueError(f"value {value} is not a Literal of type {literal_type}")
    raise TypeError(f"{literal_type} is not a Literal type")
