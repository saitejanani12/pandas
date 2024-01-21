import pandas as pd

data = pd.read_csv(r'E:\\pdf\\student.csv')

data[::]

#DataFiltering by using Normal

data[data['maths']<75]

#Data Filtering By using Query 
data.query('telugu>65')

# Data Filtering By using isin
data[data['name'].isin(['Ramesh'])]

# Data Filtering By using loc complex condition
data[(data['name']=='Ramesh')&(data['maths']>50)]

# Data Filtering By using loc isin
data[data.isin({'name':['Ramesh',"Biswa"],'maths':[98]})]

# Data filtering by using function
data[data['htno'].apply(lambda x:x%2==0)]

def filtering(name):
    return name == 'Ramesh'
data[data['name'].apply(filtering)]

