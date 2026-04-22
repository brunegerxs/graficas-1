# 📊 Guía de Gráficos en Matplotlib

Este repositorio contiene ejemplos y explicaciones de los gráficos disponibles en la librería Matplotlib para Python.

---

## 🚀 Gráficos Principales

### 1. Categorías y Comparación
* **plt.bar()**: Gráfico de barras verticales. Ideal para comparar magnitudes.
* **plt.barh()**: Gráfico de barras horizontales. Mejor para nombres largos.
* **plt.pie()**: Gráfico de tarta. Útil para mostrar porcentajes.

### 2. Distribución y Estadística
* **plt.hist()**: Histograma para ver la frecuencia de los datos.
* **plt.boxplot()**: Diagrama de caja para detectar valores atípicos (outliers).
* **plt.violinplot()**: Muestra la distribución de los datos con mayor detalle.

### 3. Relación y Tendencia
* **plt.plot()**: El clásico gráfico de líneas para series de tiempo.
* **plt.scatter()**: Gráfico de dispersión para ver la relación entre dos variables.
* **plt.step()**: Gráfico de escalones para cambios discretos.

---

## 🎨 Estilos Visuales

| Estilo | Comando |
| :--- | :--- |
| **GGPloT** | `plt.style.use('ggplot')` |
| **Oscuro** | `plt.style.use('dark_background')` |
| **Solarized** | `plt.style.use('Solarize_Light2')` |

---

## ⚙️ Tip de Configuración

Para que tus gráficas no se corten y salgan con buena calidad, añade esto:

```python
import matplotlib.pyplot as plt

# Ajusta el diseño automáticamente
plt.tight_layout()

# Guarda la imagen en alta definición
plt.savefig('grafica.png', dpi=300)
