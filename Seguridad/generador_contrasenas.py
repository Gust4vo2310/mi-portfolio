#Importaciones no son necesarias para este script de lectura.

#----Paso 1: Abrir el archivo de texto para leerlo----
#Usamos "With open ()" nuevamente, pero esta vez con "r" para "read (leer)"
#Asegurarse que ese script este en  la misma carpeta que "credenciales.txt"
try:
    with open("credenciales.txt" , "r") as archivo_de_lectura:
        print("----- Credenciales guardadas -----")
        
        #----Paso 2: Leer el archivo linea por linea----
        #El bucle "for" lee cada linea del archivo de forma secuencial
        for linea in archivo_de_lectura:
            #----Paso3: Procesar cada linea----
            #"strip()" elimina el salto de linea (\n) al final de cada linea
            linea_limpia = linea.strip()
            
            #"split(":")" divide la cadena en dos partes usando el ":" como separador.
            #Esto crea una lista: ["usuario",contraseña"].
            partes = linea_limpia.split(", ")
            
            #La primera parte es el nombre de usuario.
            usuario = partes[0]
            #La segunda parte es la contraseña.
            contrasena = partes[1]
            
            #----Paso 4: Imprimir los datos----
            print(f"{usuario}, {contrasena}")

except FileNotFoundError:
     #si el archivo no existe, mostramos un mensaje de error
    print("ERROR: El archivo 'credenciales.txt' no fue encontrado.")
    print("Asegurate de que esta en la misma carpeta que este script.")
    
print("----------------------------")
print("Lectura de archivo finalizada.")    
