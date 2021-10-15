import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import seaborn as sns #datasets library

pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")

plt.figure(figsize=(20,15))
sns.violinplot(x='Type_1', y='Attack', data=pokemon)
plt.show()