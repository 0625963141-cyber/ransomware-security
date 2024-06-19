import os
import time

# Chemin du répertoire à surveiller
directory_to_watch = '/chemin/vers/votre/repertoire'

# Fonction pour vérifier les modifications dans le répertoire surveillé
def check_directory_changes(directory):
    files_before = os.listdir(directory)
    time.sleep(60)  # Attendre 1 minute
    files_after = os.listdir(directory)
    
    # Comparer les listes de fichiers avant et après
    if files_before != files_after:
        # Détecter une modification suspecte (par exemple, nouveaux fichiers chiffrés)
        print("Modification détectée dans le répertoire surveillé !")
        # Ajoutez ici votre logique de gestion des ransomwares (par exemple, alerte, restauration de sauvegarde, etc.)
    else:
        print("Aucune modification détectée.")

# Boucle principale pour surveiller en continu
while True:
    check_directory_changes(directory_to_watch)
