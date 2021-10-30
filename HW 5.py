"""5) The column "bill_length_mm" of penguins data, find:
a) mean
b) minimum, maximum
c) mode
d) median
e) Draw the graph boxplot
"""
#****************************
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


plt.style.use("ggplot")
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("penguins2.csv")

#a) mean
mean_bill_length_mm = np.mean(data["bill_length_mm"])
print(f"mean bill_length_mm: {mean_bill_length_mm}")

#b) minimum, maximum
min_bill_length_mm = np.amin(data["bill_length_mm"])
print(f"min bill_length_mm: {min_bill_length_mm}")

max_bill_length_mm = np.amax(data["bill_length_mm"])
print(f"max bill_length_mm: {max_bill_length_mm}")

#c) mode
mode_bill_length_mm = stats.mode(data["bill_length_mm"])
print(f"mode bill_length_mm: {mode_bill_length_mm}")

#d) median
data["bill_length_mm"].fillna(0,inplace=True) #datanan 'nan' ları çıkardık
median_bill_length_mm = np.median(data["bill_length_mm"])
print(f"median bill_length_mm: {median_bill_length_mm}")

#e) Draw the graph boxplot
data.head()
boxplot=data.boxplot(column =['bill_length_mm'])
boxplot.plot()
plt.show()
#***************************************
"""mean bill_length_mm: 43.9219298245614
min bill_length_mm: 32.1
max bill_length_mm: 59.6
mode bill_length_mm: ModeResult(mode=array([41.1]), count=array([7]))
median bill_length_mm: 44.25
"""