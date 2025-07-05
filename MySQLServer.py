import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',      # Replace with your MySQL username
            password=''      # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as create_error:
                print(f"Error creating database: {create_error}")
            
            # Commit the transaction
            connection.commit()
            
    except Error as connection_error:
        print(f"Failed to connect to MySQL server: {connection_error}")
    except Exception as unexpected_error:
        print(f"An unexpected error occurred: {unexpected_error}")
    finally:
        try:
            if cursor is not None:
                cursor.close()
        except Error as cursor_error:
            print(f"Error closing cursor: {cursor_error}")
        
        try:
            if connection is not None and connection.is_connected():
                connection.close()
                print("MySQL connection closed successfully")
        except Error as connection_close_error:
            print(f"Error closing connection: {connection_close_error}")

if __name__ == "__main__":
    create_database()
