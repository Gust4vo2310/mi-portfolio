import speech_recognition as sr # Cargamos el motor de voz #
import pydub # Cargamos el motor de audio #
from pydub.utils import which # Importamos la herramienta para buscar programas #

def verificar_todo():
    print("--- CHEQUEO DE SISTEMA ---")
    
    # 1. Verificamos Python y la librería de voz
    print(f"Librería de voz: instalada (v{sr.__version__})") #
    
    # 2. Verificamos si Python encuentra a FFmpeg (lo que instalamos en C:)
    ruta_ffmpeg = which("ffmpeg") # Busca el ejecutable en tu computadora #
    
    if ruta_ffmpeg:
        print(f"FFmpeg: ENCONTRADO en {ruta_ffmpeg} ✅") #
        print("\n¡Todo listo, Gustavo! Tu entorno está perfecto.") #
    else:
        print("FFmpeg: NO ENCONTRADO ❌") #
        print("\nAtención: El código de WhatsApp no funcionará sin FFmpeg en el Path.") #

# Ejecutamos la verificación
verificar_todo()