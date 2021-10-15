import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")
pokemon_attack = pokemon["Attack"]

#pokemon_attack.plot.density()
pokemon_attack.plot.density().set_yscale("log")
plt.show()