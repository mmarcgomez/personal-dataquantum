import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='sys',
                                        user='root',
                                        password = '1234'
                                        )
    query = "CREATE DATABASE Electronics"
    cursor = connection.cursor()
    result = cursor.execute(query)
    print("MySQL database created successfully")
except Error as e:
    print("Error while creating the data base ", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")