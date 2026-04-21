import seaborn as sns
import matplotlib.pyplot as plt

# ESTA ES LA LÍNEA QUE TE FALTA:
tips = sns.load_dataset("tips") 

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="day",
    size="size",
    style="time",
    palette="deep"
)

plt.show()

