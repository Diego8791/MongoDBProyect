from pymongo import MongoClient 


def conexionStock():
    # conexión a base de datos
    MONGO_URI = 'mongodb://localhost'
    client = MongoClient(MONGO_URI)

    # iniciamos la base de datos
    db = client['store']

    # inicial la coleccion stock
    stock = db['products']

    # retornar conexion
    return stock
