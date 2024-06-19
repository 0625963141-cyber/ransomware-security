import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import DIRECTORY_TO_WATCH

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.changed_files = []

    def on_modified(self, event):
        if event.is_directory:
            return
        self.changed_files.append(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return
        self.changed_files.append(event.src_path)

    def get_changed_files(self):
        changed_files = self.changed_files
        self.changed_files = []
        return changed_files

class FileMonitor:
    def __init__(self):
        self.event_handler = FileChangeHandler()
        self.observer = Observer()
        self.observer.schedule(self.event_handler, DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

    def check_changes(self):
        return self.event_handler.get_changed_files()

    def stop(self):
        self.observer.stop()
        self.observer.join()

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
            time.sleep(5)  # Attendre 5 secondes entre chaque vérification

    except KeyboardInterrupt:
        monitor.stop()
        print("\nArrêt de la surveillance.")
