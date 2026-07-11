"""
File Organizer

This script automatically organizes files in the specified folder ("test") by sorting them
into subfolders based on their file extensions (e.g., Images, Documents, Music, etc.).
It uses only Python standard libraries and leverages pathlib for all file and folder manipulation.

Features:
- Each processed file is logged with a UTC timestamp.
- User-friendly console output and a log file showing actions and status.
- At completion, prints a sorted summary with breakdown by file category, percentage, and elapsed duration.

Author: Felipe Linck

Developed during the "Cursor AI + Python: Intelligent Development with AI" course (Santander Open Academy).
"""

from pathlib import Path
import shutil
from typing import Dict, TextIO, Optional
from datetime import datetime
import time

# ---------------------------- CONFIGURATION -----------------------------
CATEGORIES: Dict[str, list[str]] = {
    "Compressed": [".zip", ".rar", ".7z"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"],
}

FOLDER_NAME: str = "test"             # Folder to organize
LOG_FILE: str = "organization.log"    # Log filename (created inside the target folder)

# ---------------------------- UTILITY FUNCTIONS -------------------------

def get_category(extension: str) -> str:
    """
    Determine the file category for a given extension.

    Args:
        extension (str): The file extension (e.g., ".txt").

    Returns:
        str: The corresponding category, or "Others" if not found.
    """
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def create_folder_if_not_exists(base_path: Path, folder_name: str) -> Path:
    """
    Ensure a subfolder exists within the base directory. Creates the subfolder if needed.

    Args:
        base_path (Path): The parent directory.
        folder_name (str): Name of the category subfolder.

    Returns:
        Path: Path to the category subfolder.
    """
    folder_path = base_path / folder_name
    if not folder_path.exists():
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating folder '{folder_name}': {e}")
    return folder_path


def generate_unique_filename(destination_folder: Path, filename: str) -> Path:
    """
    Generate a unique filename within the destination to prevent overwriting.

    Args:
        destination_folder (Path): Destination directory.
        filename (str): The original filename.

    Returns:
        Path: Path with a unique filename.
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


def move_file(
    file_path: Path,
    destination_folder: Path,
    log_handle: TextIO
) -> Optional[str]:
    """
    Move a file to the destination folder, using a unique filename if necessary.
    Log the action with a UTC timestamp.

    Args:
        file_path (Path): Source file.
        destination_folder (Path): Destination folder.
        log_handle (TextIO): Writable log file handle.

    Returns:
        Optional[str]: Category if the move succeeded, otherwise None.
    """
    try:
        unique_dest = generate_unique_filename(destination_folder, file_path.name)
        shutil.move(str(file_path), str(unique_dest))
        category = destination_folder.name
        time_str = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S UTC")
        msg = f"Moved: {file_path.name} -> {category}"
        print(msg)
        log_handle.write(f"[{time_str}] {msg}\n")
        return category
    except Exception as e:
        time_str = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S UTC")
        msg = f"Failed: {file_path.name}. Reason: {e}"
        print(msg)
        log_handle.write(f"[{time_str}] {msg}\n")
        return None


def generate_report(total_files: int, category_counts: Dict[str, int], duration_seconds: float) -> None:
    """
    Print a summary of the organization, sorted by category, including count and percentage.

    Args:
        total_files (int): Total files processed.
        category_counts (Dict[str, int]): Mapping of category -> number of files.
        duration_seconds (float): Total elapsed time, in seconds.
    """
    print("\n--- Organization Summary ---")
    print(f"Total files processed: {total_files}")
    print(f"Time taken: {duration_seconds:.2f} seconds\n")
    print("Category Breakdown:")
    for category in sorted(category_counts.keys()):
        count = category_counts[category]
        percent = (count / total_files * 100) if total_files > 0 else 0.0
        print(f"  {category:12}: {count} file(s)  ({percent:.1f}%)")
    print("---------------------------")

# ---------------------- MAIN ORGANIZER FUNCTION ------------------------

def organize_folder(folder_name: str) -> None:
    """
    Organize files in the specified folder by category with logging and a summary report.

    Args:
        folder_name (str): The folder to process.
    """
    base_path = Path(folder_name)
    if not base_path.exists() or not base_path.is_dir():
        print(f"Folder '{folder_name}' does not exist or is not a directory.")
        return

    log_file_path = base_path / LOG_FILE
    try:
        log_handle = open(log_file_path, "a", encoding="utf-8")
    except Exception as e:
        print(f"Unable to open log file: {e}")
        return

    now = datetime.now()
    log_handle.write(f"\n=== Organization started at {now.strftime('%Y-%m-%d %H:%M:%S %Z')} ===\n")
    print(f"Log file: {log_file_path}\n")

    start_time = time.perf_counter()

    total_files = 0
    category_counts: Dict[str, int] = {key: 0 for key in list(CATEGORIES.keys()) + ["Others"]}

    # Only process files, skip subfolders and the log itself
    files = [
        f for f in base_path.iterdir()
        if f.is_file() and f.name != LOG_FILE
    ]
    for file_path in files:
        extension = file_path.suffix.lower()
        category = get_category(extension)
        destination_folder = create_folder_if_not_exists(base_path, category)
        result = move_file(file_path, destination_folder, log_handle)
        if result:
            total_files += 1
            category_counts[category] += 1

    duration_seconds = time.perf_counter() - start_time

    # Reporting and log finalization
    generate_report(total_files, category_counts, duration_seconds)
    log_handle.write(
        f"=== Organization finished. {total_files} files processed in {duration_seconds:.2f} seconds ===\n\n"
    )
    log_handle.close()

# ------------------------- PROGRAM ENTRY POINT -------------------------

if __name__ == "__main__":
    print("Starting File Organizer...\n")
    organize_folder(FOLDER_NAME)
    print("\nOrganization complete.")