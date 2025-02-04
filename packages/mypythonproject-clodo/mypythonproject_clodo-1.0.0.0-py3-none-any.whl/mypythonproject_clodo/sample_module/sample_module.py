from mypythonproject_clodo.cli.utils import *

# @show_signature_if_no_args

def sample_function(arg1, arg2, *args, **kwargs):
    """
    Parameters
    ----------
    Prints the sum of floats.

    Parameters
    ----------
    arg1 : float : Addend
    arg2 : float : Addend
    *args : float : Addend
    **kwargs : float : Addend

    Returns
    -------
    float : Result of sum.

    Raises
    ------
    ValueError : If result is too big.
    """
    total = arg1 + arg2 + sum(args) + sum(kwargs.values())
    import sys
    if total > sys.float_info.max:
        raise ValueError("Result exceeded floating-point max limit!")
    custom_print(total)


decorate_all_functions_within_module(show_signature_if_no_args, globals())
decorate_all_functions_within_module(with_custom_print, globals())