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

# Configurar el formato de las fechas en los ejes x
for ax in axs.flat:
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))

# Primer subgráfico: Altura Significativa del Oleaje
axs[0, 0].set_ylabel("Altura Significativa del Oleaje (m)", color="tab:blue")
axs[0, 0].plot(df['Fecha (GMT)'], df['Altura Signif. del Oleaje(m)'], color="tab:blue", label="Altura del Oleaje")
axs[0, 0].tick_params(axis="y", labelcolor="tab:blue")
axs[0, 0].set_title("Altura Significativa del Oleaje")

# Segundo subgráfico: Periodo Medio
axs[0, 1].set_ylabel("Periodo Medio (s)", color="tab:red")
axs[0, 1].plot(df['Fecha (GMT)'], df['Periodo Medio(s)'], color="tab:red", label="Periodo Medio")
axs[0, 1].tick_params(axis="y", labelcolor="tab:red")
axs[0, 1].set_title("Periodo Medio")

# Tercer subgráfico: Dirección Media de Procedencia
axs[1, 0].set_ylabel("Direcc. Media de Proced.(0=N,90=E)", color="tab:green")
axs[1, 0].plot(df['Fecha (GMT)'], df['Direcc. Media de Proced.(0=N,90=E)'], color="tab:green", label="Dirección de las Olas")
axs[1, 0].tick_params(axis="y", labelcolor="tab:green")
axs[1, 0].set_title("Dirección Media de Procedencia")

# Cuarto subgráfico: Velocidad media del viento
axs[1, 1].set_ylabel("Velocidad media del viento (m/s)", color="tab:orange")
axs[1, 1].plot(df_viento['Fecha (GMT)'], df_viento['Velocidad media del viento(m/s)'], color="tab:orange", label="Velocidad del viento")
axs[1, 1].tick_params(axis="y", labelcolor="tab:orange")
axs[1, 1].set_title("Velocidad media del viento")

# Ajustar el espacio entre los subgráficos
plt.tight_layout()

# Rotar las etiquetas del eje x para una mejor visualización en todos los subgráficos
for ax in axs.flat:
    ax.tick_params(axis="x", rotation=45)

# Mostrar la figura
plt.show()
