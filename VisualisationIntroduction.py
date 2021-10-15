import pandas as pd
import matplotlib.pyplot as plt #used for visualisations
import seaborn as sns #datasets library

iris = sns.load_dataset("iris") #iris is a machine learning dataset #its a flower dataset

# pd.plotting.scatter_matrix(iris) #use the planning functionality of pandas to create a scanner matrix
# plt.show() #render the visualisation

# plt.plot([0, 100, 200, 300])
# plt.show()

plt.plot([100, 200, 300, 400], [15, 40, 75, 90], linestyle='--', color='g', marker='x', linewidth=2.0)
plt.axis([0, 500, 0, 100])
plt.show()