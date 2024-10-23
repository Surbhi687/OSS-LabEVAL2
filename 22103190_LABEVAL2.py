
from pymongo import MongoClient
import pandas as pd

data = pd.read_csv('C:\Users\22103190\Downloads\Inpatient_Rehabilitation_Facility-General_Information_Sep2024.csv')
df = pd.DataFrame(data, columns = [' '])
print(df.head())

client = MongoClient('mongodb://localhost:12701/')
db = client['C:\Users\22103190\Downloads\Inpatient_Rehabilitation_Facility-General_Information_Sep2024.csv']
collection = db['PatientInfo']

df['Certification Date'] = pd.to_datetime(df['Certification Date'])
nonprofit = df[(df['Ownership Type']=='Non-Profit') & (df['Certification Date'] > '10-01-2011' )]

profit = df[(df['City']=='BIRMINGHAM')&(df['Ownership Type']=='For Profit')]
print(profit)

zipcode = df[(df['ZIP Code']>= 85000) & (df['ZIP Code'] <=90000)]
print(zipcode)


numnonprofit = df[df['Ownership Type']=='Non-Profit']
len1 = int(len(numnonprofit))
print(f"Number of non profit providers:{len1}")


numprofit = df[df['Ownership Type']=='For Profit']
len2 = int(len(numprofit))
print(f"Number of profit providers:{len2}")
