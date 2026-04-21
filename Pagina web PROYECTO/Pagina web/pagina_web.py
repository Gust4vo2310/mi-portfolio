# Importamos Flask y herramientas necesarias para el panel de noticias
from flask import Flask, render_template, url_for, request, redirect
import os
import json

# Crear la app
app = Flask(__name__)

# Configuración para las noticias (carpeta para fotos y archivo de datos)
UPLOAD_FOLDER = 'static/uploads'
NOTICIAS_FILE = 'noticias.json'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Nos aseguramos de que la carpeta de fotos exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Función para leer las noticias guardadas
def obtener_noticias():
    if os.path.exists(NOTICIAS_FILE):
        with open(NOTICIAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# --- TUS RUTAS ORIGINALES (INTACTAS) ---

@app.route('/')
def inicio():
    # Ahora le pasamos las noticias al index para que el carrusel las muestre
    lista_noticias = obtener_noticias()
    return render_template('index.html', noticias=lista_noticias)

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/primera')
def primera():
    return render_template('primera.html')

@app.route('/senior')
def senior():
    return render_template('senior.html')

@app.route('/cuarta')
def cuarta():
    return render_template('cuarta.html')

@app.route('/quinta')
def quinta():
    return render_template('quinta.html')

@app.route('/sexta')
def sexta():
    return render_template('sexta.html')

@app.route('/femenino')
def femenino():
    return render_template('femenino.html')

@app.route('/fixture')
def fixture():
    return render_template('fixture.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html', fecha=1)

@app.route('/resultados/<int:numero_fecha>')
def resultados_fecha(numero_fecha):
    return render_template('resultados.html', fecha=numero_fecha) 

@app.route('/actividad/<id_actividad>')
def actividad(id_actividad):
    nombres = {
        'patin': 'Patín Artístico',
        'voley_masculino': 'Voley Masculino',
        'voley_femenino': 'Voley Femenino',
        'boxeo': 'Boxeo',
        'bochas': 'Bochas',
        'kickboxing': 'Kick Boxing'
    }
    nombre = nombres.get(id_actividad, "Actividad Deportiva")
    return render_template('actividad.html', nombre_actividad=nombre, id_actividad=id_actividad)

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/campeonatos/futbol')
def camp_futbol():
    return render_template('campeonatos.html', deporte="Fútbol", logros="...")

@app.route('/campeonatos/voley')
def camp_voley():
    return render_template('campeonatos.html', deporte="Voley", logros="...")

@app.route('/campeonatos/patin')
def camp_patin():
    return render_template('campeonatos.html', deporte="Patín Artístico", logros="...")

@app.route('/campeonatos/kick-boxing')
def camp_kick():
    return render_template('campeonatos.html', deporte="Kick Boxing", logros="...")

@app.route('/campeonatos/boxeo')
def camp_boxeo():
    return render_template('campeonatos.html', deporte="Boxeo", logros="...")

@app.route('/campeonatos/bochas')
def camp_bochas():
    return render_template('campeonatos.html', deporte="Bochas", logros="...")

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# --- NUEVAS RUTAS PARA EL PANEL SECRETO (SIN ROMPER LO ANTERIOR) ---

@app.route('/gestion-noticias-vg', methods=['GET', 'POST'])
def panel_noticias():
    # CLAVE DE ACCESO (Podés cambiarla por la que quieras)
    CLAVE_MAESTRA = "villa2026"
    
    if request.method == 'POST':
        # Verificamos la clave que envíe el usuario
        clave = request.form.get('clave')
        if clave != CLAVE_MAESTRA:
            return "Clave incorrecta", 403
        
        # Obtenemos los datos del formulario
        titulo = request.form.get('titulo')
        texto = request.form.get('texto')
        foto = request.files.get('foto')
        
        nombre_foto = ""
        if foto and foto.filename != "":
            nombre_foto = foto.filename
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_foto))
        
        # Guardamos la noticia nueva al principio de la lista
        nuevas_noticias = obtener_noticias()
        nuevas_noticias.insert(0, {
            "titulo": titulo,
            "texto": texto,
            "foto": nombre_foto
        })
        
        with open(NOTICIAS_FILE, 'w', encoding='utf-8') as f:
            json.dump(nuevas_noticias, f, ensure_ascii=False, indent=4)
            
        return redirect(url_for('inicio'))

    # Si es GET, mostramos el panel (crearemos un html simple para esto después)
    return render_template('panel_admin.html')

@app.route('/borrar-noticia/<int:indice>')
def borrar_noticia(indice):
    # Función simple para limpiar noticias viejas
    noticias = obtener_noticias()
    if 0 <= indice < len(noticias):
        noticias.pop(indice)
        with open(NOTICIAS_FILE, 'w', encoding='utf-8') as f:
            json.dump(noticias, f, ensure_ascii=False, indent=4)
    return redirect(url_for('panel_noticias'))

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')