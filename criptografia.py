# Algoritmos de Criptografia
# Hugo Garcia San Pedro - Universidad de Salamanca
# 05 - 06 - 2026
# Crear una biblioteca de funciones que realicen operaciones utilizadas frecuentemente en la criptografía 

# Funcion que crea el menu para seleccionar los diferentes algoritmos
def crear_Menu():
    # Pedimos al usuario que introduzca una de las opciones
    print("---Menu de Criptografia---")
    print("Elija una opcion: A - Z.")
    lectura = input()

    # Comprobamos que se introduzca una letra y no un numero
    if lectura.isnumeric():
        print("Error. Se ha introducido un numero y no una letra.")
        return

    # Forzamos que la variable introducida sea minuscula
    opcion = lectura.lower()

    # Estructura switch para el menu
    match opcion:
        case 'a':
            print("Se ha elegido la opcion A.")
            return
        case 'b':
            print("Se ha elegido la opcion B.")
            return 
        case 'c':
            print("Se ha elegido la opcion C.")
            return 
        case 'd':
            print("Se ha elegido la opcion D.")
            return 
        case 'z':
            print("Saliendo del programa.")
            return
        case _:
            print("Opcion incorrecta.")
            return

# Funcion principal
def main():
    crear_Menu()

# Se ejecuta la funcion principal
if __name__=="__main__":
    main()