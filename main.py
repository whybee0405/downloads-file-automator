import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import shutil

DOCUMENT_EXTENSIONS = ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx']
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.svg', '.ico']
VIDEO_EXTENSIONS = ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.3gp']
ARCHIVE_EXTENSIONS = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.cab']
INSTALLER_EXTENSIONS = ['.exe', '.msi', '.deb', '.rpm', '.apk', '.dmg', '.pkg']
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.wma', '.m4a', '.aiff', '.alac']

# Listen for any new downloads
class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            if event.src_path.endswith(".part"):
                return

            # Wait to make sure file write is complete
            time.sleep(2)
            print(f"New file detected: {event.src_path}")
        
            # Determine the type of file using the extension
            download_file_type = os.path.splitext(event.src_path)[1].lower()
            print(f"file type is {download_file_type}")
            
            # In the event the file type is DOCUMENT
            if download_file_type in DOCUMENT_EXTENSIONS:
                filename = os.path.basename(event.src_path)
                dest_folder = os.path.join(downloads_path, "DOWNLOADS - Documents")
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)
                                         
                try:
                    shutil.move(event.src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}")
                except Exception as e:
                    print(f"Failed to move file: {e}")
            # In the event the file type is IMAGE
            elif download_file_type in IMAGE_EXTENSIONS:
                filename = os.path.basename(event.src_path)
                dest_folder = os.path.join(downloads_path, "DOWNLOADS - Images")
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)
                                         
                try:
                    shutil.move(event.src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}")
                except Exception as e:
                    print(f"Failed to move file: {e}")
            # In the event the file type is VIDEO   
            elif download_file_type in VIDEO_EXTENSIONS:
                filename = os.path.basename(event.src_path)
                dest_folder = os.path.join(downloads_path, "DOWNLOADS - Videos")
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)    
                                         
                try:
                    shutil.move(event.src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}")
                except Exception as e:
                    print(f"Failed to move file: {e}")  
            # In the event the file type is ARCHIVE              
            elif download_file_type in ARCHIVE_EXTENSIONS:
                filename = os.path.basename(event.src_path)
                dest_folder = os.path.join(downloads_path, "DOWNLOADS - Archives")
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)  
                                         
                try:
                    shutil.move(event.src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}")
                except Exception as e:
                    print(f"Failed to move file: {e}")     
            # In the event the file type is INSTALLER   
            elif download_file_type in INSTALLER_EXTENSIONS:
                filename = os.path.basename(event.src_path)
                dest_folder = os.path.join(downloads_path, "DOWNLOADS - Installer")
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)   
                                         
                try:
                    shutil.move(event.src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}")
                except Exception as e:
                    print(f"Failed to move file: {e}")   
            # In the event the file type is AUDIO              
            elif download_file_type in ARCHIVE_EXTENSIONS:
                filename = os.path.basename(event.src_path)
                dest_folder = os.path.join(downloads_path, "DOWNLOADS - Audio")
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename) 
                         
                try:
                    shutil.move(event.src_path, dest_path)
                    print(f"Moved {filename} to {dest_folder}")
                except Exception as e:
                    print(f"Failed to move file: {e}")
            
                    
# Define path to Downloads directory agnostically
downloads_path = os.path.expanduser("~/Downloads")
# downloads_files = os.listdir(downloads_path) #list of all files within the Downloads directory

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