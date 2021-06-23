 # - (1) pivot(), pd.pivot_table()
 #
 # - (2) stack(), unstack()
 #
 # - (3) melt()
 #
 # - (4) wide_to_long()
 #
 # - (5) pd.crosstab()

import pandas as pd
import numpy as np
from pandas import DataFrame
from icecream import ic

df = pd.DataFrame({"학생 ID" :["kim","kim","kim","lee","lee","park"],
                   "1학기 학점":["A","A","A","B","B","B"],
                   "2학기 학점":["D","D","D","C","C","D"]})
ic(df)
pd.crosstab(df['1학기 학점'],df['2학기 학점'])
#%%