# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:47:13 2020

@author: mosto
"""
import pandas as pd
GL_data= pd.read_csv("C:\\Users\\mosto\\REPOSITORY\\Gl_Salary_proj\\glassdoor_data.csv")
#GL_data.head(5)




##Cleaning Salary

GL_data=GL_data[GL_data['Salary Estimate']!='-1']
salary= GL_data['Salary Estimate'].apply(lambda x:x.split('(')[0])
minus_k=salary.apply(lambda x:x.replace('K','').replace('$',''))

GL_data['hourly']=GL_data['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower()else 0)

GL_data['Min_salary']=minus_k.apply(lambda x: int(x.split('-')[0]))
GL_data['Max_salary']=minus_k.apply(lambda x: int(x.split('-')[1]))
GL_data['Avg_salary']=(GL_data.Min_salary + GL_data.Max_salary)/2




##Clean Company name


GL_data['Company_Name_Cleaned']=GL_data.apply(lambda x: x['Company Name'] if int(x['Rating'])<0 else x['Company Name'][:-3], axis=1 )




##Location [City, State]


GL_data['Job_City']=GL_data['Location'].apply(lambda x: x.split(',')[0])
GL_data['Job_State']=GL_data['Location'].apply(lambda x: x.split(',')[1])
GL_data.Job_State.value_counts()


##Company Age
##Company Size
