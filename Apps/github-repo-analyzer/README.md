# GitHub Repo Analyzer

A lightweight, dependency-free command-line tool that fetches and analyzes public GitHub repositories using the GitHub REST API. It provides a quick overview of repository metrics, language distribution, and recent commit history directly in the terminal.

## Features

- **General Statistics:** Retrieves core repository data including star count, forks, watchers, open issues, and lifecycle dates.
- **Language Breakdown:** Calculates and displays the percentage and exact byte count of programming languages used in the repository.
- **Commit History:** Fetches the 10 most recent commits, displaying the date, author, and primary commit message.
- **Flexible Input Parsing:** Accepts both full URLs (`https://github.com/psf/requests`) and shorthand formats (`psf/requests`).
- **Resilient Error Handling:** Includes dedicated `try/except` blocks to manage invalid inputs, 404/403 HTTP errors, and network connectivity issues.

## Technical Highlights

This project was built with a focus on native Python capabilities without relying on third-party packages like `requests`. Key implementations include:

- **Standard Library Networking:** Utilizing `urllib.request` for executing HTTP REST requests.
- **Data Parsing:** Processing complex JSON responses natively with `json.loads()`.
- **Advanced Terminal Formatting:** Using f-string alignment specifiers (`:<20`, `:>6`) to create clean, tabular CLI outputs.
- **Data Sorting:** Implementing `lambda` functions alongside `sorted()` to accurately rank tuple data.
- **String Manipulation:** Slicing ISO 8601 formatted datetime strings to extract clean date formats.

## Usage

Ensure you have Python 3.x installed. Navigate to the directory containing the application and run the script:

```bash
python main.py