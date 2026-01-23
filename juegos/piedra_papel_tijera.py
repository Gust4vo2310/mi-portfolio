#Importampos la libreria 'random' para que la computadora pueda elegir su jugada favorita
import random 

#Definimos una lista con las opciones del juego.
opciones = ["piedra", "papel", "tijera"]

#Usamos un bucle "while true" para que el juego se repita hasta que el usuario decida salir. 
while True:
    #Le pedimos al usuario que elija su jugada.
    eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    
    #Si el usuario escribe 'salir',terminamos el juego.
    if eleccion_usuario == 'salir':
        print('Gracias por jugar!! Hasta la proxima!!')
        break
    
    #Verificamos si la eleccion del usuario es valida.
    if eleccion_usuario not in opciones:
        print("Opcion no valida. Por favor, elegir piedra, papel o tijera.")
        continue #Vuelve al inicio del bucle
    
    #La computadora elige su jugada de forma aleatoria
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligio: {eleccion_computadora}")
    
    #Ahora comparamos las elecciones para determinar el gaanador
    if eleccion_usuario == eleccion_computadora:
       #Si las jugadas son iguales, es un empate.
       print("¡¡¡Es un empate!!!")
       
    elif(eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
        (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
    #Usamos or para cambiar las condiciones de victoria del usuario.
        print("¡¡¡Vos ganas!!!")
        
    else:
        #Si no es un empate y el usuario no gano, la computadora gana.
        print("¡¡¡La computadora gana!!!") 
