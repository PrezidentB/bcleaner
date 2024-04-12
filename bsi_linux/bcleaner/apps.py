import os
from pprint import pprint

def cached_apps(args: dict, home_dir: str):
    if args['apps']:
        print('Deleting apps cache...')
        return 0
    else:
        print('No apps cache to delete.')
        return 1