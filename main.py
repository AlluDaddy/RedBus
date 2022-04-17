import pandas as pd
import os 
# print(os.path.join(".\\travel.xlsx"))
df = pd.read_excel(os.path.join("travel.xlsx"))
json = df.to_json(orient = 'values')
print(json)