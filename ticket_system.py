import json #Importamos la libreria para manejar archivos JSON(guardar y leer datos)
import os #Importamos OS para verificar si el archivo de datos ya existe en la carpeta
from datetime import datetime #Importamos DATETIME para registrar la fecha y hora actual

#Definimos el nombre del archivo de texto donde se almacenara todo
ARCHIVO_DATOS = "tickets.json"

def cargar_tickets():
    """Esta funcion lee los tickets guardados para que no se pierdan al cerrar el programa"""
    if not os.path.exists(ARCHIVO_DATOS): #Si el archivo NO EXISTE TODAVIA
        return [] #Retorna una lista vacia para empezar de 0
    try:
        with open(ARCHIVO_DATOS, 'r') as f: #Abrimos el archivo en modo lectura ('r')
            return json.load(f) #Convertimos el texto del archivo JSON en una lista de Python
    except Exception: #Si hay un error al leer (archivo corrupto,por ejemplo)
        return [] #Devuelve una lista vacia por seguridad
    
def guardar_tickets(tickets):
    """Esta funcion toma la lista de tickets y la escribe en el archivo JSON."""
    with open(ARCHIVO_DATOS,'w') as f: #Abrimos el archivo en modo escritura ('w)
        #Guardamos la lista con una sangria de 4 espacios para que sea legible al abrir el archivo
        json.dump(tickets, f, indent=4)
        
def crear_ticket():
    """Funcion para pedir datos y registrar un nuevo problema"""
    tickets = cargar_tickets() #Primero Cargamos los tickets existentes
    
#Si no hay tickets, el ID es 1. Si hay,sumamos 1 al ID del ultimo ticket en la lista
    nuevo_id = 1 if not tickets else tickets[-1]['id'] + 1
    
    print("\n--- CREAR NUEVO TICKET ---")
    usuario = input("Nombre del usuario: ") #Pedimos el nombre del usuario
    problema = input ("Descripcion del problema: ") #Pedimos el fallo
    prioridad = input("Prioridad (Alta/Media/Baja): ").capitalize() #Pedimos prioridad y ponemos la primera letra en Mayuscula

        #Creamos un "diccionario" que represente el ticket individual
    nuevo_ticket = {
    "id":nuevo_id,
    "usuario":usuario,
    "problema":problema,
    "prioridad":prioridad,
    "estado": "Abierto", #Por defecto,todo ticket nuevo nace "Abierto"
    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Guardaamos fecha y hora actual
    }

    tickets.append(nuevo_ticket) #Agregamos el nuevo ticket a la lista general
    guardar_tickets(tickets) #Guardamos la lista actualizada en el archivo JSON
    print(f"¡Ticket #{nuevo_id} creado con exito!") #Confirmamos al usuario que el ticket se ha creado

def ver_tickets():
    """Muestra la lista de tickets organizada por importancia"""
    tickets = cargar_tickets() #Leemos los tickets del archivo
    if not tickets: #Si la lista esta vacia
        print("\nNo hay tickets registrados.") #Informamos al usuario
        return
    
    #Creamos una guia de orden: Alta vale 1(primera),Media 2,Baja 3.
    orden_prioridad = {"Alta": 1, "Media": 2, "Baja": 3}
    #Ordenamos la lista usando la guia anterior. SI NO reconoce la prioridad,le asigna 4(al final)
    tickets_ordenados = sorted(tickets, key=lambda x: orden_prioridad.get(x['prioridad'], 4))
    
    print("\n--- LISTA DE TICKETS (Ordenados por Prioridad) ---")
    for t in tickets_ordenados: #Recorremos cada ticket en la lista ordenada
        #Imprimimos los datos principales de forma elegante
        print(f"[{t['id']}] {t['usuario']} - {t['problema']} (Prioridad: {t['prioridad']}, Estado: {t['estado']}")
    
def buscar_ticket():
    """Busca un ticket especifico usando su ID"""
    try:
        id_buscar = int(input("\nIngrese el ID del ticket a buscar: ")) #Pedimos el ID y lo convertimos a numero(int)
        tickets = cargar_tickets() #Cargamos los datos
        
        for t in tickets: #Revisamos cada ticket
            if t['id']== id_buscar: #Si el ID coincide con el que buscamos...
                print(f"\nTicket Encontrado: \nID: {t['id']}\nUsuario: {t['usuario']}\nProblema: {t['problema']}\nPrioridad: {t['prioridad']}\nEstado: {t['estado']}") 
                return #Salimos de la funcion porque ya lo encontramos
            print("No se encontro ningun ticket con ese ID.")
    except ValueError: #Si el usuario escribe letras en vez de un numero de ID
            print("ID invalido. Por favor ingrese un numero.")
            
def cambiar_estado():
    """Permite al tecnico actualizar si un ticket sigue abierto o ya se cerró"""
    try:
        id_ticket = int(input("\nID del ticket a modificar: ")) #Pedimos el ID
        tickets = cargar_tickets() #Cargamos los datos
        for t in tickets: #Buscamos el ticket
            if t['id'] == id_ticket:
                print(f"Estado actual: {t['estado']}")
                #Pedimos el nuevo estado
                nuevo_estado = input("Nuevo estado (Abierto/En proeso/Cerrado): ")
                t['estado'] = nuevo_estado #Actualizamos el valor del diccionario
                guardar_tickets(tickets) #Guardamos los cambios en el archivo
                print("¡Estado actualizado con exito!")
                return
            print("Ticket no encontrado.")
    except ValueError: #Si el usuario escribe letras en vez de un numero de ID
        print("Error: Entrada no valida")

def mostrar_menu():
    """Este es el motor del programa, el menu que se repite siempre"""
    while True: #Bucle infinito para que el programa no se cierre solo
        print("\n--- SISTEMA DE TICKETS ---")
        print("1. Crear nuevo ticket por ID")
        print("2. Ver todos los tickets")
        print("3. Buscar ticket")
        print("4. Cambiar estado de ticket")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion (1-5): ") #Leemos la ocpion del usuario
        
        if opcion == '1':
            crear_ticket() #Llamamos a la funcion para crear un nuevo ticket
        elif opcion == '2':
            ver_tickets() #Llamamos a la funcion para mostrar los tickets
        elif opcion == '3':
            buscar_ticket() #Llamamos a la funcion para buscar un ticket
        elif opcion == '4':
            cambiar_estado() #Llamamos a la funcion para cambiar el estado de un ticket
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion valida.") #Por si el usuario presiona otra tecla
            
#Esta linea asegura que el programa solo arranque si ejecutas este archivo directamente
if __name__ == "__main__":
    mostrar_menu() #Llamamos a la funcion del menu para iniciar el programa