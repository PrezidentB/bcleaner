import os
import logging

logging.basicConfig(filename='./bcleaner/logs/bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)

def bash_history(args: dict,home: str):
    # Chemin vers le fichier d'historique des commandes
    bash_history_path = home + "/.fake_history" # for testing purposes
    python_history_path = home + "/.gne_history" # for testing purposes

    if args['bash_hist']:
        # Vérifier si le fichier d'historique des commandes existe
        if os.path.exists(bash_history_path):
            try:
                # Ouvrir le fichier d'historique et le vider
                with open(bash_history_path, 'w'):
                    pass
                logging.info("Bash history cleared.")
            except Exception as e:
                logging.error(f"Error when clearing file : {e}")
        else:
            logging.error(f"File '{bash_history_path}' not found.")
    else:
        logging.info("No bash history to clear.")
    
    if args['python_hist']:
        if os.path.exists(python_history_path):
            try:
                with open(python_history_path, 'w'):
                    pass
                logging.info("Python history cleared.")
            except Exception as e:
                logging.error(f"Error when clearing file : {e}")
        else:
            logging.error(f"File '{python_history_path}' not found.")
    else:
        logging.info("No python history to clear.")
        return 1