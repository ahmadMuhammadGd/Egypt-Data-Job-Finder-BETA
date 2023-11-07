import job_classifier
import pandas as pd

'''
df = pd.read_csv('..\data\df.csv')

job_classifier.classify_rows(data_frame=df, column_name='title')


df = df[['title', 'Class', 'score']]
df.to_csv('logs.csv', index=False)'''

df = pd.read_csv('..\data\df.csv')
condition = df['City']=='Tanta'
print (df[condition] )