import pandas as pd

print(pd.read_csv('example.csv'))
# to write
print('-'*60)
df=pd.read_csv('example.csv')
print(df)

print('-'*40)
# df.to_csv('My_output')
# df.to_csv('My_output.csv')
# print(pd.read_csv('My_output.csv'))

# read= pd.read_excel('Book2.xlsx',sheet_name='2011census')
# print(read)
# df.to_excel('example.xlsx',sheet_name='NewSheet')

data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

# print(type(data))

print(data[0].head())

# print(df[0])

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('data',engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)