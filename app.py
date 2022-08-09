
from typing import Any
from ProductClass import Product
from datetime import datetime


def incomeNewProduct():

    '''
    Función para ingresar productos al stock de inventario
    '''
    now = datetime.now()

    insert = 's'
    while insert == 's':
        print('------- I N G R E S O   D E   P R O D U C T O --------')
        # ingreso del producto
        barCod = int(input("Ingresar código de barras: "))
        typeProduct = input("Naturaleza del producto: ").upper()
        name = input("Marca del producto: ").upper()
        amount = int(input("Indique cantidad de producto ingresado: "))
        priceCost = round(float(input("Ingrese precio de costo: ")), 2)
        priceSale = round(float(input('Indique precio ne venta: ')), 2)
        productExpiration = input("Fecha de vencimiento: ")
        # fecha de admisión del producto
        admissionDate = datetime(now.year, now.month, now.day, 0, 0)
        admissionDate.strftime('%Y/%m/%d')
        
        # registro en DB
        try:
            NewProduct = Product(barCod, admissionDate, typeProduct, name, productExpiration, amount, priceCost, priceSale)       
            NewProduct.insertNewProduct()
            insert = input("¿Desea ingresar otro producto? s/n: ")
        except Exception as ex:
            raise Exception(ex)


def updateProduct():
    '''
    Ingresar id y realizar un update de campos
    '''            
    # registro en DB
    barCodPro = int(input('Código de barras: '))
    item = input('ingresar clave de actualizacion: ')
    valueItem = input('Indicar valor de clave: ')
    # convertir precios en float
    try:
        if item == 'priceCost' or item == 'priceSale':
            valueItem = round(float(valueItem), 2)
        elif item == 'name' or item == 'typeProduct':
            valueItem = valueItem.upper()
        elif item == 'amount':
            valueItem = int(valueItem)
        else:
            pass
    except Exception as ex:
        raise Exception(ex) 
    # update
    try:
        updProduct = Product(barCod=Any, admissionDate=Any, typeProduct=Any, name=Any, productExpiration=Any, amount=Any,priceCost=Any, priceSale=Any)
        updProduct.updateProduct(barCodPro, item, valueItem)    
    except Exception as ex:
        raise Exception(ex)


def deleteProduct():
    '''
    Ingresar codigo de barras y borrar el articulo
    '''
    barCod = int(input("Ingresar id del producto: "))
    try:
        delProduct = Product( barCod=Any, admissionDate=Any, typeProduct=Any, name=Any, productExpiration=Any, amount=Any,priceCost=Any, priceSale=Any)
        delProduct.deleteProduct(barCod)    
    except Exception as ex:
        raise Exception(ex)

       
if __name__ == '__main__':

    incomeNewProduct()
    # updateProduct()
    # deleteProduct()
