import pandas as pd

df = pd.read_csv('data.csv')
print(df)
df['isyoung']= False
df = df.drop_duplicates(subset='email',keep='first')
df = df.to_csv('data.csv',index=False)
print(df)
