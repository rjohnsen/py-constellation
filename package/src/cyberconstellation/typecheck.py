"""
Typecheck decorator module
"""

def typecheck(expected_type):
    """
    Typecheck decorator

    Parameters:
    value (bool): State

    Returns:
    bool:Returning value
    """
    def inner(func):
        """
        Parameters:
        func (func): Reference to calling class

        Returns:
        wrapper:Returning wrapping function
        """
        def wrapper(obj, value):
            """
            Wrapper function containing typecheck

            Parameters:
            obj (obj): Reference to calling class
            value (mixed): Value to test for type

            Returns:
            func:Returning value, same as passed in
            """
            if isinstance(value, expected_type) is False:
                raise ValueError(f"Expected '{str(expected_type)}', got type '{type(value)}'")

            func(obj, value)

        return wrapper
    return inner
