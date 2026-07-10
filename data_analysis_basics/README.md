# Data Analysis Basics [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

This project demonstrates basic exploratory data analysis of a CSV dataset using Python. It reads the data, computes descriptive statistics (mean, median, standard deviation) for each column, displays the results in the terminal, and creates a scatter plot comparing Sales and Profit.

---

## ✨ Features

- Reads a CSV file into a Pandas DataFrame
- Calculates and prints mean, median, and standard deviation for each column
- Displays computed statistics in the terminal
- Generates a scatter plot of Sales vs Profit

---

## 🛠 Technologies Used

- Python
- pandas
- matplotlib

---

## 📂 Project Structure

```text
data_analysis_basics/
│
├── parse.py         # Main analysis and visualization script
├── data.csv         # Example CSV dataset (sales, profit)
├── README.md        # Project documentation
├── requirements.txt # Python dependencies
└── .gitignore       # Version control ignore rules
```

---

## 🚀 Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/Linck-creator/cursor-ai-python-journey.git
   cd cursor-ai-python-journey/data_analysis_basics
   ```

2. **(Optional) Create a virtual environment:**
   ```
   python -m venv venv
   # On Unix/MacOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

To run the analysis and visualization:

```
python parse.py
```

The script automatically loads the provided dataset, computes and displays statistics in the terminal, and opens a scatter plot window.

---

## 📸 Preview

> Screenshots will be added in a future update.

---

## 📚 Learning Objectives

- Reading CSV files with pandas
- Working with DataFrames for statistical analysis
- Calculating basic descriptive statistics
- Visualizing data with matplotlib (scatter plots)

---

## 🔮 Future Improvements

- Support for custom user-uploaded CSV files
- Option to export computed statistics to CSV or Excel
- Enhanced customization for visualizations

---

## 👨‍💻 Author

Developed by **Felipe Coelho Linck**

Administration Student | Python Developer | AI-Assisted Software Development

Created during the **Cursor AI + Python: Intelligent Development with AI** course provided by **Santander Open Academy**.