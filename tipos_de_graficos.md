#investiga los diferentes tipos de graficos disponibles en  seaborn 
## 🎨 Toolbox de Visualización: Seaborn

![Seaborn](https://shields.io) 
![Python](https://shields.io)

Seaborn divide sus funciones en tres categorías principales. Usá esta guía rápida para elegir el gráfico correcto:


| Categoría | Gráficos Clave | ¿Cuándo usarlo? |
| :--- | :--- | :--- |
| **🔗 Relacional** | `scatter`, `line` | Para ver cómo una variable afecta a otra. |
| **📐 Distribución** | `hist`, `kde`, `ecdf` | Para entender el "comportamiento" de los datos. |
| **🏷️ Categórico** | `box`, `violin`, `bar` | Para comparar grupos o etiquetas. |

---

### 🚀 Visualización Rápida

#### 1. Relaciones Numéricas
> Ideales para encontrar correlaciones en `relplot()`
*   `scatterplot()`: Dispersión de puntos.
*   `lineplot()`: Series de tiempo y tendencias.

#### 2. Distribuciones
> Entendé la concentración de tus datos con `displot()`
*   `histplot()`: El clásico histograma de barras.
*   `kdeplot()`: Curvas de densidad elegantes.

#### 3. Categorías
> Compará grupos fácilmente con `catplot()`
*   `boxplot()`: Identificá valores atípicos (outliers) rápido.
*   `violinplot()`: Combina cajas con densidad (se ve muy pro).
*   `swarmplot()`: Muestra cada punto sin que se encimen.

---

### 🔥 Gráficos de Matriz (Análisis Pro)

| Tipo | Función | Descripción |
| :--- | :--- | :--- |
| **Mapa de Calor** | `heatmap()` | Perfecto para ver correlaciones entre variables. |
| **Pares** | `pairplot()` | Crea una matriz de gráficos de todo tu dataset de una. |

# 📊 Manual Maestro de Seaborn: Gráficos y Parámetros

Guía rápida para copiar y consultar los parámetros más importantes de las visualizaciones principales.

---

## 🚀 Gráficos Relacionales y de Distribución

### 📍 Scatterplot (Puntos) & 🌊 KDE Plot (Densidad)


| Gráfico | Parámetros Clave | Código de Ejemplo |
| :--- | :--- | :--- |
| **Scatter** | `x`, `y`, `hue` (color), `size` (tamaño), `style` (forma) | `sns.scatterplot(data=df, x="x", y="y", hue="cat")` |
| **KDE** | `x`, `fill` (relleno), `bw_adjust` (suavizado), `alpha` | `sns.kdeplot(data=df, x="x", fill=True, alpha=0.5)` |

---

## 📦 Gráficos Categóricos (Comparación de Grupos)

### 📦 Boxplot & 🎻 Violinplot


| Gráfico | Parámetros Clave | Código de Ejemplo |
| :--- | :--- | :--- |
| **Boxplot** | `x`, `y`, `hue`, `palette`, `width`, `whis` (bigotes) | `sns.boxplot(data=df, x="cat", y="num", palette="Set1")` |
| **Violin** | `x`, `y`, `hue`, `split` (mitades), `inner` (interior) | `sns.violinplot(data=df, x="cat", y="num", split=True)` |

---

### 📊 Barplot (Barras de Promedio)


| Parámetro | Descripción |
| :--- | :--- |
| `estimator` | Cambia qué calcular (promedio, mediana, etc). |
| `errorbar` | Controla las líneas de error sobre las barras. |
| `orient` | `"h"` para barras horizontales o `"v"` para verticales. |

```python
# Ejemplo de Barras
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", palette="magma")
import seaborn as sns
import matplotlib.pyplot as plt

# Carga de datos base
tips = sns.load_dataset("tips")


