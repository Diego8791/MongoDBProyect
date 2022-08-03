
from conexiondb import conexion
from products import Products
from datetime import datetime


def incomeNewProduct(stock):
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
        mark = input("Marca del producto: ").upper()
        amount = int(input("Indique cantidad de producto ingresado: "))
        priceCost = float(input("Ingrese precio de costo: "))
        priceSale = float(input("Ingrese precio de venta: "))
        productExpiration = input("Indique fecha de vencimiento: ")
        # cargar en base de datos
        try:
            pIncome = Products(stock, admissionDate, typeProduct, mark, amount,priceCost, priceSale, productExpiration)
            pIncome.productIncome()
        except Exception as ex:
            raise Exception(ex)
        # consulta para ingresar otro producto
        insert = input("¿Desea ingresar otro producto? s/n: ")


if __name__ == '__main__':

    stock = conexion
    incomeNewProduct(stock)
