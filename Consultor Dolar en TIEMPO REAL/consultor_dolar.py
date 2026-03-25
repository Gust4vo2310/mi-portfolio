import requests # Libreria para conectar a internet

def consultar_criptoya(): # usando el servidor de CriptoYa
    # Usamos una URL que devuelve muchos dolares juntos (Oficial, Blue, MEP)
    url = "https://criptoya.com/api/dolar" 

    try: # Bloque de prueba
        # Pedimos los datos a CriptoYa
        respuesta = requests.get(url)
        
        # Convertimos la respuesta a formato Python (JSON)
        datos = respuesta.json()

        # En esta API los datos estan organizados diferente, los extraemos asi:
        v_oficial = datos["oficial"]["price"] # Precio del oficial
        v_blue = datos["blue"]["ask"]         # Precio venta del blue
        v_mep = datos["mep"]["al30"]["ci"]["price"] # Precio del MEP (AL30)

        while True: # Menu de usuario
            print("\n================================")
            print("   MONITOR DE DOLARES (FUENTE 2)")
            print("================================")
            print(f"1. Ver Precios Actuales")
            print(f"2. Calcular Conversion")
            print(f"3. Salir")

            opcion = input("\nSelecciona una opcion: ")

            if opcion == "1":
                print(f"\nOficial: ${v_oficial}")
                print(f"Blue:    ${v_blue}")
                print(f"MEP:     ${v_mep}")
            
            elif opcion == "2":
                pesos = float(input("\n¿Cuantos pesos tienes?: "))
                print(f"Al Blue tendrias: U$D {pesos/v_blue:.2f}")
                print(f"Al MEP tendrias:  U$D {pesos/v_mep:.2f}")
            
            elif opcion == "3":
                print("¡Chau! Proceso finalizado.")
                break
            else:
                print("Opcion incorrecta.")

    except Exception as e:
        # Si esto falla, nos va a decir exactamente que paso
        print(f"\nError al conectar con CriptoYa: {e}")

# Ejecutamos la nueva funcion
consultar_criptoya()