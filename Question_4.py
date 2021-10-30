""" “penguins”(peguins.csv) data . Find

a) How many rows and columns
b) Find the 2 columns with the highest correlation and draw this in the scatterplot?"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=pd.read_csv("C:\python_lessons\Statistik_Home_work\penguins.csv")


print("Rows of penguins.csv: ", len(data))
print("coloumn of penguins.csv: ", len(data.columns))

# Pearson Comand Prompt Result
p1 = data.loc[:,["Sample Number","Culmen Length (mm)","Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)", "Delta 15 N (o/oo)", "Delta 13 C (o/oo)"]].corr(method= "pearson")
print('Pearson correlation: ')
print(p1)

f2,ax=plt.subplots(figsize = (18,18))
y = np.random.uniform(0,350,344)
x1 = data.loc[:,["Flipper Length (mm)"]]
x2 = data.loc[:,["Body Mass (g)"]]
plt.scatter(x1,y,color="black")
plt.scatter(x2,y,color="orange")
plt.xlim([-1000,7000])
plt.ylim([-100,500])
plt.xlabel("x")
plt.ylabel("y")

plt.show()