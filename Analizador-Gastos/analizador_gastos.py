# Importamos la librería para graficar (debes instalarla con: pip install matplotlib)
import matplotlib.pyplot as plt

# Definimos una función sencilla para recolectar datos
def analizar_gastos():
    print("--- Bienvenido a tu Analizador de Gastos ---")
    
    # Pedimos al usuario que ingrese los montos por categoria
    # Usamos float() para permitir números con decimales
    comida = float(input("Ingrese gasto en Comida: "))
    alquiler = float(input("Ingrese gasto en Alquiler: "))
    ocio = float(input("Ingrese gasto en Ocio: "))

    # Guardamos las categorías y los montos en listas
    categorias = ['Comida', 'Alquiler', 'Ocio']
    montos = [comida, alquiler, ocio]

    # Creamos el gráfico de torta
    # 'autopct' sirve para mostrar el porcentaje automáticamente en el dibujo
    plt.pie(montos, labels=categorias, autopct='%1.1f%%', startangle=140)

    # Añadimos un título al gráfico
    plt.title("Distribución de Gastos Mensuales")

    # Mostramos el gráfico en una ventana nueva
    print("Generando gráfico...")
    plt.show()

# Ejecutamos la función
analizar_gastos()
