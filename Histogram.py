import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")

pokemon_attack = pokemon["Attack"]
num_bins = 100 #20 #5 #100 #1000
plt.hist(pokemon_attack, num_bins, facecolor='green', alpha=0.5)
plt.xlabel("Attack Strength")
plt.ylabel("Count")
plt.show()