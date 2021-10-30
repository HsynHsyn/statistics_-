# 3)For “Fare” columns in Titanic data find
# a) maximum, minimum
# b) mean
# c) mode
# d) median
# and
# f) Draw the graph boxplot
#********************************************

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#from scipy import stats
plt.style.use("ggplot")

import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("titanic.csv")

min_fare = np.amin(data["Fare"])
print(f"min Fare: {min_fare}")

max_fare = np.amax(data["Fare"])
print(f"max Fare: {max_fare}")

mean_fare = np.mean(data["Fare"])
print(f"mean Fare: {mean_fare}")

mode_fare = stats.mode(data["Fare"])
print(f"mode Fare: {mode_fare}")

data["Fare"].fillna(0,inplace=True) #datanan 'nan' ları çıkardık
median_fare = np.median(data["Fare"])
print(f"median Fare: {median_fare}")

data.head()
boxplot=data.boxplot(column =['Fare'])
boxplot.plot()
plt.show()
#***********************************************
# HW 2.Figure