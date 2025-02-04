import inspect
from functools import wraps
import os
import re
import sys
import types
from colorama import Fore

def show_signature_if_no_args(func):
    """
    A decorator that prints the function's signature if called without arguments.
    If called with arguments, it executes the function normally.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if no arguments were passed
        if not args and not kwargs:
            # Get the function's signature
            sig = inspect.signature(func)
            print(f"\n{' '*4}{func.__name__}{sig}")
            print_comments(func)
            
        else:
            # Call the function normally if arguments are provided
            return func(*args, **kwargs)
    return wrapper

# Define the custom print function
def custom_print(*args, **kwargs):
    # Format the output (centered and orange)
    text = " ".join(str(arg) for arg in args)
    orange = Fore.YELLOW  # Orange color code
    reset = Fore.RESET  # Reset color
    console_width = os.get_terminal_size().columns  # Assume console width is 80 characters
    centered_text = text.center(console_width)  # Center the text
    sys.stdout.write(f"\n{orange}{centered_text}{reset}\n")

# A local custom print decorator, that will not compromise functions relying on the vanilla print.
# while also avoiding the need for manually customizing print functions.
def with_custom_print(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Backup the original print function using import
        import builtins
        original_print = builtins.print

        # Override print with the custom print function
        builtins.print = custom_print

        try:
            # Execute the function with the custom print
            return func(*args, **kwargs)
        finally:
            # Restore the original print function after execution
            builtins.print = original_print

    return wrapper

def print_comments(func):
    source = inspect.getsource(func)
    comments = re.findall(r'''"""(.*?)"""''', source, re.DOTALL) 

    for comment in comments:
        print(comment)

def decorate_all_functions_within_module(decorator, global_scope):
    """
    Apply the given decorator to all functions in the current module.
    """

    # for name, obj in global_scope.items():
    #     if inspect.isfunction(obj):
    #         print(f"Function: {name}, Module: {getattr(obj, '__module__', None)}")

    filtered_globals = {
        name: obj for name, obj in global_scope.items()
        if inspect.isfunction(obj) and getattr(obj, "__module__", None) == "mypythonproject_clodo.sample_module.sample_module"
    }

    current_globals = filtered_globals
    for name, obj in current_globals.items():
        if isinstance(obj, types.FunctionType) and name not in ['wraps', 'show_signature_if_no', 'decorate_all_functions_within_module']:  # Check if it's a function
            global_scope[name] = decorator(obj)






