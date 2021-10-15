import pandas as pd
import matplotlib.pyplot as plt #used for visualisations

# labels = 'Frodo', 'Sam', 'Pippin', 'Merry'
# sizes = [215, 200, 330, 350]
# colors = ['gold', 'green', 'red', 'lightskyblue']
# explode = (0, 0.1, 0, 0)
# plt.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=140)
# plt.axis('equal')
# plt.show()

pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")
pokemon['Color'].value_counts().plot.pie()
plt.title('Pokemon colours in dataset')
plt.show()