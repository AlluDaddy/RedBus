import pandas as pd
import os 
df = pd.read_excel(os.path.join("testdata\\travel.xlsx"))
json = df.to_json(orient = 'values')
print(json)