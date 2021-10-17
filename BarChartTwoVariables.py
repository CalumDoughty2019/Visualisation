import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import numpy as np

# pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")
# pokemon.groupby(['Type_1','Type_2']).size().unstack().plot(kind='bar', stacked=True)
# ax = plt.gca()
# ax.legend_ = None
# plt.show()

a = [67,10,30,20,25]
b = [30, 42, 11, 17, 5]
X = np.arange(5)
width = 0.35
fig, ax = plt.subplots()
ax.bar(X, a, width, color='blue')
ax.bar(X+width, b, width, color='y')
ax.set_xticks(X + width / 2)
ax.set_xticklabels(('Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5'))
plt.show()