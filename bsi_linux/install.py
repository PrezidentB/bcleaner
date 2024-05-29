from bcleaner import sudo
import os

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

def install():
    print(banner)

    home = sudo.get_euid()
    cwd = os.getcwd()

    # If path does not exist, create it
    if not os.path.exists(f'{home}/.config/systemd/user'):
        print("Creating directory ~/.config/systemd/user\n")
        os.makedirs(f'{home}/.config/systemd/user')
    
    if not os.path.exists(f'{cwd}/../logs'):
        print("Creating log directory.\n")
        os.makedirs(f'{cwd}/../logs')
        
    # Install the Bcleaner service
    with open(f'{home}/.config/systemd/user/bcleaner.service', 'w') as f:
        f.write(f"""[Unit]
Description=Bcleaner Service
Before=shutdown.target reboot.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=whoami
ExecStop=/usr/bin/python3 {cwd}/main.py -a -bh -ph

[Install]
WantedBy=default.target\n""")
    
    print("Service installed successfully.\n")
    print("To reload your services, run 'systemctl --user daemon-reload'")
    print("To enable the service, run 'systemctl --user enable bcleaner.service'")
    print("To start the service, run 'systemctl --user start bcleaner.service'")
        
if __name__ == '__main__':
    install()