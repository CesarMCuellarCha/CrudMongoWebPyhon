from flask import Flask
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = '3209139823928139'

#configurar carpeta donde se van a guardar las fotos de los productos
app.config["UPLOAD_FOLDER"]="./static/imagenes/"

miConexion = MongoClient("mongodb://localhost:27017/")

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