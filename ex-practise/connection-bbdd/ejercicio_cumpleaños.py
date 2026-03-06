"""
    crear una bbdd 'familia' dentro de ella una tabla que se llame 'cumpleaños' con los
    siguientes campos: Nombre, fecha de cumpleaños Ambas PK
    Nos insertamos a nosotros mismos en la feccha, cada uno de los 5 añpos siguientes a los del sistema
"""
from datetime import datetime

import mysql.connector
from mysql.connector import Error

def crear_bbdd():


    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='sys',
                                             user='root',
                                             password='1234'
                                             )
        query = "CREATE DATABASE Familia"
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

def crear_tabla():


    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Familia',
                                             user='root',
                                             password='1234'
                                             )
        query = "CREATE TABLE CUMPLEAÑOS(NOMBRE VARCHAR(250)  NOT NULL,FECHA_CUMPLEAÑOS DATE NOT NULL,PRIMARY KEY (NOMBRE,FECHA_CUMPLEAÑOS))"
        cursor = connection.cursor()
        result = cursor.execute(query)
        print("Table Cumpleaños created successfully")
    except Error as e:
        print("Error while creating the data base ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def insertar_datos():

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Familia',
                                            user='root',
                                            password = '1234'
                                            )
        query = "INSERT INTO CUMPLEAÑOS VALUES (%s,%s)"
        #record = (id,name,price,purchase_date)
        fecha_cumple = datetime(2026,1,27)
        fecha2 =datetime(fecha_cumple.year +5,fecha_cumple.month,fecha_cumple.day)
        fecha3 = datetime(fecha2.year +10,fecha_cumple.month,fecha_cumple.day)

        records = [("Mar",fecha_cumple),("Mar2", fecha2), ("Mar3",fecha3)]
        cursor = connection.cursor()
        cursor.executemany(query,records)
        connection.commit()
        print("Data insertion successfully")
        cursor.close()
    except Error as e:
        print("Error while inserting data base ", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def ver_datos():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Familia',
                                             user='root',
                                             password='1234'
                                             )
        query = "SELECT * FROM CUMPLEAÑOS"
        cursor = connection.cursor()
        cursor.execute(query)

        records = cursor.fetchall()
        print("Fetching all rows using column name")

        for row in records:
            NOMBRE = row[0]
            CUMPLEAÑOS = row[1]
            print(NOMBRE, CUMPLEAÑOS)

    except Error as e:
        print("Error while creating the data base ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



if __name__ == "__main__":
    crear_bbdd()
    crear_tabla()
    insertar_datos()
    ver_datos()
