def typecheck(expected_type):
    def inner(func):
        def wrapper(obj, value):
            if type(value) is not expected_type:
                raise ValueError(f"Expected '{str(expected_type)}', got type '{type(value)}'")
            
            func(obj, value)

        return wrapper
    return inner
