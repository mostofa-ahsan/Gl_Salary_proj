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


#GL_data['Job_City']=GL_data['Location'].apply(lambda x: x.split(',')[0])



# us_state_abbrev = {
# 'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
# 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
# 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
# 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
# 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
# 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
# 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
# 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
# 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

GL_data['Job_State_cleaned']=GL_data['Location'].apply(lambda x: x.split(',')[1] if ',' in x else x)
GL_data.Job_State_cleaned.value_counts()


#GL_data['Job_State_cleaned'] =GL_data['Job_State_cleaned'].map(us_state_abbrev)

GL_data['Job_State_cleaned']=GL_data['Job_State_cleaned'].apply(lambda x: ' UT'if 'utah' in x.lower()else x)

GL_data['Job_State_cleaned']=GL_data['Job_State_cleaned'].apply(lambda x: ' MO'if 'missouri' in x.lower()else x)
GL_data['Job_State_cleaned']=GL_data['Job_State_cleaned'].apply(lambda x: ' NJ'if 'new jersey' in x.lower()else x)
GL_data['Job_State_cleaned']=GL_data['Job_State_cleaned'].apply(lambda x: ' VA'if 'virginia' in x.lower()else x)
GL_data['Job_State_cleaned']=GL_data['Job_State_cleaned'].apply(lambda x: ' CA'if 'california' in x.lower()else x)
##Company Age


GL_data['Age']=GL_data.Founded.apply(lambda x:x if x<1 else 2020-x)
##Company Size


##Job Description


PYTHON=['python', 'django', 'pandas', 'numpy', 'matplotlib', 'seaborn','sklearn','scikit']
GL_data['Python']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in PYTHON) else 0)


SQL=['sql','query','queries']
GL_data['SQL']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in SQL) else 0)


AWS=['aws','lambda', 'ec2', 'ec3', 'dynamo db', 'redshift','kinesis','quicksight','glue','athena']
GL_data['AWS']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in AWS) else 0)


AZURE= ['azure', 'data lake', 'data lakes', 'databrick', 'databricks', 'hdinsight', 'data factory' ]
GL_data['AZURE']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in AZURE) else 0)

BIG_DATA = ['big data', 'spark', 'pyspark', 'hadoop', 'hive', 'hiveql','mapreduce', 'yarn','hdfs','cassandra','hbase','alluxio','graphx']
GL_data['BIG_DATA']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in BIG_DATA) else 0)

Computer_Vision=['opencv','image','video','pytorch','yolo','computer vision', 'object detection']
GL_data['Computer_Vision']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in Computer_Vision) else 0)

R=['r', 'alteryx', 'r shiny', ' r ' ,' r,' , 'r studio']
GL_data['R']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in R) else 0)


Visualization = ['tableau','power bi','power-bi','visualization', 'chart', 'graph']
GL_data['Visualization']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in Visualization) else 0)


GL_data['Tableau']=GL_data['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower()else 0)
GL_data['Power BI']=GL_data['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower()else 0)

Machine_Learning=['machine learning', 'tensorflow','prediction', 'ml', 'linear regression', 'logistic regression',
                  'random forest', 'naive bayes','xgboost','support vector machine', 'svm', 'glm' 'model build', 'bagging', 'boosting',
                  'parameter tuning','hyperparameter','algorithm', 'supervised', 'unsupervised' ]
GL_data['Machine_Learning']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in Machine_Learning) else 0)


STATISTICS=['statitical','p value','bayesian','time series', 'timeseries', 'sap','spss',
            'anova','regression','statistics','t test', 'f test']
GL_data['STATISTICS']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in STATISTICS) else 0)


Deep_Learning=['deep learning', 'cnn', 'convolutional', 'neural', 'network', 'rnn', 'lstm', 'gru', 'gan']
GL_data['Deep Learning']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in Deep_Learning) else 0)

GL_data['EXCEL']=GL_data['Job Description'].apply(lambda x: 1 if 'excel' in x.lower()else 0)

model_deployment=['flask','docker', 'api', 'kubernetes', 'container', 'classifier', 'heroku', 'streamlit', 'pipeline'] 

GL_data['Deployment']=GL_data['Job Description'].apply(lambda x: 1 if any( e in x.lower() for e in model_deployment) else 0)


# GL_data['DOCKER']=GL_data['Job Description'].apply(lambda x: 1 if 'docker'in x.lower()else 0)


