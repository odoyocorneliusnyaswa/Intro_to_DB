import mysql.connector
from mysql.connector import Error

def create_database():
    """Create a MySQL database named 'alx_book_store' if it doesn't exist."""
    try:
        # Connect to MySQL Server (Update credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Create the database
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
