"""
File Organizer Tool

This module automatically organizes files in a directory
by categorizing them into folders based on file type.

Author: MD Shan
Date: June 2026
Version: 1.0.0
"""

import os
import shutil
from pathlib import Path

# File categories mapping
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'],
    'Documents': ['.pdf', '.docx', '.xlsx', '.txt', '.pptx', '.doc'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.wma']
}

def get_file_category(file_extension):
    """
    Determine the category of a file based on its extension.
    
    Args:
        file_extension (str): File extension (e.g., '.jpg')
    
    Returns:
        str: Category name or 'Other' if not found
    """
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Other'


def organize_files(folder_path):
    """
    Organize all files in the given folder into category subfolders.
    
    Args:
        folder_path (str): Path to the folder to organize
    
    Returns:
        dict: Summary with count of organized files
    
    Raises:
        FileNotFoundError: If folder doesn't exist
        PermissionError: If insufficient permissions
    """
    try:
        # Validate folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder '{folder_path}' not found")
        
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"'{folder_path}' is not a directory")
        
        organized_count = 0
        
        # Scan all files in folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Skip if it's a directory
            if os.path.isdir(file_path):
                continue
            
            # Get file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Get category for this file
            category = get_file_category(file_extension)
            
            # Create category folder if not exists
            category_folder = os.path.join(folder_path, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
                print(f"✓ Created folder: {category}/")
            
            # Move file to category folder
            try:
                destination = os.path.join(category_folder, filename)
                shutil.move(file_path, destination)
                print(f"✓ Moved {filename} → {category}/")
                organized_count += 1
            
            except PermissionError:
                print(f"✗ Permission denied: {filename}")
            except Exception as e:
                print(f"✗ Error moving {filename}: {str(e)}")
        
        return {
            'success': True,
            'organized_files': organized_count,
            'folder': folder_path
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }


def main():
    """Main function to run the file organizer."""
    print("=" * 50)
    print("  FILE ORGANIZER TOOL")
    print("=" * 50)
    
    # Get folder path from user
    folder_path = input("\nEnter the folder path to organize: ").strip()
    
    if not folder_path:
        print("Error: Please provide a valid folder path")
        return
    
    # Expand home directory if used
    folder_path = os.path.expanduser(folder_path)
    
    print(f"\nOrganizing files in: {folder_path}\n")
    
    # Organize files
    result = organize_files(folder_path)
    
    # Display result
    if result['success']:
        print(f"\n✓ Success! Organized {result['organized_files']} files")
    else:
        print(f"\n✗ Failed: {result.get('error', 'Unknown error')}")
    
    print("=" * 50)


if __name__ == "__main__":
    main()
