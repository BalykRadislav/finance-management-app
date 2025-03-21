# my-python-project README.md

# My Python Project

This project consists of a simple Python application that collects user information, specifically their name and age.

## Project Structure

```
my-python-project
├── src
│   ├── main2.py       # Main application file that uses user_info functions
│   └── user_info.py   # Contains functions to get user name and age
└── README.md          # Documentation for the project
```

## Files Description

- **src/user_info.py**: This file contains two functions:
  - `get_age()`: Prompts the user to enter their age and returns it.
  - `get_name()`: Prompts the user to enter their name and returns it.

- **src/main2.py**: This file imports the functions from `user_info.py` and uses them to ask the user for their name and age, then displays the collected information.

## Usage

1. Navigate to the project directory.
2. Run the `main2.py` file to start the application.
3. Follow the prompts to enter your name and age.

## Requirements

- Python 3.x

## Author

GitHub Copilot