"""
File Organizer

This script automatically organizes files in a specified folder ("test") by sorting them
into subfolders based on their file extensions/categories (Images, Documents, etc.).
It uses only standard Python libraries, and all logic uses pathlib where possible.

Each file processed is logged, user-friendly terminal output is displayed,
and a summary is printed at the end.

Author: Felipe Linck
"""

from pathlib import Path
import shutil
import sys

# ----------------------- CONFIGURATION SECTION -----------------------
# Mapping of file extensions to categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Compressed": [".zip", ".rar", ".7z"],
}
FOLDER_NAME = "test"  # Folder to organize
LOG_FILE = "organization.log"

# ----------------------- UTILITY FUNCTIONS -----------------------

def get_category(extension):
    """
    Identifies the category for a given file extension.
    Returns the category name or 'Others' for uncategorized extensions.
    """
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def create_folder_if_not_exists(base_path, folder_name):
    """
    Creates a folder with folder_name inside base_path if it does not exist.
    Returns the full path to the folder.
    """
    folder_path = base_path / folder_name
    if not folder_path.exists():
        try:
            folder_path.mkdir()
        except Exception as e:
            print(f"Error creating folder {folder_name}: {e}")
    return folder_path

def generate_unique_filename(destination_folder, filename):
    """
    Prevents overwriting files with the same name by appending a counter if necessary.
    Returns a Path object for the unique filename.
    """
    destination = destination_folder / filename
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    counter = 1
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        destination = destination_folder / new_name
        if not destination.exists():
            break
        counter += 1
    return destination

def move_file(file_path, destination_folder, log_handle):
    """
    Moves the specified file to the destination folder, renaming if necessary
    to prevent overwriting. Logs the movement.
    Returns (final_path, category).
    """
    try:
        unique_dest = generate_unique_filename(destination_folder, file_path.name)
        shutil.move(str(file_path), str(unique_dest))
        category = destination_folder.name
        msg = f"Moved: {file_path.name} -> {category}"
        print(msg)
        log_handle.write(msg + "\n")
        return category
    except Exception as e:
        msg = f"Failed: {file_path.name}. Reason: {e}"
        print(msg)
        log_handle.write(msg + "\n")
        return None

def generate_report(total_files, category_counts):
    """
    Prints a summary report of the file organization.
    """
    print("\n--- Organization Summary ---")
    print(f"Total files processed: {total_files}")
    for category, count in category_counts.items():
        print(f"{category}: {count} file(s)")
    print("---------------------------")

# ----------------------- MAIN ORGANIZER FUNCTION -----------------------

def organize_folder(folder_name):
    """
    Orchestrates scanning, categorization, and moving of files, and outputs reports.
    """
    base_path = Path(folder_name)
    if not base_path.exists() or not base_path.is_dir():
        print(f"Folder '{folder_name}' does not exist or is not a directory.")
        return

    # Prepare logging
    log_file_path = base_path / LOG_FILE
    try:
        log_handle = open(log_file_path, "a", encoding="utf-8")
    except Exception as e:
        print(f"Unable to open log file: {e}")
        return

    # File counters
    total_files = 0
    category_counts = {}
    for category in list(CATEGORIES.keys()) + ["Others"]:
        category_counts[category] = 0

    # Iterate files (ignore directories)
    files = [f for f in base_path.iterdir() if f.is_file() and f.name != LOG_FILE]
    for file_path in files:
        extension = file_path.suffix.lower()
        category = get_category(extension)
        destination_folder = create_folder_if_not_exists(base_path, category)
        result = move_file(file_path, destination_folder, log_handle)
        if result:
            total_files += 1
            category_counts[category] += 1

    # Reporting and cleanup
    generate_report(total_files, category_counts)
    log_handle.close()


# ----------------------- EXECUTION ENTRY POINT -----------------------

if __name__ == "__main__":
    print("Starting File Organizer...\n")
    organize_folder(FOLDER_NAME)
    print("\nOrganization complete.")