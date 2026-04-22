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
📊 2. Gráfico de Barras (plt.bar)
Estructura: Una lista de nombres y una de alturas.

Eje X: ['Categoría A', 'Categoría B', ...]

Eje Y: [Magnitud 1, Magnitud 2, ...]

Python
frutas = ['Manzanas', 'Bananas', 'Cerezas']
cantidades = [20, 35, 15]

plt.bar(frutas, cantidades, color='orange')
plt.show()
🎯 3. Dispersión (plt.scatter)Estructura: Coordenadas exactas $(x, y)$.X e Y: Deben ser numéricos para posicionar los puntos en el plano.Python# Ejemplo: Relación entre peso y altura
altura = [160, 170, 180, 150]
peso = [55, 72, 85, 48]

plt.scatter(altura, peso, color='red')
plt.show()
🏔️ 4. Histograma (plt.hist)
Estructura: Una sola lista desordenada.

Datos: Matplotlib calcula la frecuencia (cuántas veces se repiten los números) por ti.

Python
# Solo necesitas una lista de datos "crudos"
edades = [18, 19, 21, 18, 30, 35, 21, 25, 22, 18]

plt.hist(edades, bins=5, edgecolor='black')
plt.show()
📦 5. Boxplot (plt.boxplot)
Estructura: Una lista de números (o una lista de listas).

Dato: Es ideal para ver el promedio y los valores que "se salen" del grupo.

Python
salarios = [1200, 1300, 1250, 1400, 1500, 4000] # 4000 es el outlier

plt.boxplot(salarios)
plt.show()
6. Tarta (plt.pie)
Estructura: Tamaños proporcionales.

Valores: [40, 30, 20, 10] (No necesitan sumar 100, Matplotlib lo calcula).

Python
votos = [500, 250, 100]
opciones = ['Opción A', 'Opción B', 'Opción C']

plt.pie(votos, labels=opciones, autopct='%1.1f%%')
plt.show()
