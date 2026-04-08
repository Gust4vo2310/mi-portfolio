import PyPDF2
import pyttsx3
import keyboard
import sys
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def hablar_frase_segura(texto):
    """Crea un motor nuevo solo para esta frase y lo cierra al terminar"""
    try:
        #Chequeo de controles antes de cada mini-motor
        if keyboard.is_pressed('c'): 
            print("\nCERRANDOOO,NOS VEMOS LA PROXIMA!")
            sys.exit()
        
        if keyboard.is_pressed('p'):
            print("|| PAUSA - Tocá 'R' para seguir")
            keyboard.wait('r')

        print(f"Leyendo: {texto}")
        
        #configuracion
        m = pyttsx3.init()
        voces = m.getProperty('voices')
        m.setProperty('voice', voces[2].id) #voces 2 porque es latinoamericana coomo vimos en prueba_voz
        m.setProperty('rate', 155)
        
        m.say(texto)
        m.runAndWait()
        
        #DESTRUCCIÓN DEL MOTOR (Para que no se trabe la memoria)
        m.stop()
        del m 
        
    except Exception as e:
        print(f"Reintentando frase...")
        time.sleep(0.2)

def ejecutar():
    Tk().withdraw()
    ruta = askopenfilename(title="Elegí tu PDF", filetypes=[("Archivos PDF", "*.pdf")])
    if not ruta: return

    try:
        lector = PyPDF2.PdfReader(ruta)
        print(">>> ESCUCHA TU PDF (C para cerrar, P para pausar)")

        for pagina in lector.pages:
            texto = pagina.extract_text()
            if not texto: continue
            
            #Limpiamos y dividimos por puntos
            oraciones = texto.replace('\n', ' ').split('.')

            for oracion in oraciones:
                frase = oracion.strip()
                if len(frase) > 5:
                    hablar_frase_segura(frase)
                    #Un mini respiro y sigue
                    time.sleep(0.2)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()
