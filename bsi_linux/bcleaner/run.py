from .sudo import *
from .apps import * 
from .history import *
from .cookies import *
from .knwon_hosts import *
from .utils import start

def all():
    args = start()
    home = get_euid()
    cached_apps(args, home)
    cmd_history(args, home)
    browser_cookie(args, home)
    known_hosts(args, home)
