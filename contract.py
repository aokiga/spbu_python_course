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
    isinstances = map(lambda x: isinstance(x[0], x[1]), zip(args, arg_types))
    return all(isinstances)


def check_raises(function, raises, args):
    """
    Check if function raises allowed exception.
    If raises is None, no check would be performed.

    Args:
        func: Function.
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
        result = function(*args)
    except Exception as e:
        if not any(map(lambda x : isinstance(e, x), raises)):
            raise ContractError() from e
        raise e
    return result


def check_return_type(return_type, result):
    """
    Check whether type of result and return_type match.
    Returns True if return_type is None.

    Args:
        return_type: Required result type.
        result: Value to check type.

    Returns:
        True if types of result and return_type match, False otherwise.
    """
    if return_type is None:
        return True
    return isinstance(result, return_type)


def contract(arg_types=None, return_type=None, raises=None):
    """
    Decorator which checks argument types, raised exceptions and return type.

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
        def wrapped(*args):
            if not check_args_types(arg_types, args):
                raise ContractError()
            
            result = check_raises(function, raises, args)
            
            if not check_return_type(return_type, result):
                raise ContractError()                
           
            return result
        return wrapped
    return decorator
