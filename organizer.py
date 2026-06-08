import os
import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".java"]
}


def organize_files():

    folder_path = input(
        "Folder path daalo: "
    )

    for file in os.listdir(folder_path):

        file_path = os.path.join(
            folder_path,
            file
        )

        if os.path.isfile(file_path):

            extension = os.path.splitext(
                file
            )[1].lower()

            for folder_name, extensions in file_types.items():

                if extension in extensions:

                    target_folder = os.path.join(
                        folder_path,
                        folder_name
                    )

                    if not os.path.exists(
                        target_folder
                    ):
                        os.makedirs(
                            target_folder
                        )

                    shutil.move(
                        file_path,
                        os.path.join(
                            target_folder,
                            file
                        )
                    )

                    print(
                        f"{file} moved to {folder_name}"
                    )


def show_categories():

    print("\nAvailable Categories:")

    for category, extensions in file_types.items():

        print(
            f"{category} → {extensions}"
        )


def add_file_type():

    category = input(
        "Enter category name: "
    )

    extension = input(
        "Enter extension (with dot): "
    )

    extension = extension.lower()

    if category in file_types:

        if extension not in file_types[category]:

            file_types[category].append(
                extension
            )

            print(
                f"{extension} added to {category}"
            )

        else:

            print(
                "Extension already exists."
            )

    else:

        file_types[category] = [extension]

        print(
            f"New category '{category}' created with {extension}"
        )


while True:

    print("\n===== File Organizer =====")
    print("1. Organize Files")
    print("2. Show Categories")
    print("3. Add New File Type")
    print("4. Exit")

    choice = input(
        "Enter your choice: "
    )

    if choice == "1":

        organize_files()

    elif choice == "2":

        show_categories()

    elif choice == "3":

        add_file_type()

    elif choice == "4":

        print(
            "Exiting program..."
        )

        break

    else:

        print(
            "Invalid choice, try again."
        )