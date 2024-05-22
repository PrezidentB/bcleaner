import os
import logging
from pprint import pprint

logging.basicConfig(filename='bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)


def cached_apps(args: dict, home_dir: str):
    if args['apps']:
        logging.info('Deleting apps cache...')
        return 0
    else:
        logging.info('No apps cache to delete.')
        return 1