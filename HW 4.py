"""#4) “penguins”(peguins.csv) data . Find
a) How many rows and columns
b) Find the 2 columns with the highest correlation and draw this in the scatterplot?
"""
#*******************************

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("penguins.csv")

rows = len(data.axes[0])
cols = len(data.axes[1])
#*******************************
"""Number of Rows: 344
Number of Columns: 17
"""

print("Number of Rows: " + str(rows))
print("Number of Columns: " + str(cols))

sns.jointplot(data = pd.read_csv("penguins.csv"),x="Culmen Length (mm)",y="Flipper Length (mm)",kind="reg")
plt.show()

#****************************
"""HW 4.Figure"""