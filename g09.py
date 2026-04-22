import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
# Calculamos la matriz de correlación
corr = tips.select_dtypes(include=['number']).corr()

# Generamos el heatmap
sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=.5)
plt.show()
