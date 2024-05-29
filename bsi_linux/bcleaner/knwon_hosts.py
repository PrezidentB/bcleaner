import os
import logging

# Logging configuration 
logging.basicConfig(filename='./bcleaner/logs/bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)

def known_hosts(args: dict, home_dir: str):
    if args['known_hosts']:
        logging.info('Deleting ssh known_hosts file.')

        if os.path.exists(f'{home_dir}/.ssh/known_hosts'):
            try:
                with open(f'{home_dir}/.ssh/known_hosts', 'w') as f:
                    pass
                logging.info('Known hosts file cleared.')
            except Exception as e:
                logging.error(f'Error while clearing known hosts file: {e}')
        else:
            logging.info('No known hosts file found.')
    else:
        logging.info('No known hosts file to delete.')