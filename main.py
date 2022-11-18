import random, os, string

characters = list(string.ascii_letters + string.digits)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

print("\x1b[1;31m" + "\n¡¡¡Recuerde crear un .txt donde se almacenaran las contraseñas!!!")
input("\x1b[1;37m" + "\nPreciona ENTER para continuar >> ")
clear()

def generatePass():
    passLength=int(input("\x1b[1;37m" + "Que longitud desead que tenga tu contraseña?\n>>" + "\x1b[1;33m" + " "))
    
    random.shuffle(characters)
    password = []

    for x in range(passLength):
        password.append(random.choice(characters))
    random.shuffle(password)
    password="".join(password)

    fileName= input("\x1b[1;37m" + "\n" + r"Ingrese el nombre o ubicacion del archivo (ej. test.txt o D:\Proyectos\PYTHON\PasswordGenerator\test.txt)" + "\n>>" + "\x1b[1;33m" + " ")
    red=input("\x1b[1;37m" + "\nA que app pertenece?\n>>" + "\x1b[1;33m" + " ")
    print("\x1b[1;37m")
    f = open(fileName,"a")
    f.write("\n" + "\n" + red + "\n" + password)
    f.close()
    print("\x1b[1;31m" + "Lectura del txt {")
    print("\x1b[1;37m")
    f = open(fileName,"r")
    print(f.read())
    f.close()
    print("\x1b[1;31m" + "\n} Fin de lectura del txt")
    
    print("\x1b[1;32m" + "\nContraseña generada con exito!!!")

option = input("\x1b[1;37m" + "¿Quieres generar una contraseña? (y/n)\n>>" + "\x1b[1;33m" + " ")
clear()
if option == "y":
    generatePass()
    input("\x1b[1;37m" + "\nPreciona ENTER para continuar >> ")
elif option == "n":
    print("\x1b[1;33m" + "Bye!")
    quit()
else:
    print("\x1b[1;31m" + "Opcion invalida")