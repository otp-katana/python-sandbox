# Python Sandbox

A modular and structured repository containing a collection of Python-based command-line applications, interactive mini-games, and utility scripts. This repository is designed with a scalable architecture to maintain separation of concerns and ensure clean, isolated development environments.

## Table of Contents

- [Architecture](#architecture)
- [Projects Overview](#projects-overview)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Adding a New Project](#adding-a-new-project)
- [License](#license)

## Architecture

The repository utilizes a categorized monorepo structure. Each category serves a specific purpose, preventing clutter in the root directory.

```text
python-sandbox/
├── apps/                 # Data-processing and comprehensive CLI applications
├── games/                # Interactive terminal-based mini-games
├── tools/                # Single-purpose utility scripts
├── .github/              # GitHub Actions workflows and configuration (optional)
├── .gitattributes        # Git configuration for line endings and language parsing
├── .gitignore            # Ignored files and directories (e.g., __pycache__, .venv)
├── requirements.txt      # Global project dependencies
└── README.md             # Main repository documentation