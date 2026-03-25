import speech_recognition as sr # Cargamos la librería que reconoce la voz #
from pydub import AudioSegment # Cargamos la herramienta para convertir audios #
import os # Cargamos funciones para borrar archivos temporales #

# --- CONFIGURACIÓN ---
# Si no tenés un audio real todavía, podés poner cualquier nombre acá #
ARCHIVO_WHATSAPP = "mi_audio.ogg" 
ARCHIVO_PARA_PROCESAR = "temp_audio.wav"

def procesar_audio():
    print("--- INICIANDO PROCESO DE TRANSCRIPCIÓN ---")
    
    #Verificamos si el archivo existe antes de empezar #
    if not os.path.exists(ARCHIVO_WHATSAPP):
        print(f"❌ ERROR: No encontré el archivo '{ARCHIVO_WHATSAPP}' en esta carpeta.")
        print("💡 Tip: Arrastrá un audio de WhatsApp a esta carpeta y ponele ese nombre.")
        return

    try:
        #1. CONVERSIÓN: WhatsApp (.ogg) -> Estándar (.wav) #
        print("1. Convirtiendo el audio de WhatsApp...")
        audio = AudioSegment.from_file(ARCHIVO_WHATSAPP)
        audio.export(ARCHIVO_PARA_PROCESAR, format="wav")
        
        # 2. RECONOCIMIENTO: El "oído" de Python #
        reconocedor = sr.Recognizer()
        with sr.AudioFile(ARCHIVO_PARA_PROCESAR) as fuente:
            print("2. Analizando la voz (usando Google Engine)...")
            # Ajustamos por si hay ruido de fondo #
            reconocedor.adjust_for_ambient_noise(fuente)
            datos_audio = reconocedor.record(fuente)
            
            # 3. TRADUCCIÓN A TEXTO: En español argentino #
            texto = reconocedor.recognize_google(datos_audio, language='es-AR')
            
            print("\n--- ✅ RESULTADO FINAL ---")
            print(f"Mensaje detectado: {texto}")
            
            # 4. GUARDADO: Creamos un archivo .txt con el resultado #
            with open("transcripcion_final.txt", "w", encoding="utf-8") as f:
                f.write(texto)
            print("\nResultado guardado en 'transcripcion_final.txt'")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

    finally:
        # 5. LIMPIEZA: Borramos el archivo temporal .wav #
        if os.path.exists(ARCHIVO_PARA_PROCESAR):
            os.remove(ARCHIVO_PARA_PROCESAR)
            print("--- Proceso terminado y limpieza realizada ---")

# Ejecutamos la función #
if __name__ == "__main__":
    procesar_audio()