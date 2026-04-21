import seaborn as sns
import matplotlib.pyplot as plt

datos = sns.load_dataset('tips')

sns.histplot(data=datos, x='total_bill', bins=20)
plt.show()