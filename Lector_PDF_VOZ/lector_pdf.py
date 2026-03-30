import pyttsx3
import PyPDF2

# 1. Configuramos el motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 140) 

# 2. Abrimos el archivo PDF
archivo_pdf = open('documento.pdf', 'rb')
lector = PyPDF2.PdfReader(archivo_pdf)

# 3. Extraemos el texto
texto_completo = ""
for pagina in lector.pages:
    texto_completo += pagina.extract_text()

# --- Limpieza de caracteres ---
# Reemplazamos la barra "/" por un espacio para que no diga "diagonal"
texto_completo = texto_completo.replace("/", " ")
# También podemos quitar otros símbolos si te molestan (ejemplo: guiones o asteriscos)
texto_completo = texto_completo.replace("*", "")
# -------------------------------------------

# 4. Buscamos voces en español
todas_las_voces = engine.getProperty('voices')
voces_espanol = [v for v in todas_las_voces if "spanish" in v.name.lower() or "helena" in v.name.lower()]

# 5. Selección de voz
if len(voces_espanol) > 0:
    print(f"Voces detectadas: {len(voces_espanol)}")
    seleccion = input("Escribe 0 (Hombre) o 1 (Mujer): ")
    if seleccion == "1" and len(voces_espanol) > 1:
        engine.setProperty('voice', voces_espanol[1].id)
    else:
        engine.setProperty('voice', voces_espanol[0].id)

# 6. Lectura 
if texto_completo.strip():
    print("Leyendo...")
    engine.say(texto_completo)
    engine.runAndWait()
else:
    print("¡Atención! El PDF está vacío o es una imagen/escaneo y no puedo leerlo.")

archivo_pdf.close()