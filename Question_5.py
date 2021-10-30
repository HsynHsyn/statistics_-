""" 
The column "bill_length_mm" of penguins data, find:

a) mean
b) minimum, maximum
c) mode
d) median
e) Draw the graph boxplot

"""
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns 
import matplotlib.pyplot as plt
plt.style.use("ggplot")

data = pd.read_csv("C:\python_lessons\Statistik_Home_work\penguins2.csv")

print("mean",np.mean(data.bill_length_mm))
print("max",np.max(data.bill_length_mm))
print("min",np.min(data.bill_length_mm))
print("mode",stats.mode(data.bill_length_mm))
print("median",np.median(data.bill_length_mm))

melted_data = pd.melt(data,value_vars = ['bill_length_mm'])  # Burada -Draw the graph boxplot- çizimini yapıyoruz
sns.boxplot(x = "variable", y = "value",data= melted_data)
plt.show()