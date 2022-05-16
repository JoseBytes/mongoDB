from pymongo import MongoClient

conexion = MongoClient('mongodb://127.0.0.1:27017')
db = conexion['proyecto1']
col = db['usuarios']


#db.create_collection("users") crear coleccion

#print(conexion.list_database_names()) #Muestra las bases de datos
#print(db.list_collection_names()) #Muestra las colecciones de la base de datos
#print(col.count_documents({})) # Muestra los documentos de la coleccion



"""col.insert_one({
    "id":"3",
    "nombre":"Viviana Lujan",
    "username": "vivi",
    "password":"12345",
    "pais":"Venezuela",
    "sexo":"Femenino",
    "statusAcc":"1"
    }) """