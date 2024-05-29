from .sudo import *
import os
import sys
import argparse

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
╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{END}"""

def start():
    args = parsing_args()
    clean_args = {}
    for key, value in args.__dict__.items():
        clean_args[key] = value
    return clean_args # Easier to work with a dictionnary than a Namespace object 

def parsing_args():
    if len(sys.argv) == 1:
        print('No arguments given. Use -h or --help for help.')
        sys.exit(1)
    parser = argparse.ArgumentParser(description='A mini CCleaner by BSI team.')
    parser.add_argument('-a', '--apps', action='store_true', help='Delete all app caches in ~/.cache/')
    parser.add_argument('-c', '--cookies', action='store_true', help='Delete your browser cookies.')
    parser.add_argument('-bh', '--bash_hist', action='store_true', help='Clear up bash_history file.')
    parser.add_argument('-ph', '--python_hist', action='store_true', help='Clear up python_history file (Might not work on all systems).')
    args = parser.parse_args()
    return args

def install(args: dict):
    print(banner)
    print("Welcome to bcleaner, a temporary file cleaner for Linux.\n")

    # Variables
    apps = ''
    cook = ''
    bash = ''
    python = ''
    home = get_euid()
    cwd = os.getcwd()

    # If path does not exist, create it. Service directory
    if not os.path.exists(f'{home}/.config/systemd/user'):
        print("Creating directory ~/.config/systemd/user\n")
        os.makedirs(f'{home}/.config/systemd/user')
    
    # If path does not exist, create it. Log directory
    if not os.path.exists(f'{cwd}/../logs'):
        print("Creating log directory.\n")
        os.makedirs(f'{cwd}/../logs')
    
    # Get all the arguments to put them directly in the service file.
    for key, value in args.items():
        if value:
            if key == 'apps':
                apps = '-a'
            if key == 'cookies':
                cook = '-c'
            if key == 'bash_hist':
                bash = '-bh'
            if key == 'python_hist':
                python = '-ph'

    # Install the Bcleaner service.
    with open(f'{home}/.config/systemd/user/bcleaner.service', 'w') as f:
        f.write(f"""[Unit]
Description=Bcleaner Service
Before=shutdown.target reboot.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/python3 {cwd}/verif_main.py
ExecStop=/usr/bin/python3 {cwd}/main.py {apps} {cook} {bash} {python}

[Install]
WantedBy=default.target\n""")
    
    print("Service installed successfully.\n")
    print("To reload your services, run 'systemctl --user daemon-reload'")
    print("To enable the service, run 'systemctl --user enable bcleaner.service'")
    print("To start the service, run 'systemctl --user start bcleaner.service'")