# 🛠️ Estructuras de Datos para Matplotlib

Para que tus gráficos funcionen, los **arreglos (listas o arrays)** deben tener formatos específicos. Aquí tienes la guía rápida para cada uno.

---

## 📈 1. Gráfico de Líneas (`plt.plot`)
**Estructura:** Dos listas de igual longitud.
* **X:** Etiquetas o tiempo.
* **Y:** Valores numéricos.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] 
y = [10, 15, 7, 12, 9]

plt.plot(x, y, color='blue', marker='o')
plt.show()



## 📊 2. Gráfico de Barras (`plt.bar`)

**Estructura:** Una lista de nombres y una de alturas.

* **Eje X:** `['Categoría A', 'Categoría B', ...]`
* **Eje Y:** `[Magnitud 1, Magnitud 2, ...]`

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
frutas = ['Manzanas', 'Bananas', 'Cerezas']
cantidades = [20, 35, 15]

# Creación del gráfico
plt.bar(frutas, cantidades, color='orange')

# Personalización básica
plt.title('Distribución de Frutas')
plt.xlabel('Frutas')
plt.ylabel('Cantidad')

plt.show()
---

## 🎯 3. Dispersión (`plt.scatter`)

**Estructura:** Coordenadas exactas $(x, y)$.  
* **X e Y:** Deben ser numéricos para posicionar los puntos en el plano cartesiano.

```python
import matplotlib.pyplot as plt

# Ejemplo: Relación entre peso y altura
# Ambos arreglos deben tener la misma longitud
altura = [160, 170, 180, 150]
peso = [55, 72, 85, 48]

# Creamos el gráfico de puntos
plt.scatter(altura, peso, color='red', label='Datos Biométricos')

# Añadimos etiquetas para que se entienda mejor
plt.title('Relación Peso vs Altura')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend()

plt.show()
---

## 🏔️ 4. Histograma (`plt.hist`)

**Uso:** Ver la distribución de una sola variable (frecuencia). Es ideal para entender cómo se agrupan tus datos.

* **Datos necesarios:** Una única lista con muchos valores numéricos.
* **Nota:** Matplotlib calculará automáticamente cuántas veces aparece cada número dentro de los rangos (bins).

```python
import matplotlib.pyplot as plt

# Matplotlib agrupará estos números automáticamente
datos = [1, 2, 1, 3, 3, 3, 4, 5, 2, 3, 1]

# Creamos el histograma
# 'bins' define en cuántas barras se agrupan los datos
plt.hist(datos, bins=5, color='skyblue', edgecolor='black')

# Añadimos títulos y etiquetas
plt.title('Distribución de Frecuencias')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.show()
---

## 📦 5. Diagrama de Caja (`plt.boxplot`)

**Estructura:** Una lista de números (o una lista de listas para comparar varios grupos).

* **Dato clave:** Es el gráfico ideal para análisis estadístico, ya que permite ver la mediana, los cuartiles y detectar fácilmente los **outliers** (valores que se salen del grupo).

```python
import matplotlib.pyplot as plt

# Datos de ejemplo: Lista de números
# El valor 4000 actúa como un "outlier" o valor atípico
salarios = [1200, 1300, 1250, 1400, 1500, 4000] 

# Creación del gráfico de caja
plt.boxplot(salarios)

# Personalización
plt.title('Análisis Estadístico de Salarios')
plt.ylabel('Monto en USD')

plt.show()
---

## 🍕 6. Gráfico de Tarta (`plt.pie`)

**Estructura:** Tamaños proporcionales.

* **Valores:** `[40, 30, 20, 10]` (No necesitan sumar exactamente 100, Matplotlib calcula los porcentajes automáticamente).
* **Etiquetas:** Una lista de strings para identificar cada "rebanada".

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
votos = [500, 250, 100]
opciones = ['Opción A', 'Opción B', 'Opción C']

# Creación del gráfico
# 'autopct' sirve para mostrar el porcentaje dentro de la tarta
plt.pie(votos, labels=opciones, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])

# Título
plt.title('Distribución de Votos')

plt.show()
