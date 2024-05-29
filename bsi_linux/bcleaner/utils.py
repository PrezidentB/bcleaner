import argparse
import sys

def start():
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
    parser.add_argument('-c', '--cookies', action='store_true', help='Delete local cookies.')
    parser.add_argument('-bh', '--bash_hist', action='store_true', help='Clear up bash_history file.')
    parser.add_argument('-ph', '--python_hist', action='store_true', help='Clear up python_history file (Might not work on all systems).')
    args = parser.parse_args()
    return args