from datetime import date

import connection
import mysql.connector
from mysql.connector import Error

# una funcion a la q le pasaremos 2 valores, los precios y q nos muestre todos los portatiles q haya en ese rango de precios

def updateLaptop(price,id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='root',
                                             password='1234'
                                             )
        query = "UPDATE LAPTOP SET PRICE = %s WHERE ID = %s"
        input_data = (price,id)

        cursor = connection.cursor()
        cursor.execute(query,input_data)
        connection.commit()
        print("Record updated successfully")

    except Error as e:
        print("Error while creating the data base ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def updateLaptop_porcentaje(porcentaje):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='root',
                                             password='1234'
                                             )
        query = "UPDATE LAPTOP SET PRICE = PRICE+(PRICE*(%s/100)) "
        input_data = (porcentaje,)

        cursor = connection.cursor()
        cursor.execute(query,input_data)
        connection.commit()
        print("Record updated successfully")

    except Error as e:
        print("Error while creating the data base ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def selectNormal():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='root',
                                             password='1234'
                                             )

        query = "SELECT * FROM LAPTOP"
        # SELCT * FROM LAPTOP WHERE ID = %s  -> tid = (id,3) cursor.execute(query,tid)

        cursor = connection.cursor(dictionary=True)
        # Si aqui no le pones dictionary true, a la hora de recorrerlos tendras que poner los indices en vez de los nombres de las columnas

        result = cursor.execute(query)
        records = cursor.fetchall()
        print("______________________________________________________")
        print("Fetching all rows using column name")

        for row in records:
            id = row["ID"]
            name = row["NAME"]
            price = row["PRICE"]
            purchase_date = row["PURCHASE_DATE"]
            print(id, name, price, purchase_date)
        print("______________________________________________________")
    except Error as e:
        print("Error while updating the record ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    selectNormal()
    updateLaptop(485.99, 1)
    selectNormal()
    updateLaptop_porcentaje(3)
    selectNormal()

