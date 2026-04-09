import streamlit as st 
import PyPDF2
import edge_tts
import asyncio
import os

#CONFIGURACION DE LA PAGINA
st.set_page_config(page_title="Escucha tu PDF", page_icon= "🎧")

st.title("🎧Escucha tu PDF (Version Web)")
st.subheader("Subi tu archivo y transformalo en audio al instante")

#1)SUBIDA DE ARCHIVO
uploaded_file = st.file_uploader("Elegi un archivo PDF", type ="pdf")

#FUNCION PARA CONVERTIR TEXTO A VOZ (necesaria para edge-tts)
async def generar_audio(texto, archivo_salida):
    #Usamos una voz en español ARGENTINA (Tomas o Elena)
    communicate = edge_tts.Communicate(texto,"es-AR-TomasNeural")
    await communicate.save(archivo_salida)
    
if uploaded_file is not None:
    #2) EXTRAER TEXTO
    with st.spinner("Leyendo el PDF..."):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        texto_completo = ""
        for page in pdf_reader.pages:
            texto_completo += page.extract_text()
    
    if texto_completo.strip():
        st.success("PDF leido correctamente")
        
        #3)BOTON PARA CONVERTIR
        if st.button("Convertir audio"):
            archivo_audio = "lectura.mp3"
            
            with st.spinner("Generando audio...esto puede tardar unos segundos"):
                #EJEUTAR LA FUNCION DE AUDIO
                asyncio.run(generar_audio(texto_completo,archivo_audio))
                
                #4)REPRODUCTOR DE AUDIO
                st.audio(archivo_audio, format="audio/mp3")
                
                #BOTON DE DESCARGA
                with open (archivo_audio, "rb") as f:
                    st.download_button("Descargar MP3", f, file_name = "mi lectura.mp3")
        else:
            st.error("No se encontro texto en este PDF.")
            
st.info("Nota: Esta version web genera un archivo MP3 completo para que lo escuches o descargues...")
        