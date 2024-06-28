# Library Management System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Library Management System is a desktop application built with Python using Tkinter for the GUI and SQLite for the database. It allows users to manage books, members, and transactions (issue and return of books) efficiently. This project demonstrates the use of Object-Oriented Programming (OOP) concepts and database integration.

## Features
- Add, view, and manage books.
- Add, view, and manage library members.
- Issue and return books, with fine calculation.
- View all transactions (issues and returns).

## Requirements
- Python 3.x
- SQLite
- Tkinter (comes bundled with Python)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```
2. Install the required dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Initialize the database:
    ```sh
    python init_db.py
    ```
2. Run the main application:
    ```sh
    python main.py
    ```

## Project Structure
```plaintext
library-management-system/
├── library.db        # SQLite database file
├── main.py           # Main application file
├── init_db.py        # Database initialization script
└── README.md         # Project documentation
```


## Database Schema
The SQLite database (library.db) consists of three tables:
```
books:

id (INTEGER, PRIMARY KEY)
title (TEXT)
author (TEXT)
year (INTEGER)
isbn (TEXT)

members:

id (INTEGER, PRIMARY KEY)
name (TEXT)
email (TEXT)


transactions:

id (INTEGER, PRIMARY KEY)
book_id (INTEGER, FOREIGN KEY)
member_id (INTEGER, FOREIGN KEY)
issue_date (TEXT)
return_date (TEXT)
fine (REAL)

```