from flask import Flask, render_template, jsonify, request, redirect, session
import pymongo.errors
#importar objetos del archivo app.py
from app import app, baseDatos, usuarios 
#libreria para obtener nombre de archivo
from werkzeug.utils import secure_filename 
#libreria para guardar archivos en servidor
import os
#import pymongo
import pymongo
from bson.objectid import ObjectId

@app.route("/")
def iniciar():
    """_summary_
        Recibe la petición del cliente para mostrar
        la interfaz de iniciar la sesión
    Returns:
        _type_: Renderiza el formulario de iniciar sesión
    """
    return render_template("frmIniciarSesion.html")

@app.route("/iniciarSesion", methods=['POST'])
def iniciarSesion():
    """_summary_
        Recibe la petición para iniciar la sesión
        en la aplicación
    Returns:
        _type_: Redirecciona a listar los productos
        si las credenciales de ingreso son correctas,
        de lo contrario lo retorna a la misma vista
        con un mensaje de credenciales no válidas
    """
    try:
        if request.method=="POST":
            username = request.form["txtUsername"]
            password = request.form["txtPassword"]        
            usuario = usuarios.find_one({"username": username, "password":password})
            
            if (usuario is not None):
                session['username'] = username
                return redirect("/listarProductos")
            else:
                mensaje="Credenciales no válidas. Verifique"
                return render_template("frmIniciarSesion.html", mensaje=mensaje)
        else:
            mensaje="Debe primero ingresar sus credenciales desde el formulario"
            return render_template("frmIniciarSesion.html", mensaje=mensaje)
    except pymongo.errors.PyMongoError as error:
        mensaje=str(error)
        
@app.route("/salir", methods=['GET'])
def salir():
    """_summary_
        Elimina las variables de sesión existentes
    Returns:
        _type_: rdirecciona al formuario de inicio de sesión
    """
    session.clear()
    mensaje="Ha cerrado la sesión de manera exitosa..."
    return render_template("frmIniciarSesion.html", mensaje=mensaje)