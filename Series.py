# import pandas as pd 
# #python Str Data into pandas.Series
# s = pd.Series('sai')
# print(s)
# import pandas as pd 
#  #python Int Data into pandas.Series
# s = pd.Series(10)
# print(s)
# import pandas as pd 
#  #python Flot Data into pandas.Series
# s = pd.Series(10.0)
# print(s)
import pandas as pd
import numpy as np
lst = [int(x) for x in range(1,11)]
p = np.array(lst)
data = pd.Series(p,index=['A','B','C','D','E','F','G','H','I','J'])
print(data)
