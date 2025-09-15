# 🗳️ Poll Management App

A command-line **Poll Management System** built with **Python 3** and **PostgreSQL**, allowing users to create polls, add options, vote, view results, and randomly select winners.  

---

## 📌 Features
- Create new polls with multiple options  
- List all open polls  
- Vote on poll options as a specific user  
- View votes per poll with percentage breakdown  
- See detailed vote logs with timestamps  
- Randomly pick a winner from voters of a specific option  
- Database-backed using PostgreSQL with connection pooling  

---

## 🗂 Project Structure

    ├── main.py # Main program and CLI menu
    ├── connection_pool.py # PostgreSQL connection pooling
    ├── database.py # SQL queries and database helpers
    ├── models/
    │ ├── poll.py # Poll class
    │ └── option.py # Option class
    └── README.md # Project documentation

---

## ▶️ Requirements
- Python 3.8+  
- PostgreSQL server running  
- Python packages:
    ```bash
    pip install psycopg2-binary python-dotenv pytz

---

## .env file for database credentials (optional, prompts user if missing):**
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=your_database
    DB_USER=your_username
    DB_PASSWORD=your_password

---

## 🏁 Setup & Run

1. Make sure PostgreSQL is running and a database exists:
    ```sql
    CREATE DATABASE poll_db;

2. Run the application:
    ```bash
   python main.py

3. Follow the menu to create polls, vote, view results, and pick random winners.

---

## 🧑‍💻 Example Usage

    -- Menu --
    
    1) Create new poll
    2) List open polls
    3) Vote on a poll
    4) Show poll votes
    5) Select a random winner from a poll option
    6) Exit
    
    Enter your choice: 1
    Enter poll title: Favorite Programming Language
    Enter poll owner: Erfan
    Enter new option text (or leave empty to stop adding options): Python
    Enter new option text (or leave empty to stop adding options): JavaScript
    Enter new option text (or leave empty to stop adding options): 

---