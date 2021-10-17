import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import numpy as np

pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")

# plt.scatter(pokemon['Defense'], pokemon['Attack'], alpha=0.5)
# plt.show()

fig, ax = plt.subplots()
fit = np.polyfit(pokemon['Defense'], pokemon['Attack'], deg=1)
print(fit)
ax.plot(pokemon['Defense'], fit[0] * pokemon['Defense'] + fit[1], color='green')
ax.scatter(pokemon['Defense'], pokemon['Attack'])
plt.show()

