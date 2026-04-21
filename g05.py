import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar los datos (Esto es lo que faltaba antes)
tips = sns.load_dataset("tips")

# 3. El gráfico de onditas (KDE)
sns.kdeplot(data=tips, x="total_bill", fill=True)
plt.show()
