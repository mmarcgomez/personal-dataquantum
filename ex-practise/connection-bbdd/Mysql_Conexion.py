import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='sys',
                                        user='root',
                                        password = '1234'
                                        )
    if connection.is_connected():
        db_info = connection.server_info
        print("Connected to MySQL Server version", db_info)

        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You are conneted to database: ", record)

        cursor.execute("SELECT count(*) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'bd_scott'")
        record = cursor.fetchone()

        if record[0] == 0:
            print("No existe")
        else:
            print("Si existe")

except Error as e:
    print("Error while connectir to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")