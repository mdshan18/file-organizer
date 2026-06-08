import os
import shutil

folder_path = input("Folder path daalo: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives" :[".zip", ".rar"]
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                target_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(
                    file_path,
                    os.path.join(target_folder, file)
                )

                print(f"{file} moved to {folder_name}")