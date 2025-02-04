from mypythonproject_clodo.cli.utils import *

def mynewfunction():
    return

decorate_all_functions_within_module(show_signature_if_no_args, globals())
decorate_all_functions_within_module(with_custom_print, globals())