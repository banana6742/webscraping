import pandas as pd

print(pd.read_csv('example.csv'))
# to write
print('-'*60)
df=pd.read_csv('example.csv')
print(df)

print('-'*40)
# df.to_csv('My_output')
df.to_csv('My_output.csv')
print(pd.read_csv('My_output.csv'))


print('-'*40)
df.to_csv('My_output.csv',index=False)
print(pd.read_csv('My_output.csv'))

pd.read_excel('Book2.xlsx',sheet_name='Sheet1')