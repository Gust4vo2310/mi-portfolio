import random

# Lista de palabras para el juego
palabras = ["ahorcado", "programacion", "computadora", "codigo", "juego", "python"]

# Dibujos del ahorcado en una lista. El índice 0 es el inicial.
ahorcado_dibujos = [
    """
       ------
       |    |
       |
       |
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    -------
    """
]

# 1. Función para mostrar el estado actual del juego
def mostrar_estado(palabra, letras_adivinadas, intentos):
    """Muestra la palabra con guiones, el dibujo del ahorcado y los intentos restantes."""
    
    # Muestra el dibujo del ahorcado según los intentos fallidos
    intentos_fallidos = 6 - intentos
    print(ahorcado_dibujos[intentos_fallidos])
    
    # Muestra la palabra con guiones bajos para las letras no adivinadas
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    print(f"\nPalabra: {palabra_mostrada}")
    print(f"Te quedan {intentos} intentos.")
    print(f"Letras adivinadas: {' '.join(letras_adivinadas)}") # Muestra las letras que ya se adivinaron

# 2. Función principal del juego
def jugar_ahorcado():
    """Ejecuta toda la lógica del juego del ahorcado."""
    
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos_restantes = 6
    juego_terminado = False
    
    while not juego_terminado:
        mostrar_estado(palabra_secreta, letras_adivinadas, intentos_restantes)
        
        # 3. Opción para adivinar la palabra completa
        opcion = input("\n¿Quieres adivinar la palabra o una letra? (p/l): ").lower()
        
        if opcion == "p":
            adivinanza = input("Ingresa la palabra completa: ").lower()
            if adivinanza == palabra_secreta:
                print(f"\n¡Felicidades! Has adivinado la palabra: '{palabra_secreta}'")
                juego_terminado = True
            else:
                print("Incorrecto. ¡Sigue intentando!")
                intentos_restantes = 0 # El jugador pierde si la adivinanza es incorrecta
                
        elif opcion == "l":
            letra = input("Ingresa una letra: ").lower()
            
            if letra in letras_adivinadas:
                print("Ya adivinaste esa letra. ¡Intenta con otra!")
                continue
            
            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, ingresa solo una letra válida.")
                continue
                
            letras_adivinadas.append(letra)
            
            if letra not in palabra_secreta:
                intentos_restantes -= 1
                print(f"Lo siento, la letra '{letra}' no está en la palabra.")
        else:
            print("Opción no válida. Por favor, elige 'p' para palabra o 'l' para letra.")
            continue
            
        # 4. Comprobar si el jugador ganó o perdió
        palabra_completa = all(letra in letras_adivinadas for letra in palabra_secreta)
        if palabra_completa:
            print(f"\n¡Felicidades! Has adivinado la palabra: '{palabra_secreta}'")
            juego_terminado = True
        
        if intentos_restantes <= 0:
            mostrar_estado(palabra_secreta, letras_adivinadas, intentos_restantes) # Mostrar el ahorcado completo
            print(f"\n¡Oh no! Te quedaste sin intentos. La palabra era: '{palabra_secreta}'")
            juego_terminado = True
            
# Inicia el juego
jugar_ahorcado()
