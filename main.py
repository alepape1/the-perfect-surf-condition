import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

linea_inicio_olas = 1
linea_inicio_viento = 166140


# Leer el archivo CSV (reemplaza 'tu_archivo.csv' con la ruta de tu archivo)
df = pd.read_csv('13560_14791_4034011_WAVE_20230831230739_20230917230739.csv', delimiter='\t', header=1, skiprows=range(1, linea_inicio_olas))
# Leer el archivo CSV de Mar de viento (reemplaza 'tu_archivo_mar_de_viento.csv' con la ruta de tu archivo de Mar de viento)
df_viento = pd.read_csv('13561_14792_2442_WIND_20000917235401_20230917235401.csv', delimiter='\t', header=0, skiprows=range(2, linea_inicio_viento))

# Convertir la columna de fecha y hora a un formato datetime
df['Fecha (GMT)'] = pd.to_datetime(df['Fecha (GMT)'], format='%Y %m %d %H')
df_viento['Fecha (GMT)'] = pd.to_datetime(df_viento['Fecha (GMT)'], format='%Y %m %d %H')

# Crear una figura con 4 subgráficos (2 filas y 2 columnas)
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Crear una figura y ejes
fig1, ax = plt.subplots(figsize=(12, 6))

# Configurar el formato de las fechas en el eje x
for ax in axs.flat:
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))

# Configurar el primer eje y etiquetas para la "Altura Significativa del Oleaje"
axs[0, 0].set_xlabel("Fecha y Hora")
axs[0, 0].set_ylabel("Altura Significativa del Oleaje (m)", color="tab:blue")
axs[0, 0].plot(df['Fecha (GMT)'], df['Altura Signif. del Oleaje(m)'], color="tab:blue", label="Altura del Oleaje")
axs[0, 0].tick_params(axis="y", labelcolor="tab:blue")

# Crear un segundo eje y etiquetas para el "Periodo Medio"
axs2 = axs[0, 0].twinx()
axs2.set_ylabel("Periodo Medio (s)", color="tab:red")
axs2.plot(df['Fecha (GMT)'], df['Periodo Medio(s)'], color="tab:red", label="Periodo Medio")
axs2.tick_params(axis="y", labelcolor="tab:red")

# Agregar un tercer eje y etiquetas para la "Dirección Media de Procedencia"

axs[0, 1].spines['right'].set_position(('outward', 60))  # Colocar el tercer eje a la derecha
axs[0, 1].set_ylabel("Direcc. Media de Proced.(0=N,90=E)", color="tab:green")
axs[0, 1].plot(df['Fecha (GMT)'], df['Direcc. Media de Proced.(0=N,90=E)'], color="tab:green", label="Dirección de las Olas")
axs[0, 1].tick_params(axis="y", labelcolor="tab:green")

# Configurar el primer eje y etiquetas para la "Altura Significativa del Mar de Viento"
ax3 = axs[0, 1].twinx()
ax3.set_xlabel("Fecha y Hora")
ax3.set_ylabel("Mar de viento: Direcc. Media de Proced.(0=N,90=E)", color="tab:orange")
ax3.plot(df['Fecha (GMT)'], df['Mar de viento: Direcc. Media de Proced.(0=N,90=E)'], color="tab:red", label="Mar de viento: Direcc.")
ax3.tick_params(axis="y", labelcolor="tab:red")


# Agregar un cuarto eje y etiquetas para el "Mar de viento"
ax3 = axs[1, 0].spines['right'].set_position(('outward', 180))  # Colocar el cuarto eje a la derecha
axs[1, 0 ].set_ylabel("Altura Significativa del Mar de Viento (m)", color="tab:orange")
axs[1, 0 ].plot(df['Fecha (GMT)'], df['Mar de viento:  Altura signif. Espectral(m)'], color="tab:orange", label="Mar de viento")
axs[1, 0 ].tick_params(axis="y", labelcolor="tab:orange")

# Agregar un quinto eje y etiquetas para el "Mar de fondo 1"
ax3 = axs[1, 0].twinx()
ax3.spines['right'].set_position(('outward',20))  # Colocar el quinto eje a la derecha
ax3.set_ylabel("Altura Significativa del Mar de Fondo 1 (m)", color="tab:purple")
ax3.plot(df['Fecha (GMT)'], df['Mar de fondo 1:  Altura signif. Espectral(m)'], color="tab:purple", label="Mar de fondo 1")
ax3.tick_params(axis="y", labelcolor="tab:purple")


# Configurar el primer eje y etiquetas para la "Altura Significativa del Mar de Viento"
axs[1, 1].set_xlabel("Fecha y Hora")
axs[1, 1].set_ylabel("Velocidad media del viento", color="tab:orange")
axs[1, 1].plot(df_viento['Fecha (GMT)'], df_viento['Velocidad media del viento(m/s)'], color="tab:orange", label="Velocidad viento (m/s)")
axs[1, 1].tick_params(axis="y", labelcolor="tab:orange")

# Título y leyenda
plt.title("Datos de Oleaje, Dirección de las Olas, Mar de Viento y Mar de Fondo")
fig.tight_layout()
fig.legend(loc="upper left")

# Rotar las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45)

# Filtrar los valores en el rango de 330 a 335 en la columna 'Direcc. Media de Proced.(0=N,90=E)'
filtro = (df['Direcc. Media de Proced.(0=N,90=E)'] >= 330) & (df['Direcc. Media de Proced.(0=N,90=E)'] <= 335)

# Aplicar el filtro al DataFrame
df_filtrado = df[filtro]

# Ver el DataFrame filtrado
print(df_filtrado['Direcc. Media de Proced.(0=N,90=E)'])

# Configurar el eje y y etiquetas para la "Dirección Media de Procedencia"
ax.set_xlabel("Fecha y Hora")
ax.set_ylabel("Direcc. Media de Proced.(0=N,90=E)", color="tab:green")
ax.plot(df_filtrado['Fecha (GMT)'], df_filtrado['Direcc. Media de Proced.(0=N,90=E)'], color="tab:green", label="Dirección de las Olas")
ax.tick_params(axis="y", labelcolor="tab:green")

# # Título y leyenda para la segunda figura
# plt.title("Datos del Viento")
fig.tight_layout()
fig.legend(loc="upper left")

# Rotar las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45)

# Mostrar la segunda figura
plt.show()