def calculadora():
    print("--- Calculadora Profesional (Python) ---")
    print("Escribe 'salir' para finalizar")
    
    while True:
        try:
            operacion = input("\nElige operación (+, -, *, /) o 'salir': ").lower()
            
            if operacion == 'salir':
                print("Cerrando sistema...")
                break
                
            if operacion not in ['+', '-', '*', '/']:
                print("Operación no válida. Intenta de nuevo.")
                continue

            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                resultado = num1 / num2

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: Por favor, ingresa solo números válidos.")

calculadora()
