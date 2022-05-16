from mongo import *
from getpass import getpass

def search_user(username):
    query = col.find({'username':username})
    for data_user in query:
        return data_user

def add_user(nombre, username, password, pais, sexo):
    if search_user(username) is None:
        col.insert_one({
            "id":"4",
            "nombre": nombre,
            "username": username,
            "password": password,
            "pais": pais,
            "sexo": sexo,
            "statusAcc":"1"
            })
        print("Creacion Exitosa")
    else:
        print("Existe el usuario")

def password_verify(password):
    if user_name is None:
        return "Error de Autenticacion"
    else:
        if password==user_name['password']:
            return True
        else:
            return "Error de Autenticacion"

user_name = search_user(input("Username: "))
password = password_verify(input("Password: "))

if password == True:
        print(f"Bienvenid@, {user_name['nombre']}\n")
        print("2 - Agregar nuevo usuario")
        print("3 - Buscar usuarios")
        opcion = int(input("Ingrese una opcion: "))
        if opcion==2:
            print("Agregar personas")
            nombre = (input("Nombre: "))
            username = (input("Usuario: "))
            password = (input("Password: "))
            pais =(input("Pais: "))
            sexo = (input("sexo: "))
            add_user(nombre,username,password,pais,sexo)
        if opcion==3:
            print("Buscador de Usuarios")
            name = input("Ingresa el nombre del usuario: ")
            if search_user(name) is None:
                print("No se encontro")
            else:
                print(search_user(name))
        else:
            print("Opcion invalida")

else:
        print(password)
