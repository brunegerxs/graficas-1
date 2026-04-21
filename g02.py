import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('tips')

sns.scatterplot(data=datos, x='total_bill', y='tip')
plt.show()