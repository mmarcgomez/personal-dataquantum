from datetime import date

import connection
import mysql.connector
from mysql.connector import Error
def insertar(id,name,price,purchase_date):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Electronics',
                                            user='root',
                                            password = '1234'
                                            )
        query = "INSERT INTO LAPTOP VALUES (%s,%s,%s,%s)"
        #record = (id,name,price,purchase_date)
        records = [(4,"MSI League of Legends",899,99,'2026-08-23'),
                   (5,"HP Office model",299.99,'2026-05-03'),
                   (6,"Lenovo gaming model",499.95),'2025-06-21']
        cursor = connection.cursor()
        result = cursor.execute(query,records)
        connection.commit()
        print("Data insertion successfully")
        cursor.close()
    except Error as e:
        print("Error while creating the data base ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def insertar_tuplas():

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Electronics',
                                            user='root',
                                            password = '1234'
                                            )
        query = "INSERT INTO LAPTOP VALUES (%s,%s,%s,%s)"
        #record = (id,name,price,purchase_date)
        records = [(4,"MSI League of Legends",899.99,'2026-08-23'),(5,"HP Office model",299.99,'2026-05-03'),(6,"Lenovo gaming model",499.95,'2025-06-21')]
        cursor = connection.cursor()
        cursor.executemany(query,records)
        connection.commit()
        print("Data insertion successfully")
        cursor.close()
    except Error as e:
        print("Error while creating the data base ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    """insertar(1,"Lenovo",399.99,date.today())
    insertar(2, "Ryzen AMD", 599.99, date.today())
    insertar(3, "HP Monster", 699.99, date.today())"""
    insertar_tuplas()