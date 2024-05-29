import os
import logging
import re

# Logging configuration 
logging.basicConfig(filename='./bcleaner/logs/bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)

def browser_cookie(args: dict, home_dir: str):
    if args['cookies']:
        # For mozilla firefox
        if os.path.exists(home_dir + '/.mozilla'):

            logging.info('Deleting browser cookies.')
            
            firefox = home_dir + '/.mozilla/firefox/'
            subfolders = [f.name for f in os.scandir(firefox) if f.is_dir()]
            # Only in the default-release folder
            match = [m for m in subfolders if re.match(r'.*.default-release', m)]
            cookies = firefox + "".join(match) + '/cookies.sqlite'

            logging.info(f"Deleting cookies from {cookies}")
            os.unlink(cookies)

        # For google chrome
        elif os.path.exists(home_dir + '/.config/google-chrome'):

            logging.info('Deleting browser cookies.')
            chrome = home_dir + '/.config/google-chrome/Default/Cookies'
            logging.info(f"Deleting cookies from {chrome}")
            os.unlink(chrome)

        # For chromium
        elif os.path.exists(home_dir + '/.config/chromium'):

            logging.info('Deleting browser cookies.')
            chromium = home_dir + '/.config/chromium/Default/Cookies'
            logging.info(f"Deleting cookies from {chromium}")
            os.unlink(chromium)

        else:
            logging.error('No browser cookies found.')

    else:
        logging.info('No browser cookies to delete.')