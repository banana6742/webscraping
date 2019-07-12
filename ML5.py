import pandas as pd

left = pd.DataFrame({'A':['A0','A1','A2'],
                     'B':['B0','B1','B2']},
                     index=['K0','K1','K2'])

right = pd.DataFrame({'C':['C0','C1','C2'],
                      'D':['D0','D1','D2']},
                     index=['K0','K2','K3'])

print(left.join(right))

print('-'*80)
print(left.join(right,how='outer'))

import numpy as np
import pandas as pd

df = pd.DataFrame({'First':[100,200,300,400],
                  'Second':[10,20,20,100],
                  'Three':['abc','good','bad','student'],
                  'Four':['FB','Amazon','Microsoft','FlipKart']})

print(df)
print('-'*70)
print('-'*70)

#unique values in data
print(df['Second'].unique)
print('-'*70)

#get the length of the data
print(df['First'].nunique())
print('-'*70)

print(len(df['First'].unique()))
print('-'*70)

print(df['Second'].get_values())

#we can add the second column

print(df['Second'].sum())
print('-'*70)
print(df['Second'].value_counts())
print('-'*70)

#condition selection statements
#true false

print(df['First']>100)
print('-'*70)
print('-'*70)
print('-'*70)


print(df[df['First']>100])
print('-'*70)
# かつ
print(df[(df['First']>0)&(df['First']==100)])
print('-'*70)
# Second列が1000以上、またはFour列がAmazonを抽出
print(df[(df['Second']>1000)|(df['Four']=="Amazon")])
print('-'*70)
print('-'*70)
print('-'*70)

# First列の2乗を行う
def susumu(x):
    return x**2

print(df['First'].apply(susumu))
print('-'*70)

print(df['Four'].apply(len))
print('-'*70)
print('-'*70)

print(df['First'].apply(lambda x:x*2))
print('-'*70)

#dropping the column
print(df.drop('First',axis=1))

#print(df.drop('First',axis=1,inplace=True)
print('-'*70)

print(df.index)
print('-'*60)
print(df.sort_values(by="Three"))
print('-'*70)

print(df.isnull())
print('-'*70)

