import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='Electronics',
                                        user='root',
                                        password = '1234'
                                        )
    query = "CREATE TABLE LAPTOP(ID INT(11) NOT NULL,NAME VARCHAR(250) NOT NULL,PRICE FLOAT NOT NULL,PURCHASE_DATE DATE NOT NULL,PRIMARY KEY (ID))"
    cursor = connection.cursor()
    result = cursor.execute(query)
    print("Table Laptop created successfully")
except Error as e:
    print("Error while creating the data base ", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")