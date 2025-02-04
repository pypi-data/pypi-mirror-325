import os
import sys
import code
import glob
import importlib
from importlib.metadata import metadata
import gc
from colorama import Fore
if sys.platform == "win32":
    import msvcrt
else:
    import termios
    import tty
import platform
import shutil
import subprocess
from tkinter import Tk, filedialog
from tkinter.filedialog import askdirectory
import pyautogui
import pyfiglet
from IPython.terminal.prompts import Prompts, Token
import json

__package__ = 'mypythonproject_clodo'

state = {
                    'selected_section': '',
                    'selected_module':{'':''},
                    'header':{},
                    'modules':{},
                    'help':{},
                }

def pymodularcli():
    
    if ipython_available():
        
        import IPython
        
        # IPython statement to allow functions to be called without parenthesis.
        load_meta_file('modules')
        load_meta_file('help')
        load_meta_file('header')
        load_meta_file('template')

        load_modules()
        
        fullscr = 'fullscreen()'   
        autocall = '%autocall 2'

        prompt_text = state['header']['brand_name'].replace(' ', '').lower()
        prompt_settings = f'''set_ipython_prompt("🟦 {prompt_text}")'''
        header_initialize = 'print_UI()'
        override_exit = "globals()['exit'] = cli_exit"  
        setup_commands = [fullscr, autocall, prompt_settings, header_initialize, override_exit]
        # Start IPython shell quietly if available
        IPython.start_ipython(argv=[], exit_code=0, user_ns=globals(), display_banner=False, exec_lines=setup_commands )
    else:
        # Fall back to regular Python shell
        code.interact(banner='', local=globals())


# The package map file (modules.json) is created during the build and placed in the first-level modules directory.
# It maps all the modules composing the package, giving the name, current version and description.
def load_meta_file(meta_file_name):
    modules_path = os.path.join(os.path.dirname(__file__), f"{meta_file_name}.json")
    with open(modules_path, 'r') as f:
        global state
        state[f"{meta_file_name}"] = json.load(f)

def get_selected_module_info(selected_module):
    module_name = selected_module['module_name']
    module_path = __package__ + '.' + module_name 
    return module_name, module_path

def modules():
    resetUI()    
    state['selected_section'] = 'modules'
    unload_module()
    display_modules(state['modules'])
globals()['modules'] = modules

def unload_module():
    selected_module  = state['selected_module']
    if 'module_name' in selected_module:
            module_name, module_path = get_selected_module_info(selected_module)
            module_deselect(module_path)
            globals()[f"{module_name}"] = globals().get(f"import_{module_name}")
            state['selected_module'] = {}

def help():
    resetUI()
    global state
    display_help(state['help'])
globals()['help'] = help

def functions():
    resetUI()
    print_functions(globals())
globals()['functions'] = functions

def ipython_available():
    try:
        import IPython
        return True
    except ImportError:
        return False
    
# Function to center text with padding
def center_text(text, width = None):
    if width == None:
        width = os.get_terminal_size().columns
    return text.center(width)

def move_cursor(row, col):
    """Moves the cursor to the specified row and column."""
    sys.stdout.write(f"\033[{row};{col}H")
    

def print_at_position(data_string, row, col):
    """Print the string at the specified row and column."""
    # input([row,col])
    move_cursor(row, col)
    print(data_string)
    sys.stdout.flush()

def read_char():
    """Read a single character from input, handling both Windows and Unix."""
    if sys.platform == "win32":
        return msvcrt.getwch()  # Windows version
    else:
        # Unix-based system: set terminal to raw mode to read a single char
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char

def get_cursor_position():
    """Retrieve the current cursor position (row, col) in Windows without printing artifacts."""
    
    # Send the escape sequence to query the cursor position
    sys.stdout.write("\033[6n")
    sys.stdout.flush()

    response = ""
    
    while True:
        char = read_char()   # Read one character at a time
        response += char
        if char == "R":  # End of response
            break

    # Parse the response
    if response.startswith("\x1b[") and response.endswith("R"):
        try:
            position = response[2:-1]  # Remove '\x1b[' and 'R'
            row, col = map(int, position.split(";"))
            return [row, col]
        except ValueError:
            raise Exception(f"Failed to parse cursor position: {response}")
    else:
        raise Exception(f"Unexpected response: {response}")

