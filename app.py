from flask import Flask
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = '3209139823928139'

#configurar carpeta donde se van a guardar las fotos de los productos
app.config["UPLOAD_FOLDER"]="./static/imagenes/"

#uri conexión local
uri="mongodb://localhost:27017/"
#uri remota (aquí cada uno obtiene de acuerdo a su base de datos remota)
#remplazan <db_username> Y <db_password> en la cadena obtenida
uri="mongodb+srv://<db_username>:<db_password>@runt.oudoapr.mongodb.net/?retryWrites=true&w=majority&appName=RUNT"
miConexion = MongoClient(uri)


#crear base datos
baseDatos = miConexion["Negocio"]

#crear la colección
productos = baseDatos["Productos"]

#crear la coleccion
usuarios = baseDatos["Usuarios"]

if __name__=="__main__":
    from controladores.productoController import *
    from controladores.usuarioController import *
    app.run(port=5000, debug=True)