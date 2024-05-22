import os

def get_euid():
    euid = os.geteuid()
    username = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))
    home = os.path.expanduser(f'~{username}')
    if euid == 0:
        raise PermissionError("You might want to run this script normally, not as sudo.")
    print(f"Running as : {username} with home directory: {home}")
    return home