from pymongo import MongoClient 

#conexión a base de datos
MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

# iniciamos la base de datos
db = client['store']

# inicial la coleccion stock
conexion = db['products']