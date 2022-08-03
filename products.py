

class Products:

    def __init__(self, stock, admissionDate, typeProduct, mark, amount, priceCost, priceSale, productExpiration):
        self.stock = stock,
        self.admissionDate = admissionDate,
        self.typeProduct = typeProduct,
        self.mark = mark,
        self.amount = amount,
        self.priceCost = priceCost,
        self.priceSale = priceSale,
        self.productExpiration = productExpiration


    def productIncome(self):
        '''
        Ingreso de productos        
        '''
        try:
            self.stock.insert_one({
                'admissionDate': self.admissionDate,
                'typeProduct': self.typeProduct,
                'mark': self.mark,
                'amount': self.amount,
                'priceCost': self.priceCost,
                'priceSale': self.priceSale,
                'producExpiration': self.productExpiration
                })
        except Exception as ex:
            raise Exception(ex)
