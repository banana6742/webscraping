import pandas as pd
import numpy as np
labels = ['a','b','c','d','e']
my_data = [10,20,30,40,50]

arr=np.array(my_data)

d= {'a':10,'b':20,'c':30,'d':40,'e':50}
print('__________________________________________')

print(pd.Series(data=my_data))
print('__________________________________________')
#i want to have index as a,b,c.....

print(pd.Series(data=my_data,index=labels))
print('__________________________________________')

print(pd.Series(my_data,labels))
# 順番を変えてみる。データ→ラベルの順番
print(pd.Series(labels,my_data))
print('__________________________________________')
# simple way to create the Series
print(pd.Series(arr))

print('__________________________________________')
print(pd.Series(arr,labels))

print('__________________________________________')
print(pd.Series(d))

# for index values as values
print(pd.Series(data=labels))
print('__________________________________________')

# lets create the series with country names
ser1 = pd.Series([1,2,3,4,5],['USA','GERMANY','USSR','JAPAN','TURKEY'])
print(ser1)

ser2 = pd.Series([1,2,4,6,7],['USA','GERMANY','ITALY','FRANCE','INDIA'])
print(ser2)

print('__________________________________________')

ser3 = ser1 +ser2
print(ser3)

import numpy as np
import pandas as pd 
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print('__________________________________________')

print(df['W'])
print(df['Z'])
print('__________________________________________')

#lets check the datatype

print(type(df['W']))
print('__________________________________________')
#some more ways u can extract the data

print(df.W)
print(df.Z)
print('__________________________________________')
# 2つのリストを作るときは[[]]二重括弧で閉じる
print(df[['X','Y']])
print('__________________________________________')

# try to add new column in the dataframe 
df['new']= df['W']+df['Y']
print(df['new'])
print(df)

#dropping the dataframe columns
# print(df.drop('new'))
#axis=1は存在している列 
# axisかcolumnsのどちらかを使用する
# print(df.drop('new',axis=1))
# if itis true = 
# print(df.drop('new',axis=1,inplace=True))
print(df.drop('new',axis=1,inplace=False))
print('__________________________________________')

# lets delete the rows
# axis=1 is vertical axis=0 is horizontal
print(df.drop('E',axis=0))
print('__________________________________________')
print(df.drop('D',axis=0))

print(df.drop(['D','E'],axis=0))
print('__________________________________________')
print(df.loc['A'])
print('__________________________________________')
print(df.iloc[2])
print('__________________________________________')
print(df.loc['B','Y'])

print(df.loc[['A','B'],['W','Y']])

print('__________________________________________')
print('condition Selection')
print(df)
print(df>0)

print('__________________________________________')
print(df[df>0])
print('__________________________________________')

#particular values within the column
print(df[df['W']>0])
print('__________________________________________')
print(df[df['W']>1])
print('__________________________________________')
print(df[df['W']>0]['Y'])
print('__________________________________________')
print(df[df['W']>0][['Y','X']])
print('__________________________________________')
#take two conditons with and(&) with paranthesis
print(df[(df['W']>0) & (df['Y']>0)])
print('__________________________________________')
print(df)
# reset the default index values 1,2,3,4,5,............
print(df.reset_index())
print('__________________________________________')
newind='CA NY WY OR CO'.split()
print(newind)
print('__________________________________________')
df['States']=newind
print(df)
print('__________________________________________')
print(df.set_index('States'))

#Multi -Index and Index Hierachy
# index levels
outside = ['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
print('__________________________________________')

df=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)
print('__________________________________________')
#select the perticular
print(df.loc['G1'])
print('__________________________________________')

#this is slicing
print(df.loc['G1'].loc[1])
print('__________________________________________')
# Im adding the index name to the dataframes
print(df.index.names)
df.index.names=['Group','Num']
print(df)
print(df.index.names)
print(df.xs('G1'))
print('__________________________________________')
# selecting by G1 and also by there index values
print(df.xs(['G1',1]))
print('__________________________________________')
print(df.xs(['G1',3]))

print(df.xs(1,level='Num'))

f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal Append:\n',np.vstack((f,g)))
print('Horizontal Append:',np.hstack((f,g)))
    