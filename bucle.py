# Llenar una lista con los elementos numeros del 1 al 50 y mostrarlos listado con 1-2-3-4....49-50
from getpass import getpass

print("Panel de Usuario")
print()

db_user = {"admin":"root"}
i = 2

login = bool()

for key,value in db_user.items():
    while i>=0:
        user = input("Username: ")
        passwd = getpass("Password: ")
        if user==key and passwd==value:
            print("OK !")
            login = True
            break
        elif user!=key:
            print(f"Error User ({i} Intento)\n")
        elif passwd!=value:
            print(f"Error Pass ({i} Intento)\n")
        else:
            print(f"Error Auth ({i} Intento)\n")
            exit()
        i-=1

if login==True:
    print("INTO PANEL")
