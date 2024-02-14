# -*- coding: utf-8 -*-
"""seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HzHlm1nnKLU24XhT8G2-Gg8eUVVKZ5jN
"""

pip install seaborn

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#load example dataset
#tips=sns.load_csv("tips")
tips=pd.read_csv("/content/city_temperature.csv")
print(tips)
#create scatter plot
#sns.scatterplot(x="Year",y="AvgTemperature",data=tips)
#sns.scatterplot(x="total_bill",y="tips",data=tips)
sns.violinplot(x="Year",y="AvgTemperature",data=tips)
plt.title("scatter plot of Total Bill vs tip")
plt.xlabel("Year")
#plt.xlabel("Toatal Bill($)")
plt.ylabel("AvgTemperature")
#plt.ylabel("Tips($)")
plt.show()

#titanic
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#load example dataset
#tips=sns.load_csv("tips")
tips=sns.load_dataset("titanic")
print(tips)
#create scatter plot
sns.scatterplot(x="survived",y="age",data=tips)
#sns.scatterplot(x="total_bill",y="tips",data=tips)
plt.title("total survived and age")
plt.xlabel("survived")
#plt.xlabel("Toatal Bill($)")
plt.ylabel("age")
#plt.ylabel("Tips($)")
plt.show()

#iris dataset
import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
iris=sns.load_dataset("iris")
print(iris)
#compute correlation matrix
correlation_matrix=iris.corr()
#correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of iris dataset")
plt.show()

#fmri dataset
import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
iris=sns.load_dataset("fmri")
print(iris)
#compute correlation matrix
correlation_matrix=iris.corr()
#correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of fmri dataset")
plt.show()

#planets dataset
import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
iris=sns.load_dataset("planets")
print(iris)
#compute correlation matrix
correlation_matrix=iris.corr()
#correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of planets dataset")
plt.show()