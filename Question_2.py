""" Which are the two columns with the highest correlation in Titanic data? """

import pandas as pd
import numpy as np

data=pd.read_csv("C:\python_lessons\Statistik_Home_work\\titanic.csv")

p1=data.loc[:,["PassengerId", "Pclass", "Age", "SibSp", "Parch", "Ticket","Fare"]].corr(method="pearson")

print("Pearson Corelation")
print(p1)