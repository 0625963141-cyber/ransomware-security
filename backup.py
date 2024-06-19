import os
import shutil
from datetime import datetime
from config import DIRECTORY_TO_WATCH, BACKUP_DIRECTORY

class BackupManager:
    def __init__(self, source_directory=DIRECTORY_TO_WATCH, backup_directory=BACKUP_DIRECTORY):
        self.source_directory = source_directory
        self.backup_directory = backup_directory

    def backup_files(self, changed_files):
        """
        Sauvegarde les fichiers modifiés dans le répertoire de sauvegarde.
        """
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        for file_path in changed_files:
            try:
                relative_path = os.path.relpath(file_path, self.source_directory)
                backup_path = os.path.join(self.backup_directory, timestamp, relative_path)
                os.makedirs(os.path.dirname(backup_path), exist_ok=True)
                shutil.copy2(file_path, backup_path)
                print(f"Fichier sauvegardé : {backup_path}")
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de {file_path} : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    backup_manager = BackupManager()
    # Exemple de fichiers modifiés
    changed_files = ['/chemin/vers/votre/repertoire/file1.txt', '/chemin/vers/votre/repertoire/file2.txt']
    backup_manager.backup_files(changed_files)
