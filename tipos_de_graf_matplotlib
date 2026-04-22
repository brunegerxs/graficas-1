📊 Guía Visual de Matplotlib: El Arte de los Datos
Matplotlib es la biblioteca fundamental de visualización en Python. Para dominarla, es crucial saber qué gráfico elegir según la naturaleza de tus datos.
Gráfico,Función Principal,Comando Base
Gráfico de Barras,Comparar valores entre categorías discretas.,plt.bar()
Barras Horizontales,Útil cuando los nombres de las categorías son largos.,plt.barh()
Gráfico de Tarta,Mostrar proporciones de un total (usar con moderación).,plt.pie()
2. Relación y Distribución
Perfectos para entender cómo se comportan las variables y si existe una correlación entre ellas.

Dispersión (Scatter Plot)
Se usa para identificar la relación entre dos variables numéricas.

Comando: plt.scatter(x, y)

Uso: Detectar agrupamientos (clusters) o tendencias.

Histograma
Muestra la frecuencia de una variable continua dividida en "bins" o intervalos.

Comando: plt.hist(data)

Uso: Ver si los datos siguen una distribución normal o tienen sesgo.

3. Evolución Temporal (Series de Tiempo)
Cuando el eje X representa el tiempo (segundos, días, años).

Gráfico de Líneas (plt.plot()): Conecta puntos de datos para mostrar tendencias continuas. Es el gráfico por excelencia para ver el crecimiento de usuarios, precio de acciones o cambios de temperatura.

4. Estadísticas Avanzadas
Para análisis de datos más profundos y detección de valores atípicos.

Boxplot (Diagrama de Caja): Resume la distribución a través de cuartiles y resalta los outliers.

plt.boxplot(data)

Violin Plot: Combina un boxplot con una estimación de densidad, mostrando dónde se concentran más los datos.

plt.violinplot(data)

🚀 Ejemplo de Código "Estético"
Para que tus gráficos no se vean como de los años 90, usa estilos modernos:

Python
import matplotlib.pyplot as plt
import numpy as np

# Configurar un estilo moderno
plt.style.use('ggplot') 

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label='Onda Senoidal', color='#3498db', linewidth=2)

ax.set_title('Visualización Profesional en Matplotlib', fontsize=14)
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Amplitud')
ax.legend()

plt.show()
