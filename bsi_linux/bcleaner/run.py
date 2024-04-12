from .sudo import *
from .apps import * 
from .history import *
from .user_choice import *
from .utils import start

def all():
    args = start()
    home = get_euid()
    cached_apps(args, home)
    bash_history(args, home)
    delete_temp_file(args)