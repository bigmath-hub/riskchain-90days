# Runbook

This file explains how to run this project in a clean way.

## Requirements
- GitHub account
- GitHub Codespace (recommended)
- Python 3.12+

## Setup (Codespace)
1) Open the repo in a Codespace.
2) Check Python and pip:
```bash
python --version
pip --version

# Create venv (one time)
python -m venv .venv
# Active venv (every time you open a new terminal)
source .venv/bin/activate
# Deactivate venv
deactivate

# Install dependencies
pip install requests
pip freeze | head