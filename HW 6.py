#6) Find the standard deviations of the columns of
# penguins data in the Seaborn library and
# interpret the results?
#****************************************
import numpy as np
import pandas as pd


data = pd.read_csv("penguins2.csv")
print(np.std(data))
#***********************************
"""bill_length_mm         5.451596
bill_depth_mm          1.971904
flipper_length_mm     14.041141
body_mass_g          800.781229
dtype: float64
"""