"""For “Fare” columns in Titanic data find
a) maximum, minimum
b) mean
c) mode
d) median
and
f) Draw the graph boxplot"""

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use("ggplot")


data=pd.read_csv("C:\python_lessons\Statistik_Home_work\\titanic.csv")

print("max",np.max(data.Fare))
print("min",np.min(data.Fare))
print("mean",np.mean(data.Fare))
print("mode",stats.mode(data.Fare))
#print("median",np.median(data.Fare))
print("median",np.nanmedian(data.Fare))


melted_data = pd.melt(data,value_vars = ['Fare'])
sns.boxplot(x = "variable", y = "value",data= melted_data)
plt.show()