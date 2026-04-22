from flask import Flask, render_template, url_for, request, redirect
import os
import json

app = Flask(__name__)

# --- CONFIGURACIÓN DE RUTAS SEGURAS PARA RENDER ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
NOTICIAS_FILE = os.path.join(BASE_DIR, 'noticias.json')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear carpeta de fotos si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Función para leer noticias
def obtener_noticias():
    if os.path.exists(NOTICIAS_FILE):
        with open(NOTICIAS_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

# --- RUTAS DE NAVEGACIÓN ---

@app.route('/')
def inicio():
    lista_noticias = obtener_noticias()
    return render_template('index.html', noticias=lista_noticias)

@app.route('/reserva')
def reserva(): return render_template('reserva.html')

@app.route('/primera')
def primera(): return render_template('primera.html')

@app.route('/senior')
def senior(): return render_template('senior.html')

@app.route('/cuarta')
def cuarta(): return render_template('cuarta.html')

@app.route('/quinta')
def quinta(): return render_template('quinta.html')

@app.route('/sexta')
def sexta(): return render_template('sexta.html')

@app.route('/femenino')
def femenino(): return render_template('femenino.html')

@app.route('/fixture')
def fixture(): return render_template('fixture.html')

@app.route('/resultados')
def resultados(): return render_template('resultados.html', fecha=1)

@app.route('/resultados/<int:numero_fecha>')
def resultados_fecha(numero_fecha):
    return render_template('resultados.html', fecha=numero_fecha)

@app.route('/actividad/<id_actividad>')
def actividad(id_actividad):
    nombres = {
        'patin': 'Patín Artístico', 'voley_masculino': 'Voley Masculino',
        'voley_femenino': 'Voley Femenino', 'boxeo': 'Boxeo',
        'bochas': 'Bochas', 'kickboxing': 'Kick Boxing'
    }
    nombre = nombres.get(id_actividad, "Actividad Deportiva")
    return render_template('actividad.html', nombre_actividad=nombre, id_actividad=id_actividad)

@app.route('/historia')
def historia(): return render_template('historia.html')

@app.route('/campeonatos/<deporte_id>')
def campeonatos(deporte_id):
    # Simplifiqué tus rutas de campeonatos para que sea más fácil
    nombres = {'futbol': 'Fútbol', 'voley': 'Voley', 'patin': 'Patín Artístico', 
               'kick-boxing': 'Kick Boxing', 'boxeo': 'Boxeo', 'bochas': 'Bochas'}
    nombre = nombres.get(deporte_id, "Deporte")
    return render_template('campeonatos.html', deporte=nombre, logros="...")

@app.route('/galeria')
def galeria(): return render_template('galeria.html')

# --- PANEL DE CONTROL (EL "MOTOR" DE TU HTML NUEVO) ---

@app.route('/gestion-noticias-vg', methods=['GET', 'POST'])
def panel_noticias():
    CLAVE_MAESTRA = "villa2026"
    
    if request.method == 'POST':
        clave = request.form.get('clave')
        if clave != CLAVE_MAESTRA:
            return "Clave incorrecta", 403
        
        titulo = request.form.get('titulo')
        texto = request.form.get('texto')
        foto = request.files.get('foto')
        
        nombre_foto = ""
        if foto and foto.filename != "":
            nombre_foto = foto.filename
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_foto))
        
        noticias = obtener_noticias()
        # Insertar arriba y dejar solo las últimas 10
        noticias.insert(0, {"titulo": titulo, "texto": texto, "foto": nombre_foto})
        noticias = noticias[:10]
        
        with open(NOTICIAS_FILE, 'w', encoding='utf-8') as f:
            json.dump(noticias, f, ensure_ascii=False, indent=4)
            
        return redirect(url_for('inicio'))

    return render_template('panel_admin.html')

# --- INICIO DEL SERVIDOR (AJUSTADO PARA RENDER) ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
