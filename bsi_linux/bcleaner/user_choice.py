import os
import logging

logging.basicConfig(filename='../logs/bcleaner.log', filemode='w', format='%(asctime)s - %(message)s' ,level=logging.INFO)

def delete_temp_file(args: dict):
    # Demander à l'utilisateur de saisir le chemin du fichier temporaire
    if args['directory']:
        temporary_file_path = input("Veuillez saisir le chemin du fichier temporaire que vous souhaitez supprimer : ").strip()
        # Vérifier si le chemin du fichier temporaire est valide
        if os.path.exists(temporary_file_path):
            try:
                # Supprimer le fichier temporaire
                os.unlink(temporary_file_path)
                logging.info(f"Le fichier '{temporary_file_path}' a été supprimé avec succès.")
            except Exception as e:
                logging.error(f"Erreur lors de la suppression du fichier '{temporary_file_path}': {e}")
        else:
            logging.error(f"Le chemin '{temporary_file_path}' ne correspond à aucun fichier existant.")
    else:
        logging.info("Aucun fichier temporaire à supprimer.")
        return 1