def hex_to_rgb(hex_color):
    """Convert hex color code to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_ansi_rgb(r, g, b):
    """Convert RGB values to ANSI RGB code."""
    return 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)

def tag(data_string, offset=[0,0], color_hex=None, padding = 1):

    start_position = get_cursor_position()

    row = start_position[0] + offset[0]
    col = start_position[1] + offset[1]

    tag_width = len(data_string) + 2 * padding
    tag_height = 1
    right_vertical_bars = ['\u23B9']
    left_vertical_bars = ['\u23B8']

    tw = tag_width
    th = tag_height
    hp = padding * ' '
    rvb = right_vertical_bars[0]
    lvb = left_vertical_bars[0]

    # If a color is provided, convert it to ANSI escape code
    if color_hex:
        r, g, b = hex_to_rgb(color_hex)
        ansi_color_code = rgb_to_ansi_rgb(r, g, b)
        color_code = f"\033[38;5;{ansi_color_code}m"  # Set the color
        reset_code = "\033[39m"  # Reset to default color
    else:
        color_code = ""
        reset_code = ""

    # Print the tag with the specified color and position
    print_at_position(f"{color_code}{' ' * 1}{'_' * tw}", row, col)
    print_at_position(f"{rvb}{hp}{data_string}{hp}{lvb}", row + 1, col)
    print_at_position(f"{' ' * 1}{'‾' * tw}{reset_code}", row + 2, col)


def print_tag_list(tag_list, offset = [0,0], color_hex=None, spacing = 6, alignment = 'left'):
    
    tag_padding = 1
    total_to_print = "".join(tag_list) + ' '*spacing*(len(tag_list) - 1) + 4 * ' '
    total_length = len(total_to_print)
    if alignment == 'center':
        terminal_width = os.get_terminal_size().columns
        offset[1] = int((terminal_width - total_length)/2)
    def recursive(tag_list, offset = [0,0], color_hex=None, spacing = 6, alignment = 'left'):
    
        if tag_list:
            tag_string = tag_list.pop()
            tag(tag_string, offset, color_hex, padding = tag_padding)
            offset[1] += len(tag_string) + spacing
            recursive(tag_list, [-3, offset[1]], color_hex, spacing, alignment)    
        return
    recursive(tag_list, offset, color_hex, spacing, alignment)

def print_pretty_ascii(app_name, color_hex = None):
    # Generate ASCII art from the input text
    ascii_art = pyfiglet.figlet_format(app_name)

    # Get the width of the terminal
    terminal_width = os.get_terminal_size().columns

    # Split the ASCII art into lines
    lines = ascii_art.splitlines()

    # If a color is provided, convert it to ANSI escape code
    if color_hex:
        r, g, b = hex_to_rgb(color_hex)
        ansi_color_code = rgb_to_ansi_rgb(r, g, b)
        color_code = f"\033[38;5;{ansi_color_code}m"  # Set the color
        reset_code = "\033[39m"  # Reset to default color
    else:
        color_code = ""
        reset_code = ""

    # Print each line centered
    for line in lines:
        centered_line = line.center(terminal_width)
        print(f"{color_code}{centered_line}{reset_code}")   

def print_info_box():
    pass

def print_startup_info():
    pass

#Declaring existing commands to be displayed in the navbar
navbar_commands = {
                'new' : 'initializes a new project directory',
                'browse' : 'working directory selection',
                'files' : 'opens the project files manager',
                'modules' : 'module selection',
                'functions' : 'lists functions for current module',
                # 'run script' : 'run python script',
                # 'save' : 'save iPython session as script',
                'clear'   : 'clear interface',
                'help' : 'extra information on commands',
                'exit' : 'custom cli exit',
                }

def tags():
    #Defines tags contents

    project_section = metadata(__package__)
    # pkg_author = project_section.get("Author", next((value for key, value in project_section.items() if key.lower() == "author-email"), "Unknown Email")).strip()
    # pkg_description = project_section.get("Summary", "No Description Available").strip()
    license = f"{project_section.get("License", "-").strip().upper()}" 
    list = {
        'python_version' : f"Python {sys.version.split(" ")[0].strip()}",
        'OS' : f"{platform.platform()}".strip().upper(),
        'license' : license,
        'path' : f"{os.getcwd()}",
    }
    return list


def print_UI():

    print("\033[H\033[J\033[3J", end="")  # Clear screen and scrollback buffer    
    header(os.get_terminal_size().columns)
    print_tag_list([tags()['license'], tags()['OS'], tags()['python_version']], offset = [0,0], color_hex = '#FFD43B', spacing = 6, alignment= 'center')    
    navbar(navbar_commands)
    tag(tags()['path'], offset = [0,4], color_hex='#FFE873')    

def header(terminal_width = os.get_terminal_size().columns):
    state['selected_section'] == ''
    header_width = terminal_width
    # Fetch pyproject header section
    header_data = state['header']
    brand_name = header_data['brand_name']
    slogan = header_data['slogan']
    creators = header_data['creators']
    # print_pretty_ascii(package_name, '#1B3B6F')
    print_pretty_ascii(brand_name, '#1010EE')
    print()
    print(center_text(slogan, header_width))
    print()
    for creator in creators:
        print(center_text(f"{creator['name']} <{creator['email']}>", header_width))
    print()

def module_selection(global_scope, module_name):
    module_name = module_name.strip()
    module_path = (__package__.strip() + '.' + module_name.strip()).strip().lower()
    imported_objects = {}

    try:
        # Dynamically import the module
        module = importlib.import_module(module_path)
        # Use the passed global scope to assign imported attributes
        for attr_name in dir(module):
            if not attr_name.startswith("_"):  # Ignore private/protected attributes
                global_scope[attr_name] = getattr(module, attr_name)
                
                # Add to the dictionary for return
                imported_objects[attr_name] = getattr(module, attr_name)
                
                # Print the attribute being imported
                # print(f"Imported: {attr_name}")

        resetUI()

        state['selected_module'] = {'module_name':module_name, 'module_version':module.__version__, 'objects':imported_objects }
        
        # print(f"All functions and variables from '{module_path}' imported successfully.")
        print_functions(global_scope) 
        return imported_objects  # Return the dictionary with all imported attributes
    
    except ModuleNotFoundError:
        print(f"Error: Module '{module_path}' not found.")
    except Exception as e:
        print(f"Error importing from module '{module_path}': {e}")
        return {}


def is_substring_in_list(substring, string_list):
    return any(substring in s for s in string_list)

def module_deselect(module_path):
    """Attempts to fully unload a dynamically imported module and its global objects."""
    if module_path in sys.modules:
        module = sys.modules[module_path]

        # Remove global objects that belong to the module
        globals_to_remove = [
            obj for name, obj in state['selected_module']['objects'].items()
            if module_path in getattr(obj, "__module__", ' ')
        ]
        # Delete functions thrown into global scope
        for obj in globals_to_remove:
            exec(f"del(globals()['{obj.__name__}'])")

        # Delete the module reference
        del module

        # Run garbage collection
        gc.collect()


def print_functions(global_scope):

    terminal_width=os.get_terminal_size().columns
    left_padding = int(terminal_width / 3)
    print_section_title('functions')
    
    module_selected = state['selected_module']
    if 'module_name' not in module_selected:
        print(f"\n\n{Fore.LIGHTRED_EX}{' ' * left_padding} No module selected.{Fore.RESET}\n\n")
        return 
    
    module_name  = module_selected['module_name']
    module_version  = module_selected['module_version']
    objects  = module_selected['objects']
    # Selects only functions defined in the package's files.
    function_functions = {
        k: v
        for k, v in objects.items()
        if callable(v) 
        and getattr(v, "__module__", "").startswith(f"{__package__}.{module_name}")
    }
    
    terminal_width = os.get_terminal_size().columns
    indent = ' ' * int(terminal_width / 4)
    col_width = 25  # Adjust the column width as needed
    max_cols = max(1, terminal_width // col_width)  # Calculate max columns based on terminal width

    # Get function names
    procedure_names = list(function_functions.keys())

    # Split names into rows based on available columns
    rows = [procedure_names[i:i + max_cols] for i in range(0, len(procedure_names), max_cols)]

    # Print current module name and version
    print(f"{" " * 8}{Fore.LIGHTYELLOW_EX}{indent}{module_name.upper()} {module_version}{Fore.RESET}\n")

    # Print each row with equal spacing
    for row in rows:
        formatted_row = "".join(f"{name:<{col_width}}" for name in row)
        print(Fore.GREEN + indent + formatted_row + Fore.RESET)

    print(f"\n{'-' * terminal_width}".center(terminal_width))
    print(f"To view its signature, enter the function's name without arguments.\n")


def navbar(commands):

    project_section = metadata(__package__)
    pkg_version = project_section.get("Version", "Unknown Version").strip()

    # Console window size
    terminal_width = os.get_terminal_size().columns
    header_width = terminal_width

    fillers = ['░', '█', '▓', '▒']
    decoration_left = f"{fillers[1]*2}"
    title = f"{' '*1} {state['header']['brand_name']} {pkg_version}{' '*1}{fillers[3]*20}"
    # Format the command list
    print(f"{'_' * header_width}".center(header_width))
    command_line = f'{fillers[1]} ' + f" {fillers[1]} ".join(commands.keys()).upper() + f' {fillers[1]}'
    formatted_keys = decoration_left + title + command_line
    decoration_right = f"{fillers[3]*(header_width-len(formatted_keys))}"
    formatted_keys = formatted_keys + decoration_right
    print(formatted_keys)
    print(f"{'‾' * header_width}".center(header_width))


def display_modules(modules):
    terminal_width=os.get_terminal_size().columns
    left_padding = int(terminal_width / 3.5) 
    print_section_title('modules')
    for idx, (module, details) in enumerate(modules.items(), start=1):
        # print(f"[{idx}] {module.capitalize()} v{details['version']}")
        print(f"{Fore.LIGHTYELLOW_EX}{' ' * (left_padding)} ° {module} v{details['version']}{Fore.RESET}")
        print(f"{' ' * left_padding}   {details['description']}\n")

def display_help(help_info):
    resetUI()
    print_section_title('HELP')
    print_elegant_json(help_info)

def print_elegant_json(data, indent=4, width=os.get_terminal_size().columns, level=2):
    """
    Elegantly prints a hierarchical structure from a JSON-like object.

    Args:
        data (dict or list): The data to print (can be nested).
        indent (int): Number of spaces for indentation per level.
        width (int): The total width of the display (optional).
        level (int): Used internally for recursion to track depth.

    Returns:
        None
    """

    def recursive_print(obj, level):
        """Recursively print dictionary or list with indentation."""
        prefix = " " * (level * indent)  # Indentation based on level
        if isinstance(obj, dict):
            for key, value in obj.items():
                print(f"{Fore.LIGHTBLACK_EX}{prefix} {key}:{Fore.RESET}\n")
                recursive_print(value, level + 1)
        elif isinstance(obj, list):
            for item in obj:
                recursive_print(item, level)
        else:
            # Print leaf node (e.g., str, int, float)
            if 'http' in obj:
                print(f"{Fore.CYAN}{prefix}  {obj}{Fore.RESET}\n")
            else:
                print(f"{prefix}  {obj}\n")

    recursive_print(data, level)

def resetUI():
    state['selected_section'] = ''
    print_UI()
globals()['clear'] = resetUI

def cli_exit():
    """Custom exit function that works for both IPython and Python."""

    terminal_width = os.get_terminal_size().columns

    contributions_url = ''
    for item in metadata(__package__).values():
        if 'Contributions' in item:
            contributions_url = item.split(',')[1].strip()
            break
    contributions_url = Fore.CYAN + contributions_url + Fore.RESET
    ANSI_color_code_length_left_compansation = 2 * len(Fore.RESET) * ' '
    brand_name = state['header']['brand_name']
    contributions_message = ANSI_color_code_length_left_compansation  +  f"Show your support for {brand_name} at " + contributions_url

    thank_you = "\nThank you!"
    acknowledgments = ""
    
    print("\033[H\033[J\033[3J", end="")  # Clear screen and scrollback buffer 
    print('\n\n')
    header(os.get_terminal_size().columns)
    print_pretty_ascii(thank_you, '#FFD43B')
    print('\n\n')
    print(center_text(contributions_message, terminal_width))
    input()

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        from IPython import get_ipython
        ipython = get_ipython()
        if ipython is not None:
            # Print a message and exit IPython
            print("Exiting IPython...")
            os._exit(0)  # Force exit without cleanup
    except ImportError:
        pass

    # Exit standard Python
    os._exit(0)

def change_working_directory_explorer():
    """Change the working directory using a file explorer."""
    resetUI()

    # Suppress the Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    root.attributes('-topmost', True)  # Make the dialog appear on top

    # Open the file explorer to select a directory
    new_dir = askdirectory(title="Select New Working Directory")

    # Validate the directory selected
    if new_dir:
        try:
            os.chdir(new_dir)
            working_directory = os.getcwd()
            root.destroy()  # Ensure the root window is properly destroyed and control is given back to the terminal window
            print(f"Successfully changed the working directory to: {working_directory}")
            resetUI()
            if check_project_file():
                manage_project()
        except FileNotFoundError:
            print(f"Error: The directory '{new_dir}' does not exist.")
        except PermissionError:
            print(f"Error: You do not have permission to access '{new_dir}'.")
    else:
        print("No directory selected.")
        root.destroy() 
globals()['browse'] = change_working_directory_explorer



def create_new_project():
    resetUI()
    print_section_title('project creation')
    working_directory = os.getcwd()
    # print(f"Current working directory: {working_directory}")
    
    # Ask for the project name
    project_name = input(f"Enter the project name: ").strip()
    project_path = os.path.join(working_directory, project_name)

    folders = state['template']

    # Create the project folder
    os.makedirs(project_path, exist_ok=True)
    # Create the fixed directories with placeholder files
    def create_folder_recursivelly(folders, path):

        if len(folders) == 0:
            return
        
        for folder, content in folders.items():
            folder_path = os.path.join(path, folder)
            os.makedirs(folder_path, exist_ok=True)
            if isinstance(content, dict):
                create_folder_recursivelly(content, folder_path)    
                # with open(os.path.join(folder_path, "README.txt"), "w") as f:
                #     f.write(description)
        return
    create_folder_recursivelly(folders, project_path)

    os.chdir(project_path)

    # Create project .pyproj file
    with open(os.path.join('./', "project.pyproj"), "w") as f:
        f.write(f"pymodularcli Project {project_name}")

    resetUI()
    print(f"\nProject '{project_name}' created successfully:\n")
    manage_project()
globals()['new'] = create_new_project

def check_project_file(folder_path = './'):

    proj_files = glob.glob(os.path.join(folder_path, "*.pyproj"))
    
    if proj_files:
        return True
    else:
        width = os.get_terminal_size().columns
        padding_left = int(width/3.5)
        print(f"\n\n{Fore.LIGHTRED_EX}{' '*padding_left}No '.pyproj' project file found.\n\n")
        return False

def recursive_traversal(path_sequence, func, current_path = '.'):
            if len(path_sequence) == 0:
                func(current_path)
                manage_project()
                return
            subfolders = [subfolder for subfolder in os.listdir(current_path)]
            if path_sequence[0] in subfolders:
                current_path += ('/' + path_sequence.pop(0))
                recursive_traversal(path_sequence, upload_files, current_path)
            else:
                print("Invalid folder name. Please enter a valid folder or type 'exit' to leave.")
                manage_project()

def manage_project():

    resetUI()
    if check_project_file():
        width = os.get_terminal_size().columns
        print_section_title('file manager')
        
        print_project_structure('./')
        
        print("\nEnter a folder name to select its files using the explorer.")
        print("To leave the manager, press enter with the field empty.\n")
        
        folder_path = input("Enter folder name: ").strip()
        if len(folder_path) == 0:
            print("Exiting project management.")
            resetUI()
            return
        
        path_sequence = folder_path.split('/')
        recursive_traversal(path_sequence, upload_files)
globals()['files'] = manage_project

def print_project_structure(path, indent=4, is_root=True):
    """ Recursively prints the directory structure, including the root folder. """
    
    if is_root:
        print(f"|-- {os.path.basename(os.path.abspath(path))}\n")
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if item != 'project.pyproj':
            print(' ' * indent + '|-- ' + item)
        if os.path.isdir(item_path):
            print_project_structure(item_path, indent + 4, is_root=False)

def open_project_directory(path="."):
    path = os.path.abspath(path)
    system = platform.system()

    if system == "Windows":
        os.system(f'explorer "{path}"')
    elif system == "Darwin":  # macOS
        os.system(f'open "{path}"')
    elif system == "Linux":
        os.system(f'xdg-open "{path}"')
    else:
        print("Unsupported operating system")

def upload_files(destination_folder):
    # Oculta a janela principal do Tkinter
    root = Tk()
    root.withdraw()

    # Abre a janela para selecionar múltiplos arquivos
    file_paths = filedialog.askopenfilenames(title="Select files to upload")

    if not file_paths:
        print("No files selected.")
        return

    # Certifique-se de que a pasta de destino existe
    os.makedirs(destination_folder, exist_ok=True)

    # Copia os arquivos selecionados para a pasta de destino
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy(file_path, destination_path)
        # print(f"Uploaded: {file_name} -> {destination_folder}")
    
    root.destroy()  # Ensure the root window is properly destroyed and control is given back to the terminal window.

    # print("All selected files have been uploaded successfully.")

def fullscreen():
    """ Force terminal window to fullscreen based on the operating system. """
    
    current_os = platform.system()

    if current_os == "Windows":
        # Maximize the terminal window using keyboard shortcuts (Alt + Space, then X).
        pyautogui.hotkey('alt', 'space')  # Open the window menu
        pyautogui.press('x')  # Press 'x' to maximize

    elif current_os == "Linux":
        # For Linux, we use `wmctrl` to maximize the terminal window.
        subprocess.run(["wmctrl", "-r", ":ACTIVE:", "-b", "add,maximized_vert,maximized_horz"])

    elif current_os == "Darwin":
        # For macOS, use AppleScript to resize the terminal window.
        applescript = """
        tell application "Terminal"
            activate
            set bounds of front window to {0, 0, 1920, 1080}  -- Adjust the coordinates as needed
        end tell
        """
        subprocess.run(["osascript", "-e", applescript])

    else:
        print("Unsupported OS for fullscreen terminal window.")

def print_section_title(title):
    terminal_width = os.get_terminal_size().columns    
    width = terminal_width
    print(" ")
    print(" " * ((width - 10) // 2) + f"{title.upper()}")
    # print("=" * width)
    print(" ")

def get_selected_module():
    selected_module = state['selected_module']
    if 'module_name' in selected_module:
        return selected_module['module_name'] + '.'
    return ''

class MyPrompt(Prompts):
    def __init__(self, shell, text=''):  # Default: Gold
        super().__init__(shell)
        self.text = text

    def in_prompt_tokens(self, cli=None):
        return [
            # This is a little tricky... didn't manage to set custom colors, but found that specific properties have specfic colors. 
            # Name.Class, for example, has default as 'blue'. It seems each property, like PromptNum, Name.Entity, Name.Class has a style 
            # associated with it, instead of a functional thing, e.g., the counting feature works with properties other than PromptNum 
            # There are some other properties to find out and explore if needed.
            (Token.Name.Entity, f"[{self.shell.execution_count}]"),
            (Token.Name.Class, f"{' '*2}{self.text}"),
            (Token.Name.Class, f".{get_selected_module()}"),
        ]
    
    def out_prompt_tokens(self, cli=None):
        return []

def set_ipython_prompt(text, color = '#FFFFFF'):
    ip = get_ipython()
    if ip is None:
        print("Error: Not running inside an IPython session.")
        return
    ip.prompts = MyPrompt(ip, text)

# Creates a module switching system including every found module.
def load_modules():
    for module_name in state['modules'].keys():
        width = int(os.get_terminal_size().columns / 3)
        
        code_str = f"""
def import_{module_name}():
    if state['selected_section'] == 'modules': 
        module_selection(globals(), "{module_name}")
    else:
        resetUI()
        print("\\n\\n" + " " * {width} + "{Fore.LIGHTRED_EX}Select modules at the {Fore.WHITE}MODULES{Fore.LIGHTRED_EX} section.{Fore.RESET}\\n\\n")

globals()["{module_name}"] = import_{module_name}  # Assign function reference to globals()
"""

        exec(code_str, globals())  # Execute in global scope

