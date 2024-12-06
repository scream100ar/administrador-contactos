import funciones


def menu():
    """Pantalla principial del programa en formato
    de menú con opciones seleccionables.
    Cada opción se almacena en la variable 'eleccion'.
    La variable booleana 'valor' indica que el usuario
    ya seleccionó una opción.
    """
    print("Administrador de Contactos")
    print("Elija una opción:")
    print("1 - Buscar una persona")
    print("2 - Agregar o actualizar los datos de una persona")
    print("3 - Importar contactos desde un archivo")
    print("4 - Imprimir toda la agenda")
    print("o cualquier otra tecla para salir")
    global valor
    global eleccion
    eleccion = input()
    if eleccion == "1" or eleccion == "2"\
            or eleccion == "3" or eleccion == "4":
        valor = True
    else:
        valor = False


funciones.leer_agenda()
menu()


while valor is True:
    print("elección: ", eleccion)
    if eleccion == "1":     # Buscar una persona
        print("\nBuscar una persona en la agenda:")
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        funciones.buscar(nombre, apellido)
    elif eleccion == "2":   # Agregar o actualizar los datos de una persona
        print("\nAgregar o actualizar una persona:")
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        telefono = input("Ingrese el telefono de la persona: ")
        funciones.agregar(nombre, apellido, telefono)
    elif eleccion == "3":   # Importar contactos desde un archivo
        funciones.importar()
    elif eleccion == "4":   # Imprimir toda la agenda
        funciones.imprimir_agenda()
    else:
        break
    menu()
