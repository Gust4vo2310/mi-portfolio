# Saludamos al usuario al iniciar el chat
print("🤖 ¡Hola! Bienvenido al chat de Los Programadores FC ⚽")

# Iniciamos un bucle infinito (while True) para que el chat siga funcionando
# hasta que el usuario decida salir.
while True:
    
    # Mostramos el menú de opciones al usuario
    print("\n--- MENÚ PRINCIPAL ---")
    print("¿En qué podemos ayudarte?")
    print("1. Ver información del próximo partido.")
    print("2. Consultar cómo hacerse socio.")
    print("3. Ver la tienda del club.")
    print("4. Salir del chat.")
    
    # Pedimos al usuario que ingrese su elección usando input()
    # El input() siempre nos da un 'string' (texto)
    opcion = input("Escribe el número de la opción (1, 2, 3 o 4): ")
    
    # Usamos condicionales (if/elif/else) para revisar qué número eligió el usuario
    
    # Si la opción es "1"
    if opcion == "1":
        print("\n---------------------------------")
        print("--- 📅 PRÓXIMO PARTIDO ---")
        print("¡Jugamos la final del torneo!")
        print("Programadores FC vs. Los Compiladores")
        print("Día: Este domingo a las 17:00 hs.")
        print("Estadio: El Código Arena")
        print("---------------------------------")
    
    # Si no fue "1", pero fue "2" (elif = else if)
    elif opcion == "2":
        print("\n---------------------------------")
        print("--- 💳 HACERSE SOCIO ---")
        print("¡Gracias por tu interés en el club!")
        print("Para asociarte, visita nuestra web: www.programadoresfc.com/socios")
        print("¡Te esperamos!")
        print("---------------------------------")
    
    # Si no fue "1" ni "2", pero fue "3"
    elif opcion == "3":
        print("\n---------------------------------")
        print("--- 👕 TIENDA OFICIAL ---")
        print("¡Tenemos la nueva camiseta titular!")
        print("Visita www.programadoresfc.com/tienda para verla.")
        print("---------------------------------")
    
    # Si no fue ninguna de las anteriores, pero fue "4"
    elif opcion == "4":
        print("\n---------------------------------")
        print("¡Gracias por chatear con nosotros! ¡Vamos Programadores FC! 🏆")
        print("---------------------------------")
        
        # Usamos 'break' para romper el bucle (while True) y terminar el programa
        break
    
    # Si no escribió "1", "2", "3" ni "4"
    else:
        print("\n---------------------------------")
        print("❌ Opción no válida.")
        print("Por favor, asegúrate de escribir solo el número (por ejemplo: 1).")
        print("---------------------------------")
