from datetime import date

import connection
import mysql.connector
from mysql.connector import Error

# una funcion a la q le pasaremos 2 valores, los precios y q nos muestre todos los portatiles q haya en ese rango de precios

def selectRango(precio1, precio2):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='root',
                                             password='1234'
                                             )
        query = "SELECT * FROM LAPTOP WHERE PRICE BETWEEN %s AND %s"
        tid = (precio1,precio2)

        cursor = connection.cursor()
        cursor.execute(query,tid)

        records = cursor.fetchall()
        print("Fetching all rows using column name")

        for row in records:
            id = row[0]
            name = row[1]
            price = row[2]
            purchase_date = row[3]
            print(id, name, price, purchase_date)

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

        print("Fetching all rows using column name")

        for row in records:
            id = row["ID"]
            name = row["NAME"]
            price = row["PRICE"]
            purchase_date = row["PURCHASE_DATE"]
            print(id, name, price, purchase_date)

    except Error as e:
        print("Error while creating the data base ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    selectRango(100, 400)