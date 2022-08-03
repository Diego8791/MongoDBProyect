
from dataclasses import field
from multiprocessing.sharedctypes import Value
from pymongo import MongoClient 
from datetime import datetime
from ProductClass import Product


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
        typeProduct = input("Naturaleza del producto: ").upper()
        name = input("Marca del producto: ").upper()
        productExpiration = input("Indique fecha de vencimiento: ")
        amount = int(input("Indique cantidad de producto ingresado: "))
        price = float(input("Ingrese precio del producto: "))
        admissionDate = datetime(now.year, now.month, now.day, 0, 0)
        admissionDate.strftime('%Y/%m/%d')
        
        # registro en DB
        try:
            NewProduct = Product(stock, admissionDate, typeProduct, name, productExpiration, amount, price)       
            NewProduct.insertNewProduct()
            insert = input("¿Desea ingresar otro producto? s/n: ")
        except Exception as ex:
            raise Exception(ex)


def updateProduct(stock):
    '''
    Ingresar id y realizar un update de campos
    '''            
    # registro en DB
    """ try:
        
    except Exception as ex:
        raise Exception(ex) """


def deleteProduct(stock):
    '''
    Ingresar id y realizar un update de campos
    '''
    idProduct = input("Ingresar id del producto: ")
    # keyProduct = input("Ingresar clave del producto: ")
    # valueProduct = input("Ingrear valor de la clave: ")

    #print(idProduct, type(idProduct))
    # Borrar producto de la BD
    try:
        stock.delete_one({'_id': { "objectId" : idProduct}})
    except Exception as ex:
        raise Exception(ex)  


if __name__ == '__main__':

    # insertNewProduct(stock)
    # updateProduct(stock)
    deleteProduct(stock)
