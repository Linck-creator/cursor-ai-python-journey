# Python Learning Project

A hands-on Python project focused on mastering essential programming concepts and practical development tools. This repository is a collection of beginner-friendly scripts and exercises to guide learners in developing problem-solving skills, file operations, and code quality practices in Python.

---

## 📖 Project Overview

This project provides interactive Python scripts and mini projects that cover key topics such as arithmetic processing, control flow, file manipulation, and data analysis. It also introduces common software development workflows including testing, code formatting, and linting.

---

## ✨ Features

- Console-based Python scripts with clear, documented code
- Basic calculator for arithmetic operations
- FizzBuzz logic implementation
- Text file word counter for analysis
- CSV data analysis: mean, median, standard deviation, and scatter plots
- Structured examples to practice for loops and conditionals
- Test suite with **pytest**
- Automated code formatting with **Black**
- Code style checking with **Pylint**

---

## 🛠 Requirements

- **Python 3.10+**
- [pytest](https://pytest.org/) (for testing)
- [black](https://black.readthedocs.io/) (for formatting)
- [pylint](https://pylint.pycqa.org/) (for linting)

Install development dependencies with:

```sh
pip install -r requirements.txt
```

*Or install tools individually:*

```sh
pip install pytest black pylint
```

---

## 🚀 Installation

1. **Clone this repository:**

   ```sh
   git clone https://github.com/Linck-creator/Curso_Santander_Open.git
   cd Curso_Santander_Open
   ```

2. **Ensure Python 3.10 or newer is installed:**

   ```sh
   python --version
   ```

---

## ⚡️ Usage Examples

Run scripts from the project directory using your terminal:

### Calculator Script (`calculator.py`)

Performs basic arithmetic operations (+, -, *, /).

```sh
python calculator.py
```
or
```sh
python3 calculator.py
```

### FizzBuzz Script (`fizzbuzz.py`)

Prints the FizzBuzz sequence up to a specified number.

```sh
python fizzbuzz.py
```
or
```sh
python3 fizzbuzz.py
```

### Word Counter Script (`counter.py`)

Counts words in a given text file.

```sh
python counter.py sample.txt
```

### Data Analysis Script (`parse.py`)

Reads a CSV file, calculates mean, median, and standard deviation, and generates a scatter plot using pandas and matplotlib.

```sh
python parse.py data.csv
```

---

## 🧪 Testing

Run all tests using pytest for script validation:

```sh
pytest
```

---

## 🧹 Code Formatting

Ensure consistent code style by auto-formatting with Black:

```sh
black .
```

---

## 📝 Linting

Check scripts for style and error-prone code using Pylint:

```sh
pylint calculator.py fizzbuzz.py counter.py parse.py
```

---

## 👤 Author

Created by Felipe Linck during a Python learning journey with inspiration from the Cursor AI platform.

---

Happy learning!