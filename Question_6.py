"""Find the standard deviations of the columns of penguins data in the Seaborn library and interpret the results?"""
import pandas as pd
import numpy as np

data = pd.read_csv("C:\python_lessons\Statistik_Home_work\penguins2.csv")

bill_length_mm1=data.loc[:,["bill_length_mm"]]
bill_depth_mm1=data.loc[:,["bill_depth_mm"]]
flipper_length_mm1 = data.loc[:,["flipper_length_mm"]]
body_mass_g1 = data.loc[:,["body_mass_g"]]

print("Standart Deviation of  ", np.std(bill_length_mm1))
print("Standart Deviation of  ", np.std(bill_depth_mm1))
print("Standart Deviation of  ", np.std(flipper_length_mm1))
print("Standart Deviation of  ", np.std(body_mass_g1))
