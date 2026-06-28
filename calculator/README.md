# Calculator

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

An interactive command-line calculator implemented in Python. Perform basic arithmetic operations with input validation and user-friendly error handling.

> **Note:** A standalone Windows executable can be generated using [PyInstaller](https://www.pyinstaller.org/).

---

## ✨ Features

- Interactive console interface for arithmetic calculations
- Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`)
- Validates numeric input and handles invalid entries gracefully
- Robust handling of division by zero
- Informative error messages for invalid operations and input

---

## 🛠 Technologies Used

- Python 3.10+ (standard library)
- PyInstaller (for packaging executable)

---

## 📂 Project Structure

```text
calculator/
│
├── calculator.py        # Main calculator script
├── calculator.spec      # PyInstaller build specification
├── README.md            # Project documentation
├── requirements.txt     # Development dependencies (for optional tasks)
└── release/
    └── calculator.exe   # Standalone Windows executable (optional, generated)
```

---

## 🚀 Installation

Clone the repository:

```sh
git clone https://github.com/Linck-creator/cursor-ai-python-journey.git
cd cursor-ai-python-journey/calculator
```

(Optional, recommended) Create and activate a virtual environment:

<details>
  <summary>Windows (PowerShell)</summary>

  ```sh
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
</details>

<details>
  <summary>Unix / macOS</summary>

  ```sh
  python -m venv venv
  source venv/bin/activate
  ```
</details>

To install development dependencies (if you intend to run tests or maintain the project):

```sh
pip install -r requirements.txt
```

> The calculator requires only Python 3.10+ to run. No external libraries are needed for calculator functionality.

---

## ▶️ Usage

Run the calculator from the `calculator` directory:

```sh
python calculator.py
```

**Instructions:**
- Enter one of `+`, `-`, `*`, or `/` to select an operation.
- Enter two numbers when prompted.
- Type `exit` as the operation to quit the program.

**Example session:**
```
Enter an operation (+, -, *, /) or 'exit' to quit: *
Enter the first number: 6
Enter the second number: 7
42.0

Enter an operation (+, -, *, /) or 'exit' to quit: /
Enter the first number: 10
Enter the second number: 0
Error: Division by zero is not allowed.
```

---

## 📸 Preview

> Screenshots will be added in a future update.

---

## 📚 Learning Objectives

This project provides practical experience with:

- Command-line input and output
- Control flow using loops and conditional statements
- Exception handling with `try`/`except`
- Input validation and type conversion (string to float)
- Structuring a simple Python project

---

## 🔮 Future Improvements

- Implement unit and integration tests for improved reliability
- Add additional operations (e.g., modulus, exponentiation)
- Enhance user prompts and error messaging for improved usability
- Support command-line arguments for scriptable batch calculations

---

## 👨‍💻 Author

Developed by **Felipe Coelho Linck**  
Administration Student | Python Developer | AI-Assisted Software Development

Created during the **Cursor AI + Python: Intelligent Development with AI** course provided by **Santander Open Academy**.