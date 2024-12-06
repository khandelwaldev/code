import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

column_names = ['columnA', 'columnB', 'columnC']

df = pd.DataFrame(data, columns=column_names)

print(df)