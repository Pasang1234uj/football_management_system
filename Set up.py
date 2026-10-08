setup.py
--------
Optional command-line setup. Most people should just run:

    python main.py

main.py now shows a graphical "Connect to MySQL" screen automatically the
first time, or whenever it can't connect - so this script is only useful
if you prefer a terminal, or want to script the setup step.
"""
import mysql.connector

from database import initialize_database

# Set your MySQL password here so you're not asked for it every time.
MYSQL_PASSWORD = "MySQL@123"


def run():
    print("=== Football League Management System - first-time setup ===\n")
    host = input("MySQL host [localhost]: ").strip() or "localhost"
    port = int(input("MySQL port [3306]: ").strip() or 3306)
    user = input("MySQL user [root]: ").strip() or "root"
    password = MYSQL_PASSWORD

    try:
        initialize_database(host, port, user, password)
    except mysql.connector.Error as e:
        print(f"\nCould not connect to MySQL: {e}")
        return
    except OSError as e:
        print(f"\nCould not read setup.sql: {e}")
        return

    print("\nDatabase and tables created. Connection saved to config.json.")
    print("Setup complete. Start the program with:  python main.py")
    print("Then click Sign Up - the first person signs up as Super Admin and sets the refer code.")


if name == "main":
    run()
