import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(501)

new_df = pd.DataFrame(randn(6,5),['city','place','country','zip','name','floor'],['A','B','C','D','E'])

print(new_df)
print('-'*50)
print(new_df['A'])
print('-'*50)
print(new_df[['A','B']])
print('-'*50)
print(new_df.A)
print('-'*50)
print(new_df[['A','B','D']])
print('-'*50)
new_df['contact']=new_df['A']+new_df['B']+new_df['C']
print('-'*50)
print(new_df)
print('-'*50)
print(new_df.loc['city'])
print('-'*50)
print(new_df.loc[['city','place'],['A','B']])
print('-'*50)
print('-'*50)
new_df=pd.DataFrame(randn(3,2),['B','C','D'],['home','bungalow'])
print(new_df)
print('-'*50)
print(new_df[new_df['bungalow']<0])
print('-'*50)
print(new_df[new_df['bungalow']<0.6])
print('-'*50)
store_df=new_df[new_df['bungalow']>0]
print(store_df)
print('-'*50)
print(store_df['home'])
print('-'*50)
print(store_df['bungalow'])
print('-'*50)
# print(new_df[new_df['home']>0][['B','A']])
print('-'*50)
# print([new_df (new_df['home']>0) | (new_df['B']>1) ])

print(new_df[new_df['home']>0]['home'])
print(new_df[new_df['home']<5]['bungalow'])


print(new_df[new_df['home']>1]['home'])

import numpy as np
import pandas as pd

df=pd.DataFrame({'A':[1,2,np.nan],
                'B':[np.nan,np.nan,np.nan],
                'C':[1,2,3]})

print('-'*50)
print('-'*50)
print(df)
print('-'*50)
#removes NaN values
# by default axis=0
# means works fine for only x-axis

print(df.dropna())
print('-'*50)
print(df.dropna(axis=1))
# df.dropna()
print('-'*50)
# thresh  argument
# And basically what that means is because row 1 had at least two non and a values 2.0 and the two it
# find all Nan values and remove it
print(df.dropna(thresh=2))
print('-'*50)
print(df.dropna(thresh=3))

df=pd.DataFrame({'A':[1,2,np.nan],
                'B':[5,np.nan,np.nan],
                'C':[1,2,3]})

print('-'*50)
print('-'*50)
print(df)
print('-'*50)
#removes NaN values
# by default axis=0
# means works fine for only x-axis

print(df.dropna())
print('-'*50)
print(df.dropna(axis=1))
# df.dropna()
print('-'*50)
# thresh  argument
# And basically what that means is because row 1 had at least two non and a values 2.0 and the two it
# find all Nan values and remove it
print(df.dropna(thresh=2))
print('-'*50)
print(df.dropna(thresh=3))

#A行のNAでない数を平均したり、足したりして埋める
print(df['A'].fillna(value=df['A'].mean()))
print(df['A'].fillna(value=df['A'].sum()))

print('_'*50)
#grouping them

import numpy as np
import pandas as pd

data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charile','Ama','Susume','Sue','Carl'],
        'Sales':[200,400,233,233,565,342]
}

df=pd.DataFrame(data)
print(df)
print('-'*50)
print(df.groupby)

print(df.groupby('Company'))

byComp=df.groupby('Company')
print(byComp)

print(byComp.mean())
print(byComp.sum())
print(byComp.std())

print('-'*50)

print(byComp.sum().loc['FB'])

print('-'*50)

print(df.groupby("Company").sum().loc['MSFT'])

print(df.groupby("Company").count())
print('-'*50)
print(df.groupby("Company").max())
print('-'*50)
print(df.groupby("Company").min())
print('-'*50)

print(byComp.describe())
print('-'*50)
print(df.groupby("Company").describe().transpose())
print('-'*50)
print(df.groupby("Company").describe().transpose()["FB"])

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                    index=[0,1,2,3])


df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                    index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                    index=[8,9,10,11])


print(df1)
print('_'*60)
print(df2)
print('_'*60)
print(df3)
print('_'*60)

# Concatenation
# Concatenation basically glues together DataFrames. Keep in mind that dimensions should
# match along the axis you are concatenating on.You can use pd. concat and pass in a list of
# DataFrames to concatenate together:

print(pd.concat([df1,df2,df3]))
# print(pd.concat([df1,df2,df3],axis=0))
print('_'*60)
print(pd.concat([df1,df2,df3],axis=1))

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A' : ['A0','A1','A2','A3'],
                    'B' : ['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C' : ['C0','C1','C2','C3'],
                    'D' : ['D0','D1','D2','D3']})
print('_'*60)
print(left)
print('_'*60)
print(right)
print('_'*60)
# merging
# the **merge** function allows you to merge DataFrames together using a similar logic as
# merging SQL Tables together. For examle:

# instead of concatinating i will get common elmements
print(pd.merge(left,right,how='inner',on='key'))
# The INNER JOIN selects all rows from both particeipating tables as long as there is a
# match between the columns. An SQL INNER JOIN is same as JOIN clause,combining rows from 
# two or more tables.
print('_'*60)
left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                    'key2':['K0','K1','K0','K1'],
                    'A' : ['A0','A1','A2','A3'],
                    'B' : ['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K1','K2'],
                    'key2':['K0','K0','K0','K0'],
                    'C' : ['C0','C1','C2','C3'],
                    'D' : ['D0','D1','D2','D3']})
print('_'*60)
print(pd.merge(left,right,on=['key1','key2']))
# Outer joins. When performing an inner join, rows from either table that are unmatched in 
# the other table are not returned.In an outer join, unmatched rows in one or both tables 
# can be returned
print('_'*60)
print(pd.merge(left,right,how='outer',on=['key1','key2']))
# inner join はベン図の'かつ'、
# outer join はベン図の'または'、


#operations
print('_'*60)
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

#info on unique values

print(df['col2'].unique())
print(len((df['col2'].unique())))

print(df['col2'].nunique())

# counts how many times repeated
print(df['col2'].value_counts())

print('-'*70)

#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
print('newdf: ', newdf)
print('-'*70)

def times2(x):
    return x*2
print(df['col1'].apply(times2))

print(df['col3'].apply(len))

print(df['col1'].sum())
print(df['col2'].sum())

del df['col1']
print(df)

print('-'*50)

df.columns
print('df.columns:',df.columns)
print('df.index: ', df.index)

#sorting of the data
#inplace= False by default
# 最初はcol2の数字の大きさ順
print(df.sort_values(by='col2'))
# 最初はcol2のアルファベット順
print(df.sort_values(by='col3'))

#boolean values

print(df.isnull())
print('-'*50)

#createing the new dataframe

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
#repeating values present

print(df)
print('-'*50)



