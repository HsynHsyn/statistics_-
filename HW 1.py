import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the titanic data to data variable
data=pd.read_csv("C:\\titanic.csv")

#Read the head of data
print (data.head())

#Read the first column to understand the headers
first_row=data.loc[0,:]
print(first_row)

#********************************************
"""[5 rows x 8 columns]
Survived                                        0
Pclass                                          3
Name                       Mr. Owen Harris Braund
Sex                                          male
Age                                          22.0
Siblings/Spouses Aboard                         1
Parents/Children Aboard                         0
Fare                                         7.25
"""