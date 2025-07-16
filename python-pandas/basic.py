import pandas as pd

datasets = {
    "name":['prabhu','rohit','pramod'],
    "email":['a@','b@','b@'],
    "salry":[10,20,30]
}

result = pd.DataFrame(datasets)
result.to_csv('data.csv',index=False)
print(result)

print(result.loc[0])

