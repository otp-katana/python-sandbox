# 🧮 Simple Calculator (Python)

A robust, terminal-based simple calculator application developed in Python. It provides a structured, user-friendly interface to perform fundamental mathematical operations within a continuous execution loop, prioritizing error prevention and UI clarity.

## 🚀 Features

* **Core Operations:** Supports addition (➕), subtraction (➖), multiplication (✖️), and division (➗).
* **Smart Division Handling:** Automatically prevents `division by zero` errors, displaying a custom warning prompt instead of crashing the program. 
* **Dynamic Type Formatting:** Dynamically formats division results; outputs as integers (`int`) if the numbers divide evenly (no remainder), or as decimals (`float`) when a remainder exists.
* **Custom Terminal UI:** Utilizes Unicode characters to draw a structured, easy-to-navigate menu interface that feels like a native dashboard.
* **Color-Coded Feedback:** Employs ANSI escape codes to highlight critical errors and key interactions with colored (`\033[31m`) and underlined (`\033[4m`) text.
* **Paced User Experience:** Leverages the `time.sleep()` module to introduce deliberate delays. Combined with required `input()` keystrokes, this prevents the terminal from endlessly scrolling and keeps the user in full control of the reading pace.

## 🛠️ Usage

1. Ensure you have Python installed on your system.
2. Clone the repository:
   ```bash
   git clone [https://github.com/your_username/your_project_name.git](https://github.com/your_username/your_project_name.git)