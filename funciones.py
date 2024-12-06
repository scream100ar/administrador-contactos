agenda = {}


def leer_agenda():
    """Lee el archivo agenda.txt y
    guarda la informacion en el diccionario agenda.
    La clave del diccionario es el orden en que se leen
    los contactos de agenda.txt comenzando por el 1.
    Cada indice tiene dentro un diccionario con los
    datos del contacto: Nombre, Apellido y Teléfono.
    Atrapa excepciones relacionadas al trabajo con archivos."""
    try:
        with open('agenda.txt', 'r', encoding="utf-8") as archivo:
            lineas_agenda = archivo.readlines()
        for linea in range(0, len(lineas_agenda), 4):
            agenda[str(len(agenda) + 1)] = {
                "Nombre": lineas_agenda[linea].split(": ")[1].strip(),
                "Apellido": lineas_agenda[linea+1].split(": ")[1].strip(),
                "Teléfono": lineas_agenda[linea+2].split(": ")[1].strip()
            }
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except PermissionError:
        print("No se tienen permisos para acceder al archivo.")
    except Exception as e:
        print(f"Error al leer la agenda: {e}")


def escribir_agenda():
    """Toma el contenido del diccionario agenda y lo escribe
    en el archivo agenda.txt previo a borrar todo su contenido.
    Atrapa excepciones relacionadas al trabajo con archivos."""
    try:
        with open('agenda.txt', 'w', encoding="utf-8") as archivo:
            for contacto in agenda.values():
                archivo.write(f"Nombre: {contacto['Nombre']}\n")
                archivo.write(f"Apellido: {contacto['Apellido']}\n")
                archivo.write(f"Teléfono: {contacto['Teléfono']}\n\n")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except PermissionError:
        print("No se tienen permisos para acceder al archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def agregar(nombre, apellido, telefono):
    """Agrega un contacto nuevo al diccionario si es que no existe,
    si ya existe actualiza su telefono.
    Args:
        nombre (string): Nombre de la persona en la agenda.
        apellido (string): Apellido de la persona en la agenda.
        telefono (string): Número de telefono de la persona en la agenda."""
    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()
    for contacto in agenda.values():
        if contacto["Nombre"] == nombre and contacto["Apellido"] == apellido:
            contacto["Teléfono"] = telefono
            print("\n¡Contacto actualizado!\n")
            escribir_agenda()
            return
    agenda[str(len(agenda) + 1)] = {"Nombre": nombre, "Apellido": apellido, "Teléfono": telefono}
    print("\n¡Contacto agregado correctamente!\n")
    escribir_agenda()


def buscar(nombre, apellido):
    """Busca un contacto dentro de la agenda usando nombre y apellido.
    Si lo encuentra lo muestra en pantalla,
    si no lo encuentra muestra un mensaje en pantalla.
    Args:
        nombre (string): Nombre de la persona en la agenda.
        apellido (string): Apellido de la persona en la agenda."""
    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()
    for contacto in agenda.values():
        if contacto["Nombre"] == nombre and contacto["Apellido"] == apellido:
            print(f"\nContacto encontrado:\
                  \nNombre: {contacto['Nombre']}\
                  \nApellido: {contacto['Apellido']}\
                  \nTeléfono: {contacto['Teléfono']}\n")
            return
    print("\nContacto no encontrado.\n")


def importar():
    """Lee el contendio del archivo importar.txt, lo almacena en el
    diccionario de la agenda y llama a la funcion escribir_agenda
    para actualizar el archivo agenda.txt.
    Si el contacto a importar ya existe en la agenda, actualiza su teléfono.
    Atrapa excepciones relacionadas al trabajo con archivos."""
    try:
        with open('importar.txt', 'r', encoding="utf-8") as archivo:
            lineas_archivo = archivo.readlines()
        for linea in range(0, len(lineas_archivo), 4):
            nombre = lineas_archivo[linea].split(": ")[1].strip()
            apellido = lineas_archivo[linea+1].split(": ")[1].strip()
            telefono = lineas_archivo[linea+2].split(": ")[1].strip()
            agregar(nombre, apellido, telefono)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except PermissionError:
        print("No se tienen permisos para acceder al archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def imprimir_agenda():
    """Imprime en pantalla todos los contactos
    guardados en el diccionario agenda."""
    if not agenda:
        print("\n¡La agenda está vacía.!\n")
        return
    for contacto, datos in agenda.items():
        print(f"Contacto {contacto}:\
              \n  Nombre: {datos['Nombre']}\
              \n  Apellido: {datos['Apellido']}\
              \n  Teléfono: {datos['Teléfono']}\n")
