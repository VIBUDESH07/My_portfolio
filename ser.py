import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="hackbuzz"
    )

    if connection.is_connected():
        print("Connected to MySQL database")


except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if 'connection' in locals():
        connection.close()
        print("MySQL connection closed")
