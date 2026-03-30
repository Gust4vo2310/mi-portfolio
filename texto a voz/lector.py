from gtts import gTTS
import os

# 1. Nombre del archivo que creaste en el Bloc de Notas
# ¡Fijate que coincida letra por letra!
nombre_entrada = "mi_texto.txt"

try:
    # 2. Intentamos abrir el archivo
    with open(nombre_entrada, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    # 3. Si lo encuentra, lo convierte a audio
    print("Leyendo el archivo y convirtiendo a audio...")
    voz = gTTS(text=contenido, lang='es', slow=False)

    # 4. Guardamos el audio
    nombre_salida = "audio_resultado.mp3"
    voz.save(nombre_salida)

    # 5. Lo reproduce automáticamente
    print("¡Listo! Reproduciendo...")
    os.system(f"start {nombre_salida}")

except FileNotFoundError:
    # Este mensaje sale si el archivo no está en la misma carpeta
    print(f"¡Ups! No encuentro el archivo '{nombre_entrada}'.")
    print("Recomendación: Guardá el .py y el .txt en la misma carpeta (ej. Escritorio).")
