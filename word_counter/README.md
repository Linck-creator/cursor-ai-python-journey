# Word Counter

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A Python utility for command-line analysis of text files. It reads a specified file, extracts all words (case-insensitive), counts the total number of words, and reports the 10 most frequent words. The project demonstrates file handling, regular expressions, word frequency analysis, exception handling, and basic unit testing using object-oriented design.

## ✨ Features

- Count the total number of words in a text file  
- Display the 10 most frequent words along with their counts  
- User-friendly CLI for reading and analyzing text files  
- Gracefully handles missing text files using exception handling

## 🛠 Technologies Used

- Python 3.10+
- Python Standard Library
  - collections
  - collections.abc
  - re
  - typing

## 📂 Project Structure

```
word_counter/
├── counter.py       # Main script: counts words and finds most common terms via CLI
├── test_counter.py  # WordCounter class and its unit tests
├── sample.txt       # Example text file for testing the script
├── .gitignore       # Standard ignores for Python development and editors
├── README.md        # Project overview and instructions
└── requirements.txt # Project dependencies
```

- **counter.py**: Command-line application that reads a text file, normalizes case, counts words, and prints the total and top 10 most frequent word counts using `collections.Counter`.
- **test_counter.py**: Implements the reusable `WordCounter` class and includes unit tests with simple `assert` statements to validate core logic.
- **sample.txt**: Example text file included for experimentation or demonstration.
- **.gitignore**: Lists files and directories to be ignored by Git.
- **README.md**: Project overview and instructions.
- **requirements.txt**: Defines the project dependencies.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Linck-creator/cursor-ai-python-journey.git
   cd cursor-ai-python-journey/word_counter
   ```
2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install project dependencies (optional):
   ```bash
   pip install -r requirements.txt
   ```

   > This project uses only the Python Standard Library. No external packages are required at runtime.

## ▶️ Usage

1. Run the word counter script:
   ```bash
   python counter.py
   ```
2. Enter the path to your text file when prompted.

**Example:**
```
Enter the path of the text file:
sample.txt
Total words:
...

10 most frequent words:
...
```

## 📸 Preview

> Screenshots will be added in a future update.

## 📚 Learning Objectives

- Reading and processing text files
- File I/O
- Regular expressions
- `collections.Counter`
- Exception handling
- Object-Oriented Programming
- Basic unit testing

## 🔮 Future Improvements

- Add command-line arguments for input files and settings
- Include character and line counting functionality
- Enhance text preprocessing (e.g., ignoring punctuation or stop words)
- Integrate more robust automated testing (e.g., with `pytest`)

## 👨‍💻 Author

Developed by **Felipe Coelho Linck**  
Administration Student | Python Developer | AI-Assisted Software Development

Created during the **Cursor AI + Python: Intelligent Development with AI** course provided by **Santander Open Academy**