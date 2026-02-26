import pandas as pd
import matplotlib.pyplot as plt

# 1. CARGA DE DATOS
# Cambiá 'tus_datos.csv' por el nombre real de tu archivo (ej: 'argentina.csv')
df = pd.read_csv('argentina.csv')

# Convertimos la fecha al formato correcto (día/mes/año como tenés vos)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# --- 1️⃣ EXPLORACIÓN INICIAL ---
print(f"Partidos analizados: {len(df)}")
equipos = df['Home'].unique()
print(f"Cantidad de equipos en el periodo: {len(equipos)}")

# --- 2️⃣ ANÁLISIS DE GOLES ---
df['Total_Goles'] = df['HG'] + df['AG']
promedio = df['Total_Goles'].mean()
print(f"\nPromedio de goles por partido (2012-2026): {promedio:.2f}")

# Partido con más goles
mas_goles = df.loc[df['Total_Goles'].idxmax()]
print(f"Partido récord: {mas_goles['Home']} {mas_goles['HG']} - {mas_goles['AG']} {mas_goles['Away']}")

# --- 3️⃣ RENDIMIENTO LOCAL VS VISITANTE ---
# Contamos los resultados en la columna 'Res'
# H = Home (Local), D = Draw (Empate), A = Away (Visitante)
resultados = df['Res'].value_counts(normalize=True) * 100
print("\nDistribución de resultados:")
print(f"Victorias Locales: {resultados['H']:.1f}%")
print(f"Empates: {resultados['D']:.1f}%")
print(f"Victorias Visitantes: {resultados['A']:.1f}%")

# --- 4️⃣ ANÁLISIS TEMPORAL (Goles por Año) ---
df['Año'] = df['Date'].dt.year
goles_por_año = df.groupby('Año')['Total_Goles'].mean()

# --- 5️⃣ VISUALIZACIÓN ---
plt.figure(figsize=(10, 5))
plt.plot(goles_por_año.index, goles_por_año.values, marker='o', color='red', linestyle='--')
plt.title('Promedio de goles por año en la Liga Argentina')
plt.xlabel('Año')
plt.ylabel('Goles promedio')
plt.grid(True)
plt.show()

# --- BONUS: TOP 5 EQUIPOS GOLEADORES ---
# Sumamos goles cuando juegan de local y cuando juegan de visitante
goles_local = df.groupby('Home')['HG'].sum()
goles_visita = df.groupby('Away')['AG'].sum()

# Combinamos ambos y ordenamos de mayor a menor
total_goles_equipo = goles_local.add(goles_visita, fill_value=0).sort_values(ascending=False)

print("\n--- TOP 5 EQUIPOS MÁS GOLEADORES (2012-2026) ---")
print(total_goles_equipo.head(5))

# --- TOP 5 EQUIPOS CON MÁS GOLES EN CONTRA ---
goles_recibidos_loc = df.groupby('Home')['AG'].sum()
goles_recibidos_vis = df.groupby('Away')['HG'].sum()
total_recibidos = goles_recibidos_loc.add(goles_recibidos_vis, fill_value=0).sort_values(ascending=False)

print("\n--- TOP 5 EQUIPOS CON MÁS GOLES EN CONTRA ---")
print(total_recibidos.head(5))

# --- 1. PREPARACIÓN DE DATOS ---
# Usamos el cálculo que hicimos antes para tener el total de goles por equipo
top_5_goleadores = total_goles_equipo.head(5)

# --- 2. CREACIÓN DEL GRÁFICO ---
plt.figure(figsize=(10, 6)) # Ajustamos el tamaño de la ventana
# Creamos barras de color azul (skyblue) con bordes negros
plt.bar(top_5_goleadores.index, top_5_goleadores.values, color='skyblue', edgecolor='black')

# --- 3. DETALLES ESTÉTICOS ---
plt.title('Top 5 Equipos con más Goles (2012-2026)', fontsize=14)
plt.xlabel('Equipo', fontsize=12)
plt.ylabel('Cantidad Total de Goles', fontsize=12)

# Agregamos el número exacto de goles sobre cada barra para que sea más claro
for i, v in enumerate(top_5_goleadores.values):
    plt.text(i, v + 5, str(int(v)), ha='center', fontweight='bold')

plt.show()

# --- BUSCADOR DE EQUIPO INTERACTIVO ---

print("\n" + "="*30)
print("🔍 BUSCADOR DE ESTADÍSTICAS")
equipo_buscado = input("Escribí el nombre del equipo (ej: Independiente): ")

# Filtramos los partidos donde el equipo jugó como local o visitante
partidos_equipo = df[(df['Home'] == equipo_buscado) | (df['Away'] == equipo_buscado)]

if not partidos_equipo.empty:
    # Calculamos estadísticas básicas del equipo
    total_pj = len(partidos_equipo)
    
    # Goles a favor (cuando es local + cuando es visitante)
    gf_local = partidos_equipo[partidos_equipo['Home'] == equipo_buscado]['HG'].sum()
    gf_visita = partidos_equipo[partidos_equipo['Away'] == equipo_buscado]['AG'].sum()
    total_gf = gf_local + gf_visita
    
    print(f"\nResultados para: {equipo_buscado}")
    print(f"- Partidos jugados: {total_pj}")
    print(f"- Total de goles marcados: {total_gf}")
    print(f"- Promedio de gol por partido: {(total_gf/total_pj):.2f}")
else:
    print(f"\n❌ No se encontraron datos para '{equipo_buscado}'.")
    print("Asegurate de escribirlo tal cual aparece en el archivo CSV.")