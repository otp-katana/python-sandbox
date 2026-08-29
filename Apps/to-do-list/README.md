# To-Do List Application

A robust, interactive command-line application for task management. This tool allows users to add, delete, complete, and list tasks with persistent data storage.

## Features

- **Interactive Menu:** A user-friendly, loop-driven terminal menu for easy navigation[cite: 3].
- **Persistent Storage:** Tasks are automatically saved to and loaded from a local JSON file (`gorevler.json`), ensuring data is not lost between sessions[cite: 3].
- **Task Management:** Full Create, Read, Update, and Delete (CRUD) capabilities:
  - Add new tasks with unique IDs[cite: 3].
  - Mark tasks as completed (indicated by a `[✓]`)[cite: 3].
  - Delete tasks securely[cite: 3].
  - View a formatted list of all tasks, including a summary of total, completed, and pending tasks[cite: 3].
- **Input Validation:** Includes robust `try/except` error handling to ensure user inputs (like Task IDs) are valid integers, preventing application crashes[cite: 3].
- **Standard Library Only:** Built using only Python's built-in `json` and `os` modules[cite: 3]. No external dependencies are required.

## Usage

Navigate to the directory containing the application and run the script using Python:

```bash
python main.py