#Importamos librerias necesarias
#Pandas es para manejar los datos en un DataFrame.
# OS nos ayuda a verificar si el archivo existe

import pandas as pd
import os

#---- PARTE 1: Recopilar los datos y crear el archivo CSV----

#Preguntamos al usuario los datos para una persona. 
print("Vamos a crear un registro de datos simple.")
nombre = input("Por favor, introducir el nombre: ")
edad = int(input("Introducir edad: "))
ciudad = input("Introduce la ciudad: ")

#Creamos un diccionario con los datos.
#Diccionario  es una coleccion de pares clave-valor, ideal para organizar datos.
datos = {'Nombre': [nombre],
         'Edad': [edad],
         'Ciudad': [ciudad]}

#Convertimos el diccionario a un DataFrame de Pandas.
#DataFrame es como una tabla de excel dentro de python
df = pd.DataFrame(datos)

#Definimos el nombre del archivo.
nombre_archivo = "registro_personas.csv"

#Verificamos si el archivo ya existe.
if os.path.exists(nombre_archivo):
    #Si el archivo existe, agregamos la nueva fila al final
    #mode='a' significa "añadir"(append), y header=False evita duplicar encabezados
    df.to_csv(nombre_archivo, mode = 'a' , index=False , header=False)
    print(f"\nDatos de {nombre} añadidos al archivo existente.")
else:
    #Si el archivo no existe, lo creamos y escribimos los encabezados.
    #index=False evita escribir una columna de numeros no deseada.
    df.to_csv(nombre_archivo, index=False)
    print(f"\nArchivo '{nombre_archivo}' creado con los datos de {nombre}.")
    
#---- PARTE2: Leer y analizar los datos con Pandas ----

#Volvemos a leer todo el archivo CSV.
#Esto es necesario para asegurarnos de que el DataFrame contenga todos los registros
df_completo = pd.read_csv(nombre_archivo)

#Mostramos el contenido completo del DataFrame.
print("\n--- Todos los registros del archivo ---")
print(df_completo)


#Calculamos y mostramos la edad promedio
#Seleccionamos la columna "Edad" y usamos el metodo .mean()  para obtener el promedio
promedio_edad = df_completo['Edad'].mean()
print("\n--- Analis de datos ---")
print(f"La edad promedio de todas las personas registradas es: {promedio_edad:.2f} años.")
