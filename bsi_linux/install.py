from bcleaner import sudo
import os

def install():
    sudo.get_euid()
    cwd = os.getcwd()

    # Install the Bcleaner service
    with open('/etc/systemd/system/bcleaner.service', 'w') as f:
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