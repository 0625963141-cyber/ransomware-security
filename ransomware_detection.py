import os
from config import DIRECTORY_TO_WATCH

class RansomwareDetector:
    def __init__(self, suspicious_extensions=['.encrypted', '.locked']):
        self.suspicious_extensions = suspicious_extensions

    def detect_suspicious_behavior(self, changed_files):
        """
        Détecte les comportements suspects basés sur les extensions de fichiers modifiés.
        """
        for file_path in changed_files:
            _, extension = os.path.splitext(file_path)
            if extension in self.suspicious_extensions:
                print(f"Comportement suspect détecté : {file_path}")
                return True
        return False

# Exemple d'utilisation
if __name__ == "__main__":
    detector = RansomwareDetector()
    # Exemple de fichiers modifiés
    changed_files = ['/chemin/vers/votre/repertoire/file1.encrypted', '/chemin/vers/votre/repertoire/file2.txt']
    if detector.detect_suspicious_behavior(changed_files):
        print("Alerte : Ransomware détecté !")
