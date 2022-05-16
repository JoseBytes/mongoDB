from mongo import *
from getpass import getpass

print("User Panel")
print()

login = bool()

username = input("Ingrese username: ")
query = col.find({"username":username})
count = 2

for data_user in query:
    if username != data_user['username']:
        exit()
    else:
        while count>=0:
            password = getpass("Introduce password: ")
            if username==data_user['username'] and password==data_user['password']:
                login = True
                break
            else:
                if count==2:
                    print("Te quedan 2 intentos.")
                elif count==1:
                    print("Te queda 1 intento, si fallas el ultimo seras bloqueado por 1 hora.")
                elif count==0:
                    print("Usuario bloqueado por seguridad.")
            count -=1

if login==True:
    print(f"Bienvenido, {data_user['nombre']}")

