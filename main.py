import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import shutil

# Extension groups
FILE_TYPE_MAP = {
    "Documents" : ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Images" : ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.svg', '.ico'],
    "Videos" : ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.3gp'],
    "Archives" : ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.cab'],
    "Installer" : ['.exe', '.msi', '.deb', '.rpm', '.apk', '.dmg', '.pkg'],
    "Audio" : ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.wma', '.m4a', '.aiff', '.alac']
}

# Reverse lookup dictionary to map extension to folder
EXTENSION_TO_FOLDER = {
    ext: folder for folder, extensions in FILE_TYPE_MAP.items() for ext in extensions
}


downloads_path = os.path.expanduser("~/Downloads")

# Listen for any new downloads
class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or event.src_path.endswith(".part"):
            return

        # Wait to make sure file write is complete
        time.sleep(2)
        file_path = event.src_path
        file_ext = os.path.splitext(event.src_path)[1].lower()
        filename = os.path.basename(file_path)
            
        dest_folder_name = EXTENSION_TO_FOLDER.get(file_ext)

        if dest_folder_name:
            dest_folder = os.path.join(downloads_path, dest_folder_name)
            dest_path = os.path.join(dest_folder, filename)
            os.makedirs(dest_folder, exist_ok=True)              
            try:
                shutil.move(file_path, dest_path)
                print(f"Moved {filename} to {dest_folder_name}")
            except Exception as e:
                print(f"Failed to move file: {e}")
            # In the event the file type is IMAGE
        else:
            print(f"No matching folder for file typeL {file_ext}")
            
# Watchdog setup for monitoring
event_handler = DownloadsHandler()
observer = Observer()
observer.schedule(event_handler, path=downloads_path, recursive=False)
observer.start()

print(f"Monitoring folder {downloads_path}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()