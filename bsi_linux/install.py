from bcleaner import sudo
import os

def install():
    home = sudo.get_euid()
    cwd = os.getcwd()

    # If path does not exist, create it
    if not os.path.exists(f'{home}/.config/systemd/user'):
        print("Creating directory ~/.config/systemd/user")
        os.makedirs(f'{home}/.config/systemd/user')
        
    # Install the Bcleaner service
    with open(f'{home}/.config/systemd/user/bcleaner.service', 'w') as f:
        f.write(f"""[Unit]
Description=Bcleaner Service
Before=shutdown.target reboot.target
              
[Service]
Type=Oneshot
RemainAfterExit=true
ExecStop=/usr/bin/python3 {cwd}/main.py
                
[Install]
WantedBy=multi-user.target \n""")
        
if __name__ == '__main__':
    install()