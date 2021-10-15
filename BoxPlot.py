import matplotlib.pyplot as plt #used for visualisations
import seaborn as sns #datasets library

# iris = sns.load_dataset("iris")
# iris.plot(kind='box', subplots=True, layout=(2,2))
# plt.show()

import pandas as pd
pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")
pokemon.plot(kind='box', subplots=True, layout=(4,4))
plt.show()

