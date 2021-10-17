import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import seaborn as sns #datasets library
import numpy as np

trains = pd.read_csv("C://Users//Calum//Documents//University//YEAR3//Term1//FundamentalsOfDataAnalytics//Week6//Visualisation//files//train.csv")


#3
#Produce a stacked bar chart showing the number of each gender in each passenger class
# trains.groupby(['Pclass','Sex']).size().unstack().plot(kind='bar', stacked=True)
# ax = plt.gca()
# ax.legend_ = None
# plt.show()

#4
#Produce a heatmap showing the correlation between each numerical variable. What shows a strong correlation?
# corr = trains.corr()
# sns.heatmap(corr)
# plt.show()

#5
#Produce a single scatter plot showing age and passenger class as well as age and number of siblings, different symbols should be used to represent the two different comparisons
fig, ax = plt.subplots()
fit = np.polyfit(trains['Age'], trains['Pclass'], deg=1)
print(fit)
ax.plot(trains['Age'], trains['SibSp'], color='green')
ax.scatter(trains['Age'], trains['Pclass'])
plt.show()