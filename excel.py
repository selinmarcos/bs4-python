#SCRIPT TO EXPORT IN EXCEL USING PANDAS


import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Col A': [1],
    'Col B': ['A'],
    'Col C': ['Apple'],
})

df.to_excel('df.xlsx', index=False) # para que no aparezca el index