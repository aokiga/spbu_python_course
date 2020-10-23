"""Contract decorator for hw3."""


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object


def check_args_types(arg_types, args):
    """
    Check whether args_types and types of args match.

    If arg_types is None, returns True.

    Args:
        arg_types: Required argument types.
        args: Arguments to check types.

    Returns:
        True if types of args and arg_types match, False otherwise.
    """
    if arg_types is None:
        return True
    if len(arg_types) != len(args):
        return False
    isinstances = map(
        lambda pair: isinstance(pair[0], pair[1]),
        zip(args, arg_types),
    )
    return all(isinstances)


def check_raises(function, raises, args):
    """
    Check if function raises allowed exception.

    If raises is None, no check would be performed.

    Args:
        function: Function.
        raises: Allowed exceptions.
        args: Args of function.

    Raises:
        ContractError: If a mismatch was found.
        Exception: Allowed function exception.

    Returns:
        Value of function.
    """
    if raises is None:
        return function(*args)
    try:
        result_value = function(*args)
    except Exception as function_exception:
        isinstances_raises = map(
            lambda exc: isinstance(function_exception, exc),  # noqa: F821
            raises,
        )
        if not any(isinstances_raises):
            raise ContractError() from function_exception
        raise function_exception
    return result_value


def check_return_type(return_type, result_value):
    """
    Check whether type of result_value and return_type match.

        Returns True if return_type is None.

    Args:
        return_type: Required result_value type.
        result_value: Value to check type.

    Returns:
        True if types of result_value and return_type match, False otherwise.
    """
    if return_type is None:
        return True
    return isinstance(result_value, return_type)


def contract(arg_types=None, return_type=None, raises=None):
    """
    Return decorator which checks types.

    Decorator checks types of arguments, type of return, raised exceptions.

    Args:
        arg_types: Required types of arguments.
        return_type: Required types of return value.
        raises: Exceptions that function can raise.

    Raises:
        ContractError: If a mismatch was found.

    Returns:
        Decorator.
    """
    def decorator(function):
        def wrapped(*args):  # noqa: WPS430
            if not check_args_types(arg_types, args):
                raise ContractError()

            result_value = check_raises(function, raises, args)

            if not check_return_type(return_type, result_value):
                raise ContractError()

            return result_value
        return wrapped
    return decorator
