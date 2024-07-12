# GitHub Copilot Workshop Runbook

## Overview

Welcome to the GitHub Copilot workshop! In this session, you will learn how to leverage GitHub Copilot to assist in developing a test-driven TicTacToe game. By the end of this workshop, you should be comfortable using Copilot to generate code, refactor functions, and write tests.

The repository is pre-populated with the basic files you need (`game.py`, `game_test.py`, `README.md`).

## Prerequisites

- GitHub Copilot license.
- One of the following IDEs with the GitHub Copilot plugin installed:
    - Visual Studio Code
    - PyCharm
    - IntelliJ IDEA

Make sure you have followed the setup instructions in the `README.md` file to ensure your development environment is ready.

## Getting Started

### Step 1: Open the Project in Your IDE

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Open the Project**:
    - Open the project directory in your preferred IDE (Visual Studio Code, PyCharm, or IntelliJ IDEA).

3. **Set Up Virtual Environment**:
    - Follow the instructions in the `README.md` to set up and activate the virtual environment.

### Step 2: Enable GitHub Copilot

1. **Ensure GitHub Copilot Plugin is Installed**:
    - Check that the GitHub Copilot plugin is installed in your IDE.
    - You should see the Copilot icon on the bottom right of your IDE status bar.

2. **Sign In to GitHub Copilot**:
    - Sign in with your GitHub account that has Copilot access.

### Step 3: Understanding the existing project structure

1. **Project Files**:
    - `game.py`: Contains the `TicTacToe` class with methods for initializing the game, making a move, and checking for a winner.
    - `game_test.py`: Contains test cases for the `TicTacToe` class methods.

2. **Running the Game**:
    - Run the game using the command (ensure the virtual environment is activated):
        ```sh
        python game.py
        ```
    - Try to play the game, and observe if board updates correctly.
    - Unfortunately, the game is not fully functional yet. It will be your task to implement the missing features!

3. **Running Tests**:
    - Run the tests using the command:
        ```sh
        python -m unittest discover
        ```
    - Observe that some tests are failing. Your goal is to implement the missing functionality and make all tests pass.

## Using GitHub Copilot

### Step 4: Getting Your First Autocomplete Suggestion

1. **Open `game.py`**:
    - Navigate to the `TicTacToe` class.

2. **Implement the `move` Method**:
    - Since we already have failing tests for the `move` method, let's start by implementing this method.
    - Remove the `pass` statement inside the `move` method.
    - Place your cursor inside the `move` method.
    - GitHub Copilot will suggest code to implement this method. Accept the suggestion by pressing `Tab`.
    - Rerun the tests to see if the `move` method is working correctly. All tests should pass.

### Step 5: Using Copilot Chat

1. Write a test case for the `check_winner` method in `game_test.py`.
   - Write only the test description and let GitHub Copilot do the rest.
   **Hint**: A winner in TicTacToe is determined when a player has three of their symbols in a row, column, or diagonal.
2. Open GitHub Copilot Chat by clicking on the Copilot icon in the status bar.
3. Write a message to Copilot asking it to write the check_winner logic to pass the test(s).
4. Ask GitHub Copilot to rewrite the `play` method in `game.py` to use the `check_winner` method.
5. Test the implementation manually

## Advanced Features and Extensions

### Extension Ideas for Advanced Participants

1. **Multiplayer Features**:
    - Implement a server-client architecture to allow multiple players to play TicTacToe over a network.
    - Suggested libraries: `socket`, `flask`, or `django`.

2. **TicTacToe AI**:
    - Develop an AI opponent using algorithms like Minimax.
    - Suggested libraries: `numpy`, `scipy`.

3. **Enhance UI**:
    - Build a graphical user interface (GUI) using `tkinter` or `pygame`.

### Step 6: Implementing Advanced Features

1. **Start with a New Branch**:
    - Create a new branch for your advanced feature.
        ```sh
        git checkout -b feature/multiplayer
        ```

2. **Develop with Copilot**:
    - Use Copilot to assist with the development of your advanced feature by writing comments and allowing it to suggest implementations.

## References

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Python Unittest Documentation](https://docs.python.org/3/library/unittest.html)

