import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar los datos (Esto es lo que faltaba antes)
tips = sns.load_dataset("tips")
sns.boxplot(data=tips, x="day", y="total_bill", hue="time", palette="Set2")
plt.show()
