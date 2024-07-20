import pandas as pd

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

df = pd.DataFrame(data)

excel_file = 'output.xlsx'
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created successfully.")
