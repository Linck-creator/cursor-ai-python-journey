# Python Learning Project

A hands-on Python project focused on mastering essential programming concepts and practical development tools. This repository contains beginner-friendly scripts and exercises designed to develop problem-solving skills, file operations, data analysis, testing, and code quality practices in Python.

---

## 📖 Project Overview

This project was developed as part of a Python learning journey using Cursor AI. It includes practical exercises covering arithmetic operations, control flow, file processing, automated testing, code formatting, static analysis, and basic data analysis.

The objective is to build a solid foundation in Python while becoming familiar with modern development tools and workflows.

---

## ✨ Features

- Console-based Python scripts with clear and documented code
- Basic calculator for arithmetic operations
- FizzBuzz implementation
- Text file word counter using Python collections
- CSV data analysis with pandas
- Statistical calculations (mean, median, and standard deviation)
- Scatter plot generation with matplotlib
- Examples of loops, conditionals, and exception handling
- Automated testing with pytest
- Code formatting with Black
- Static code analysis with Pylint
- Git and GitHub integration

---

## 🛠 Requirements

- Python 3.10+
- pandas
- matplotlib
- pytest
- black
- pylint

Install all dependencies using:

```sh
pip install -r requirements.txt

```

---

## 🚀 Installation

1. Clone the repository:

```sh
git clone https://github.com/Linck-creator/Curso_Santander_Open.git
cd Curso_Santander_Open

```

1. Verify your Python installation:

```sh
python --version

```

1. (Optional) Create and activate a virtual environment:

```sh
python -m venv venv

```

Windows PowerShell:

```sh
.\venv\Scripts\Activate.ps1

```

1. Install dependencies:

```sh
pip install -r requirements.txt

```

---

## 📦 Distribution

The calculator application can be packaged as a standalone Windows executable using PyInstaller.

### Install PyInstaller

```sh
pip install pyinstaller

```

### Generate the executable

```sh
pyinstaller --onefile calculator.py

```

### Executable Location

After the build process is completed, the executable will be available at:

```text
dist/calculator.exe

```

### Benefits

- No Python installation required for end users
- Single executable file for easy sharing
- Simplified deployment on Windows systems
- Convenient testing on different computers

---

## ⚡ Usage Examples

Run the scripts from the project directory.

### Calculator (`calculator.py`)

Performs basic arithmetic operations with input validation and division-by-zero protection.

```sh
python calculator.py

```

### FizzBuzz (`fizzbuzz.py`)

Prints numbers from 1 to 50 following the FizzBuzz rules.

```sh
python fizzbuzz.py

```

### Word Counter (`counter.py`)

Counts the frequency of words in a text file.

```sh
python counter.py

```

### Data Analysis (`parse.py`)

Reads a CSV file, calculates statistical measures, and generates a scatter plot using pandas and matplotlib.

```sh
python parse.py

```

---

## 🧪 Testing

Run all automated tests:

```sh
pytest

```

---

## 🧹 Code Formatting

Format the project using Black:

```sh
black .

```

---

## 📝 Linting

Analyze code quality using Pylint:

```sh
pylint calculator.py fizzbuzz.py counter.py parse.py

```

---

## 📂 Project Structure

```text
Curso_Santander_Open/
│
├── calculator.py
├── fizzbuzz.py
├── counter.py
├── test_counter.py
├── parse.py
├── data.csv
├── requirements.txt
├── README.md
├── build/
└── dist/

```

---

## 👤 Author

Created by **Felipe Linck** during a Python learning journey using Cursor AI, Git, GitHub, and modern development practices.

---

Happy learning and coding! 🚀