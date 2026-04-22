import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
# Calculamos la matriz de correlación
corr = tips.select_dtypes(include=['number']).corr()

sns.pairplot(tips, hue="sex", palette="pastel")
plt.show()
