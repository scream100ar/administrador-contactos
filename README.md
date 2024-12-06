# Administrador de Contactos

## Descripción
El **Administrador de Contactos** es una aplicación en Python diseñada para gestionar contactos personales. Permite realizar operaciones como buscar, agregar, actualizar, importar y listar contactos, almacenándolos de manera persistente en un archivo de texto.

---

## Características
- **Búsqueda de contactos:** Encuentra contactos por nombre y apellido.
- **Agregar o actualizar contactos:** Agrega nuevos contactos o actualiza los existentes si se detectan duplicados.
- **Importar contactos desde un archivo:** Integra contactos masivamente desde un archivo externo `importar.txt`.
- **Listar todos los contactos:** Muestra de manera ordenada todos los contactos almacenados en la agenda.
- **Persistencia de datos:** Almacena los contactos en un archivo `agenda.txt` para conservar la información entre sesiones.

---

## Requisitos
- Python 3.8 o superior.
- Archivo `agenda.txt` (opcional, se generará automáticamente si no existe).
- Archivo `importar.txt` (opcional, para importar contactos).

---

## Instalación
1. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando:
   ```bash
   python --version
   ```
Si lo desea puede ejecutar la instacion en un entorno virtual, sino puede saltar directamente al punto 7.
En caso de querer instalarlo de forma aislada en un entorno virtual:

2. Asegúrate de tener venv instalado en tu ejecucion de Python. Para verificarlo:
   ```bash
   python -m venv --version
   ```
3. Cree un entorno virtual con venv (Windows):
   ```bash
   python -m venv ./venv 
   ```
4. Cree un entorno virtual con venv (Linux):
   ```bash
   python3 -m venv ./venv 
   ```
5. Active el entorno virtual (Windows):
   ```bash
   .\venv\Scripts\activate
   ```
6. Active el entorno virtual (Linux):
   ```bash
   source myenv/bin/activate
   ```
7. Clona este repositorio o descarga los archivos manualmente.
   ```bash
   git clone https://github.com/scream100ar/administrador-contactos
   cd administrador-contactos
   ```
6. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando:
   ```bash
   python --version
   ```
7. Ejecuta el archivo principal (Windows):
   ```bash
   python main.py
   ```
8. Ejecuta el archivo principal (Linux):
   ```bash
   python3 main.py
   ```

---

## Uso
Al iniciar el programa, se mostrará un menú con las siguientes opciones:

1. **Buscar una persona:** Solicita el nombre y apellido de la persona para buscar en la agenda.
2. **Agregar o actualizar los datos de una persona:** Solicita nombre, apellido y teléfono. Si el contacto ya existe, actualiza su información.
3. **Importar contactos desde un archivo:** Importa contactos desde `importar.txt`. Cada contacto debe estar en el formato:
   ```
   Nombre: Julieta
   Apellido: Aguirre
   Teléfono: +54 9 11 5598-7890
   ```
4. **Imprimir toda la agenda:** Muestra todos los contactos en pantalla.

Cualquier otra entrada cerrará el programa.

---

## Organización del Proyecto

### Archivos Principales
- `main.py`: Contiene la lógica principal y el menú interactivo.
- `funciones.py`: Contiene las funciones auxiliares para realizar las operaciones de la agenda.

### Archivos de Datos
- `agenda.txt`: Archivo de almacenamiento persistente de contactos.
- `importar.txt`: Archivo opcional para importar contactos masivamente.

---

## Ejemplo de Uso
### Ejemplo 1: Agregar un nuevo contacto
```bash
Administrador de Contactos
Elija una opción:
1 - Buscar una persona
2 - Agregar o actualizar los datos de una persona
3 - Importar contactos desde un archivo
4 - Imprimir toda la agenda
Cualquier otra tecla para salir
Ingrese su elección: 2

Ingrese el nombre: Rodrigo
Ingrese el apellido: Molina
Ingrese el teléfono: +54 9 11 5574-5678

¡Contacto agregado correctamente!
```

### Ejemplo 2: Buscar un contacto
```bash
Ingrese su elección: 1

Buscar una persona en la agenda:
Ingrese el nombre: Rodrigo
Ingrese el apellido: Molina

Contacto encontrado:
Nombre: Rodrigo
Apellido: Molina
Teléfono: +54 9 11 5568-9012
```

---

## Contribuciones
Para colaborar en el proyecto por favor:
1. Haz un fork de este repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b nombre-de-la-rama
   ```
3. Envía un pull request detallando las mejoras realizadas.

---


## Autor
Desarrollado por [Claudio Barrientos](https://github.com/scream100ar).
