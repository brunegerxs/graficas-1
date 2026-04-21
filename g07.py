import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar los datos (Esto es lo que faltaba antes)
tips = sns.load_dataset("tips")
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True, palette="pastel")
plt.show()
