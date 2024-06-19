import os
import hashlib
from config import DIRECTORY_TO_WATCH

class FileMonitor:
    def __init__(self):
        self.last_known_files = self._get_files_snapshot()

    def _get_files_snapshot(self):
        """
        Retourne un dictionnaire avec les fichiers du répertoire à surveiller
        et leurs empreintes hash.
        """
        files_snapshot = {}
        for root, _, files in os.walk(DIRECTORY_TO_WATCH):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = self._get_file_hash(file_path)
                files_snapshot[file_path] = file_hash
        return files_snapshot

    def _get_file_hash(self, file_path):
        """
        Calcule l'empreinte hash MD5 du fichier spécifié.
        """
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buffer = f.read()
            hasher.update(buffer)
        return hasher.hexdigest()

    def check_changes(self):
        """
        Vérifie les modifications apportées aux fichiers depuis la dernière
        vérification et retourne la liste des fichiers modifiés.
        """
        current_files = self._get_files_snapshot()
        changed_files = []

        for file_path, current_hash in current_files.items():
            if file_path not in self.last_known_files:
                changed_files.append(file_path)
            elif self.last_known_files[file_path] != current_hash:
                changed_files.append(file_path)

        self.last_known_files = current_files
        return changed_files

# Exemple d'utilisation
if __name__ == "__main__":
    monitor = FileMonitor()

    try:
        while True:
            changed_files = monitor.check_changes()
            if changed_files:
                print("Modification détectée dans les fichiers :")
                for file in changed_files:
                    print(file)
            time.sleep(300)  # Attendre 5 minutes entre chaque vérification

    except KeyboardInterrupt:
        print("\nArrêt de la surveillance.")
