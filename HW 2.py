#2)Which are the two columns with the highest correlation in Titanic data?
#************************************

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv("titanic.csv")
print(data.corr(method ='pearson'))

f,ax=plt.subplots(figsize = (12,12))
# corr() is actually pearson correlation
sns.heatmap(data.corr(),annot= True,linewidths=0.3,fmt = ".1f",ax=ax)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.title('Correlation Map')
plt.show()
#**********************************************
"HW 1.Figure"
