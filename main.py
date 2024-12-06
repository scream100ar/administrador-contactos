import funciones


def mostrar_menu():
    """Despliega el menú principal y retorna la elección del usuario."""
    print("Administrador de Contactos")
    print("Elija una opción:")
    print("1 - Buscar una persona")
    print("2 - Agregar o actualizar los datos de una persona")
    print("3 - Importar contactos desde un archivo")
    print("4 - Imprimir toda la agenda")
    print("Cualquier otra tecla para salir")
    return input("Ingrese su elección: ")


def ejecutar_opcion(eleccion):
    """Ejecuta la acción correspondiente a la elección del usuario.

    Args:
        eleccion (str): Opción seleccionada por el usuario."""
    if eleccion == "1":
        print("\nBuscar una persona en la agenda:")
        nombre = input("Ingrese el nombre: ").strip()
        apellido = input("Ingrese el apellido: ").strip()
        funciones.buscar(nombre, apellido)
    elif eleccion == "2":
        print("\nAgregar o actualizar los datos de una persona:")
        nombre = input("Ingrese el nombre: ").strip()
        apellido = input("Ingrese el apellido: ").strip()
        telefono = input("Ingrese el teléfono: ").strip()
        funciones.agregar(nombre, apellido, telefono)
    elif eleccion == "3":
        print("\nImportando contactos desde un archivo...")
        funciones.importar()
    elif eleccion == "4":
        print("\nImprimiendo toda la agenda:")
        funciones.imprimir_agenda()
    else:
        return False
    return True


def main():
    """Punto de entrada principal del programa."""
    funciones.leer_agenda()
    while True:
        eleccion = mostrar_menu()
        if not ejecutar_opcion(eleccion):
            print("\nSaliendo del programa.")
            break


if __name__ == "__main__":
    main()
