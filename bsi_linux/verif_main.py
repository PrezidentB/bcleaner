import os
import logging

logging.basicConfig(filename='./logs/bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)

def check_file():
    file_path = os.getcwd()
    if os.path.exists(file_path):
        return
    else:
        logging.error(f"The file {file_path} is missing")

