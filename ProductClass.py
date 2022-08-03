
class Product:

    def __init__(self, stock, admissionDate, typeProduct, name, productExpiration, amount, price):
        self.stock = stock
        self.admissionDate = admissionDate
        self.typeProduct = typeProduct
        self.name = name
        self.productExiration = productExpiration
        self.amount = amount
        self.price = price
        
    
    def insertNewProduct(self):
        self.stock.insert_one({
                'admissionDate': self.admissionDate,
                'typeProduct': self.typeProduct,
                'name': self.name,
                'productExpiration': self.productExiration,
                'amount': self.amount,
                'price': self.price
            })


    def updateProduct(self, idProduct):
        self.stock.update_one({'_id': idProduct}, 
            {'$set': {
                'admissionDate': self.admissionDate,
                'typeProduct': self.typeProduct,
                'name': self.name,
                'productExpiration': self.productExiration,
                'amount': self.amount,
                'price': self.price
        }})