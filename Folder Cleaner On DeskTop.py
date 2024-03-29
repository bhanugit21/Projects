
import os
import shutil

def Create_subfolder_if_needed(folder_path, subfolder_name):
    """Creates a subfolder in the specified path if it doesn't already exist."""
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def Move_file_to_subfolder(file_path, subfolder_path):
    """Moves a file to the specified subfolder."""
    shutil.move(file_path, subfolder_path)

def Folder_Cleaner(folder_path):
    """Organizes files in the specified folder into subfolders based on file type."""
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:  # Check if file has an extension
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                move_file_to_subfolder(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}/")

print("Clean Floders On Desktop")
folder_path = 'The Folder That You Want To Clean'
if os.path.isdir(folder_path):
    Folder_Cleaner(folder_path)
    print("Cleaning complete.")
else:
    print("Invalid folder path. Please ensure the path is correct and try again.")
