# File Organizer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A professional file automation script that automatically organizes files into categorized folders by extension, using only Python standard libraries.

---

## ✨ Features

- Automatically organize files into categorized folders
- Categorize files by extension
- Automatically create category folders
- Prevent filename collisions
- Generate organization logs
- Display organization summary
- Calculate category percentages
- Measure execution time

---

## 🛠 Technologies Used

- Python 3.10+
- Python Standard Library
  - pathlib
  - shutil
  - datetime
  - time
  - typing

---

## 📂 Project Structure

```text
file_organizer/
│
├── organize.py
├── test/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/Linck-creator/cursor-ai-python-journey.git
cd cursor-ai-python-journey/file_organizer
```

2. (Optional) Create and activate a virtual environment.

<details>
  <summary>Windows (PowerShell)</summary>

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

</details>

<details>
  <summary>Unix / macOS</summary>

```bash
python -m venv venv
source venv/bin/activate
```

</details>

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

> This project uses only the Python Standard Library. No external packages are required at runtime.

---

## ▶️ Usage

To organize the contents of the **test/** folder, run:

```bash
python organize.py
```

The script will automatically sort all files in the `test/` folder into categorized subfolders according to their extensions.

---

## 📸 Preview

> Screenshots will be added in a future update.

---

## 📚 Learning Objectives

- File system automation
- Working with pathlib
- File handling
- Directory management
- Logging
- Exception handling
- Performance measurement
- Modular programming

---

## 🔮 Future Improvements

- Recursive directory support
- User-selected folders
- Configuration file
- Drag-and-drop support
- Progress bar
- Undo operation
- Command-line argument support

---

## 👨‍💻 Author

Developed by **Felipe Coelho Linck**

Administration Student | Python Developer | AI-Assisted Software Development

Created during the **Cursor AI + Python: Intelligent Development with AI** course provided by **Santander Open Academy**.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━