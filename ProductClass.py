from conexionBD import conexionStock


class Product:

    def __init__(self, barCod, admissionDate, typeProduct, name, productExpiration, amount, priceCost, priceSale):
        self.barCod = barCod
        self.admissionDate = admissionDate
        self.typeProduct = typeProduct
        self.name = name
        self.productExiration = productExpiration
        self.amount = amount
        self.priceCost = priceCost
        self.priceSale = priceSale
        
    
    def insertNewProduct(self):
        stock = conexionStock()
        stock.insert_one({
                'barCod': self.barCod,
                'admissionDate': self.admissionDate,
                'typeProduct': self.typeProduct,
                'name': self.name,
                'productExpiration': self.productExiration,
                'amount': self.amount,
                'priceCost': self.priceCost,
                'priceSale': self.priceSale
            })


    def updateProduct(self, barCodPro, item, valueItem):
        stock = conexionStock()
        stock.update_one({'barCod': barCodPro}, 
            {'$set': {
                item: valueItem
        }})


    def deleteProduct(self, barCodPro):
        stock = conexionStock()
        stock.delete_one({'barCod': barCodPro})