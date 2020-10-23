"""Contract decorator for hw3."""


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object


def check_args_types(arg_types, args):
    if arg_types is None:
        return True
    if len(arg_types) != len(args):
        return False
    isinstances = map(lambda x: isinstance(x[0], x[1]), zip(args, arg_types))
    return all(isinstances)


def check_raises(function, raises, args):
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
    if return_type is None:
        return True
    return isinstance(result, return_type)


def contract(arg_types=None, return_type=None, raises=None):
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
