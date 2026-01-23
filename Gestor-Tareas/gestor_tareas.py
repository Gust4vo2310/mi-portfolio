#Importamos la libreria 'os' para trabajar con archivos en el sistema operativo.
import os 

#Definimos el nombre del archivo donde guardaremos las tareas.
NOMBRE_ARCHIVO = "tareas.txt"

def cargar_tareas():
    """ Carga las tareas desde el archivo de texto."""
    tareas = []
    
    #Usamos 'os.path.exists()' para verificar si el archivo ya existe.
    if os.path.exists(NOMBRE_ARCHIVO):
        #'with open (...)' se usa para abrir y cerrar el archivo automaticamente
        with open (NOMBRE_ARCHIVO, "r") as archivo:
            for linea in archivo:
                #La funcion '.strip()' elimina los espacios y saltos de linea al final de cada linea.
                tareas.append(linea.strip())
    return tareas

def guardar_tareas(tareas):
    """Guarda las tareas en el archivo de texto"""
    #El modo 'w' de 'open' escribe en el archivo. Si el archivo existe,lo sobreescribe.
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for tarea in tareas:
            #Escribimos cada tarea seguida de un salto de linea.
            archivo.write(tarea + "\n")
            
def mostrar_menu():
    """Mostrar el menu de opciones."""
    print("\n--- Gestor de Tareas ---")
    print("1) Agregar una tarea")
    print("2) Ver todas las tareas")
    print("3) Eliminar una tarea")
    print("4) Salir")
    
def agregar_tareas(tareas):
    """Permite al usuario agregrar una nueva tarea."""
    nueva_tarea = input("Escribir la nueva tarea: ")
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("Tarea agregada con exito.")
    
def ver_tareas(tareas):
    """Muestra la lista de tareas."""
    if not tareas:
        print("No tenes tareas pendientes.")
    else:
        print("\n--- Tu lista de Tareas ---")
        #'enumerate' nos da el indice y la tarea al mismo tiempo.
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
            
def eliminar_tarea(tareas):
    """Permite al usuario eliminar una tarea por su numero."""
    ver_tareas(tareas)
    if tareas:
        try:
            num_a_eliminar =int(input("Ingresa el numero de la tarea a eliminar: "))
            indice = num_a_eliminar - 1
            if 0 <= indice <len(tareas):
                tarea_eliminada = tareas.pop(indice)
                guardar_tareas(tareas)
                print(f"Tarea '{tarea_eliminada}' eliminada con exito.")
            else:
                print("Numero de tarea no valido.")
        except ValueError:
            print("Entrada no valida. Por favor, ingresar un numero.")
            
# ---- PROGRAMA PRINCIPAL ----
#Cargamos las tareas guardadas al iniciar el programa.
lista_de_tareas = cargar_tareas()

while True:
    mostrar_menu()
    opcion = input("Elegir una opcion (1, 2, 3, o 4): ")
    
    if opcion == '1':
        agregar_tareas(lista_de_tareas)
    elif opcion == '2':
        ver_tareas(lista_de_tareas)
    elif opcion == '3':
        eliminar_tarea(lista_de_tareas)
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opcion no valida. Por favor, elige 1, 2, 3 o 4.")
