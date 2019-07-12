#Im using the kaggle dataset
#Import pandas as pd**
import pandas as pd

#**Read Salaries.csv as a dataframe called sal**.
sal = pd.read_csv('Salaries.csv')

# print(sal)
print(sal.head())
#Check the head of the DataFrame/**
print(sal.info)

# what is the average BasePay?
print(sal['BasePay'].mean())

# what is the highest amount of overtimepay in the dataset?
print(sal['OvertimePay'].max())

# what is the job title of JOSEPH DRISCOLL? 
# Im using the kaggle dataset


# ** Import pandas as pd.**
import pandas as pd

# ** Read Salaries.csv as a dataframe called sal.**
sal=pd.read_csv('Salaries.csv')
print(sal)
print('------------------------------')

# ** Check the head of the DataFrame. **

print(sal.head())
# ** Use the .info() method to find out how many entries there are.**
print('------------------------------')

print(sal.info)

# What is the average BasePay ?
print(sal['BasePay'].mean())

# ** What is the highest amount of OvertimePay in the dataset ? **
print(sal['OvertimePay'].max())
# ** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
# ** How much does JOSEPH DRISCOLL make (including benefits)? **
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
# ** What is the name of highest paid person (including benefits)?**
# print(sal['TotalPayBenefits'].max())
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()])
# print(sal.loc[sal['TotalPayBenefits'].idxmax()])

# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**
# print(sal['TotalPayBenefits'].min())
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()])


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
# print(sal[sal['Year']=='2011:2014']['BasePay'].mean())
print(sal.groupby('Year').mean()['BasePay'])
# ** How many unique job titles are there? **
# print(sal['JobTitle'].unique)
print(sal['JobTitle'].nunique())
# ** What are the top 5 most common jobs? **
print(sal['JobTitle'].value_counts().head())

# ** How many people have the word Chief in their job title? (This is pretty tricky) **



# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **
