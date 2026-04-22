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



Gráfico de Barras (plt.bar)
Estructura: Una lista de nombres (Eje X) y una lista de alturas (Eje Y).

Python
import matplotlib.pyplot as plt

frutas = ['Manzanas', 'Bananas', 'Cerezas']
cantidades = [20, 35, 15]

plt.bar(frutas, cantidades, color='orange')
plt.show()
Gráfico de Dispersión (plt.scatter)
Estructura: Coordenadas (x, y). Ideal para ver la relación entre dos variables numéricas.

Python
import matplotlib.pyplot as plt

altura = [160, 170, 180, 150]
peso = [55, 72, 85, 48]

plt.scatter(altura, peso, color='red')
plt.show()
Histograma (plt.hist)
Estructura: Una sola lista de datos. Matplotlib agrupa los valores y cuenta la frecuencia solo.

Python
import matplotlib.pyplot as plt

edades = [18, 19, 21, 18, 30, 35, 21, 25, 22, 18]

plt.hist(edades, bins=5, edgecolor='black')
plt.show()
Diagrama de Caja (plt.boxplot)
Estructura: Una lista de números. Sirve para ver promedios y detectar valores fuera de rango.

Python
import matplotlib.pyplot as plt

salarios = [1200, 1300, 1250, 1400, 1500, 4000]

plt.boxplot(salarios)
plt.show()
Gráfico de Tarta (plt.pie)
Estructura: Una lista de valores y una lista de nombres para las etiquetas.

Python
import matplotlib.pyplot as plt

votos = [500, 250, 100]
opciones = ['Opción A', 'Opción B', 'Opción C']

plt.pie(votos, labels=opciones, autopct='%1.1f%%')
plt.show()
