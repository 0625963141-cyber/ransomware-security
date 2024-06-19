from surveillance.file_monitor import FileMonitor
from detection.ransomware_detector import RansomwareDetector
from protection.backup import BackupManager
from protection.alert_system import AlertSystem

# Configuration initiale (exemple)
directory_to_watch = '/chemin/vers/votre/repertoire'
backup_directory = '/chemin/vers/votre/repertoire_de_sauvegarde'

def main():
    # Initialisation des composants
    file_monitor = FileMonitor(directory_to_watch)
    ransomware_detector = RansomwareDetector()
    backup_manager = BackupManager(directory_to_watch, backup_directory)
    alert_system = AlertSystem()

    try:
        while True:
            # Surveiller les modifications de fichiers
            changed_files = file_monitor.check_changes()

            # Détecter les comportements suspects de ransomware
            if ransomware_detector.detect_suspicious_behavior(changed_files):
                # Si un comportement suspect est détecté, prendre des mesures
                backup_manager.backup_files(changed_files)
                alert_system.send_alert()

            # Pause de surveillance (par exemple, toutes les 5 minutes)
            time.sleep(300)

    except KeyboardInterrupt:
        print("\nArrêt de la surveillance.")

if __name__ == "__main__":
    main()
