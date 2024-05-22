import argparse
import sys

#### COLOR CONSTANT ####
BOLD = "\033[1m"

GREEN = "\033[0;32m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"

END = "\033[0m"
########################


banner = f"""{BLUE}
██████╗  ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██████╔╝██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██╔══██╗██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{END} """

def start():
    print(banner)
    args = parsing_args()
    clean_args = {}
    for key, value in args.__dict__.items():
        clean_args[key] = value
    return clean_args # easier to work with a dictionnary than a Namespace object 

def parsing_args():
    if len(sys.argv) == 1:
        print('No arguments given. Use -h or --help for help.')
        sys.exit(1)
    parser = argparse.ArgumentParser(description='A mini CCleaner by BSI team.')
    parser.add_argument('-a', '--apps', action='store_true', help='Delete a list of app files in ~/.cache/')
    # parser.add_argument('-t', '--temp', action='store_true', help='Delete all temporary files in /temp/')
    parser.add_argument('-c', '--cookies', action='store_true', help='Delete all cookies from your browser.')
    # parser.add_argument('-d', '--directory', action='store_true', help=f'Delete a directory of your choice {RED}{BOLD}/!\ DON\'T DO ANYTHING STUPID /!\.{END}{END}')
    parser.add_argument('-bh', '--bash_hist', action='store_true', help='Clear up bash_history file.')
    parser.add_argument('-ph', '--python_hist', action='store_true', help='Clear up python_history file.')
    args = parser.parse_args()
    return args