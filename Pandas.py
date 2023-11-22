# import numpy as np 
# import pandas as pd
# import random


# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# # 1 вариант
# data = data.melt(ignore_index=False).reset_index().pivot_table('variable', 'index', 'value', aggfunc='count').fillna(0)

# print(data)

# # 2 вариант
# data = pd.get_dummies(data.melt(ignore_index=False).value).groupby(level=0).max()

# print(data)

