import random
#Pedimos al usuario que elija el rango de números y la cantidad de intentos
print("--- configura tu juego ---")

#Usamos "int(input())" para asegurarnos de que el valor ingresado sea un número entero
limite_inferior = int(input("Ingresa el limite inferior para el rango de numeros: "))
limite_superior = int(input("Ingresa el limite superior para el rango de numeros: "))
intentos_maximos = int(input("¿Cuantos intentos queres tener?: "))
print("-" * 25)

#El programa elige un numero secreto dentro del rango definido por el usuario
#la funcion "random.randint" genera un numero entero aleatorio entre los dos limites
numero_secreto = random.randint(limite_inferior, limite_superior)

print(f"Estoy pensando en un numero entre {limite_inferior} y {limite_superior}.")
print(f"tenes {intentos_maximos} intentos para adivinarlo.")

#usamos bucle "for" para limitar el numero de intentos
#el bucle se ejecutara "intentos_maximos" veces
for intento in range(1, intentos_maximos + 1):
    try:
        suposicion = int(input(f"Intento {intento}: ¿Cual es tu suposicion?: "))
        if suposicion < numero_secreto:
            print("El numero es mas alto.")
        elif suposicion > numero_secreto:
            print("El numero es mas bajo.")
        else:
            #Si la suposicion es correcta, felicitamos al usuario y salimos del bucle
            print(f"¡Felicidades! Adivinaste el numero {numero_secreto} en {intento} intentos.")
            break #el break termina el bucle
    except ValueError:
        print("Por favor, ingresa un numero valido.")
else:
    #el bloque "else" se ejecuta solo si el bucle "for" termina sin usar "break"
    print(f"Se te terminaron los intentos. El numero era {numero_secreto}.")
