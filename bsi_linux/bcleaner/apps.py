import os
import logging
from pprint import pprint

logging.basicConfig(filename='./bcleaner/logs/bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)

def cached_apps(args: dict, home_dir: str):
    if args['apps']:
        logging.info('Deleting files in ~/.cache directory.')
        cache_path = home_dir + '/.cache'
        
        subfolders = [f.path for f in os.scandir(cache_path) if f.is_dir()]
        subfiles = [f.path for f in os.scandir(cache_path) if f.is_file()]

        for folder in subfolders:
            try:
                os.rmdir(folder)
                logging.info(f"Folder '{folder}' deleted.")
            except Exception as e:
                logging.error(f"Error when deleting folder '{folder}': {e}")
        
        for file in subfiles:
            try:
                os.unlink(file)
                logging.info(f"File '{file}' deleted.")
            except Exception as e:
                logging.error(f"Error when deleting file '{file}': {e}")
        return 0
    else:
        logging.info('No apps cache to delete.')
        return 1