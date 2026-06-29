# Calculator

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

A professional command-line calculator built with Python. This tool performs basic arithmetic operations with robust input validation and error handling. Designed for clarity and reliability, it offers a clear user experience and can be distributed as a standalone Windows executable.

> **Note:** You can package this calculator as a Windows executable using [PyInstaller](https://www.pyinstaller.org/).

---

## ✨ Features

- Command-line interface for arithmetic calculations
- Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`)
- Validates numeric input and handles invalid entries gracefully
- Robust handling of division by zero
- Displays informative error messages for invalid operations and input

---

## 🛠 Technologies Used

- Python 3.10+ (standard library)
- PyInstaller (for optional executable packaging)

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
    └── calculator.exe   # Standalone Windows executable (generated, optional)
```

---

## 🚀 Installation

Clone the repository:

```sh
git clone https://github.com/Linck-creator/cursor-ai-python-journey.git
cd cursor-ai-python-journey/calculator
```

(Optional) Create and activate a virtual environment:

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

To install development dependencies (for packaging tasks):

```sh
pip install -r requirements.txt
```

> The calculator requires only Python 3.10+ to run. No external libraries are needed.

---

## ▶️ Usage

To run the calculator:

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

This project provides hands-on experience with:

- Command-line input and output
- Control flow using loops and conditionals
- Exception handling with `try`/`except`
- Input validation and type conversion (string to float)
- Structuring a simple Python script

---

## 🔮 Future Improvements

- Add unit and integration tests to ensure reliability
- Implement additional operations (e.g., modulus, exponentiation)
- Refine user prompts and error messages for enhanced usability
- Support command-line arguments for non-interactive (batch) calculations

---

## 👨‍💻 Author

Developed by **Felipe Coelho Linck**  
Administration Student | Python Developer | AI-Assisted Software Development

Created during the **Cursor AI + Python: Intelligent Development with AI** course provided by **Santander Open Academy**.