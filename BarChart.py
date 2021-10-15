import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import numpy as np

status = ('Divorced', 'Single', 'Married', 'Widowed')
y_pos = np.arange(len(status))
numbers = [400, 556, 678, 123]
plt.bar(y_pos, numbers, align='center', alpha=0.5)
plt.xticks(y_pos, status)
plt.ylabel('Count')
plt.title('Marital Status of Narnians')
plt.show()

# pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")
# pokemon['Color'].value_counts().plot.bar()
# plt.ylabel('Count')
# plt.title('Pokemon colours in dataset')
# plt.show()

# pokemon = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week5//DataAndPandas//files//pokemon_alopez247.csv")
# pokemon['Color'].value_counts().nlargest(5).sort_values(ascending=True).plot.barh()
# plt.title('Pokemon 5 pokemon colours in dataset')
# plt.show()