from bcleaner import sudo
import os

def install():
    home = sudo.get_euid()
    cwd = os.getcwd()

    # If path does not exist, create it
    if not os.path.exists(f'{home}/.config/systemd/user'):
        print("Creating directory ~/.config/systemd/user")
        os.makedirs(f'{home}/.config/systemd/user')
    
    if not os.path.exists(f'{cwd}/../logs'):
        print("Creating directory log directory.")
        os.makedirs(f'{cwd}/../logs')
        
    # Install the Bcleaner service
    with open(f'{home}/.config/systemd/user/bcleaner.service', 'w') as f:
        f.write(f"""[Unit]
Description=Bcleaner Service
Before=shutdown.target reboot.target
              
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStop=/usr/bin/python3 {cwd}/main.py
                
[Install]
WantedBy=multi-user.target \n""")
    
    print("Service installed successfully.")
    print("To reload the service, run 'systemctl --user daemon-reload'")
    print("To enable the service, run 'systemctl --user enable bcleaner.service'")
    print("To start the service, run 'systemctl --user start bcleaner.service'")
        
if __name__ == '__main__':
    install()