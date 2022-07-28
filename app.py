
from flask import jsonify
from pymongo import MongoClient 
from datetime import datetime
import traceback


# conexión a base de datos
MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

# iniciamos la base de datos
db = client['store']

# inicial la coleccion stock
stock = db['products']


def insertNewProduct(stock):
    '''
    Función para ingresar productos al stock de inventario
    '''
    now = datetime.now()

    insert = 's'
    while insert == 's':
        # ingreso del producto
        admissionDate = datetime(now.year, now.month, now.day, 0, 0)
        admissionDate.strftime('%Y/%m/%d')
        typeProduct = input("Naturaleza del producto: ").upper()
        name = input("Marca del producto: ").upper()
        productExpiration = input("Indique fecha de vencimiento: ")
        amount = int(input("Indique cantidad de producto ingresado: "))
        price = float(input("Ingrese precio del producto: "))
        print(admissionDate, typeProduct, name, productExpiration, amount, price)
        # registro en DB
        try:
            stock.insert_one({
                'admissionDate': admissionDate,
                'typeProduct': typeProduct,
                'name': name,
                'productExpiration': productExpiration,
                'amount': amount,
                'price': price
            })
        except:
            # error
            return jsonify({'trace': traceback.format_exc})

        insert = input("¿Desea ingresar otro producto? s/n: ")


if __name__ == '__main__':

    insertNewProduct(stock)