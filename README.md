# MaibornWolff TicTacToe Game

## Overview

This is a sceleton implementation of a simple command-line implementation of the TicTacToe game. It features a basic UI
for player interaction and supports two players taking turns.

## Prerequisites

- A GitHub Copilot License. If you don't have one, you can request one here within 5
  minutes [here](https://progressbar.maibornwolff.de/esc?id=kb_article&sysparm_article=KB0010197&topic_id=fde03128c3c7fd50977753f0e001310a).
- One of the following IDEs with the GitHub Copilot plugin installed:
    - Visual Studio Code
    - PyCharm
    - IntelliJ IDEA

## Setup Instructions

To run the game on your local machine, follow the instructions below.

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.

### For Windows

1. **Download and Install Python**:
    - Visit [Python's official website](https://www.python.org/downloads/) and download the latest version of Python for
      Windows.
    - Run the installer and follow the setup instructions. Make sure to check the "Add Python to PATH" option.

2. **Set Up Virtual Environment**:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```

### For macOS

1. **Install Python using Homebrew (if not already installed)**:
    - First, install [Homebrew](https://brew.sh/) if you haven't already:
      ```sh
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
    - Then, install Python:
      ```sh
      brew install python
      ```

2. **Set Up Virtual Environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

## Running the Application

1. **Install Required Packages**:
    - Navigate to the project directory in your terminal.
    - Activate the virtual environment if not active:
      ```sh
      # On Windows
      .\venv\Scripts\activate
      
      # On macOS
      source venv/bin/activate
      ```

2. **Run the Game**:
    ```sh
    python game.py
    ```

You can exit the game with Ctrl + C.

## Running the Tests

1. **Ensure the virtual environment is activated**:
    ```sh
    # On Windows
    venv\Scripts\activate

    # On macOS
    source venv/bin/activate
    ```

2. **Run Tests with `unittest`**:
    ```sh
    python -m unittest discover
    ```

Alternative: You can install ``pytest`` via `pip install pytest` and then run the tests via `pytest game_test.py`.
