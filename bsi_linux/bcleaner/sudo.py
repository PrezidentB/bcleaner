import os

def get_euid():
    euid = os.geteuid()
    username = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))
    home = os.path.expanduser(f'~{username}')
    if euid != 0:
        raise PermissionError("You need to run this script as sudo.")
    print(f"Running as sudo: {username} with home directory: {home}")
    return home