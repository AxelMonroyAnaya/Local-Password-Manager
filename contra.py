import random,string,sqlite3,os
from time import sleep
from os import system

alfa = string.ascii_letters
numbers = string.digits
code = string.hexdigits

def ver():
    """

    :return:
    """
    cursor.execute("""
        SELECT * FROM CREDENCIALES;
    """)
    res = cursor.fetchall()
    conexion.commit()
    return res

def creacion():
    contra = str()
    for i in range(0, 8):
        contra += str(random.choice(code))+str(random.choice(alfa))+str(random.choice(numbers))+str(random.choice(numbers))+str(random.choice(numbers))
    sleep(5)
    print("\tla contrasena generada es: ",contra)
    usuario = os.environ.get("USER") or os.environ.get("USERNAME")
    usuario = str(usuario)
    if usuario:
        print(f"El usuario registrado es: {usuario}")
    else:
        print("No se pudo determinar el nombre del usuario.")
        usuario = str(input("\ncual es tu nombre"))

        if not usuario.strip():
            raise ValueError("\nEl nombre no puede estar vacío.")

        # Validar que no contenga números
        if any(char.isdigit() for char in usuario):
            raise ValueError("\nEl nombre no puede contener números.")

    eleccion = int(input("\n deseeas ingresar el correo y la plataforma asociados con esta contrasena?\t 1.si \t 2.no\n (selecciona el numero de la eleccion)  "))
    if eleccion == 1:
        correo = str(input("\ncual es correo :"))
        plataforma = str(input("\ncual es la plataforma :"))
        insertar(usuario,contra,plataforma,correo)
    else:
        insertar(usuario, contra,"","")

conexion = sqlite3.connect("contra.db")
cursor  = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS credenciales(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario VARCHAR(45) NOT NULL,
        fecha_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
        plataforma VARCHAR(45),
        contra VARCHAR(45) NOT NULL,
        correo TEXT
    )
""")
conexion.commit()

def insertar(usuario,contra, plataforma= "",correo=""):
    sleep(5)
    if contra:
        cursor.execute("""
            insert into credenciales(usuario,plataforma,contra,correo)
            values(?,?,?,?) 
            """,(usuario,plataforma,contra,correo))
        conexion.commit()

    else:
        contra = creacion()
sleep(5)
system("cls")
print("*"*5,"menu principal","*"*5)
menu = 8
while menu ==  8 :
    opc= int(input("\n selecciona una opcion\n1._ Generar contraseña\n2.- ver contrasenas \n3.- eliminar contrasenas \n4.-modificar contrasenas"))
    if opc == 1:
        creacion()
    if opc == 2:
        res = ver()
        for i in res :
            print(f"\n\n| plataforma : {i[3]} |  password : {i[4]} |\n")
    if opc == 5:

        break
    else:
        pass