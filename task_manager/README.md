# Task Manager

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A modern task management web application built with Flask. This project enables users to create, complete, and delete tasks while tracking progress through a responsive web interface. Tasks are stored locally in a JSON file, providing a simple persistence layer without requiring a database.

---

## ✨ Features

- Create new tasks
- Mark tasks as completed
- Delete tasks
- Store tasks using JSON persistence
- Dashboard statistics
- Progress tracking
- Task priority levels
- Task creation date
- Responsive web interface

---

## 🛠 Technologies Used

- Python 3.10+
- Flask
- HTML5
- CSS3
- JSON

---

## 📂 Project Structure

```text
task_manager/
│
├── app.py                 # Flask application
├── tarefas.json           # Local task storage
├── templates/
│   └── index.html         # Main application template
├── static/
│   └── style.css          # Application stylesheet
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
└── .gitignore             # Git ignore rules
```

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/Linck-creator/cursor-ai-python-journey.git
```

2. Change to the project directory:

```bash
cd cursor-ai-python-journey/task_manager
```

3. (Optional) Create and activate a virtual environment:

<details>
<summary>Windows (PowerShell)</summary>

```powershell
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

4. Install dependencies:

```bash
pip install -r requirements.txt
```

> This project requires **Flask**. Install the dependency using the provided `requirements.txt` file before running the application.

---

## ▶️ Usage

Start the application with:

```bash
python app.py
```

- The application will start a local Flask server.
- Open your browser to access the web interface.
- Manage your tasks: create, complete, or delete items.
- All tasks are stored locally in `tarefas.json`.
- Dashboard statistics and progress update automatically.

---

## 📸 Preview

> Screenshots will be added in a future update.

---

## 📚 Learning Objectives

- Flask fundamentals
- Routing
- HTML templates
- Forms
- JSON data persistence
- CRUD operations
- Responsive interface development
- CSS styling
- Backend and frontend integration

---

## 🔮 Future Improvements

- SQLite database support
- User authentication
- Task editing
- Due dates
- Categories
- Search and filtering
- REST API
- Docker support

---

## 👨‍💻 Author

Developed by **Felipe Coelho Linck**

Administration Student | Python Developer | AI-Assisted Software Development

Created during the **Cursor AI + Python: Intelligent Development with AI** course provided by **Santander Open Academy**.