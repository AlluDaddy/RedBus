import pandas as pd
df = pd.read_excel("C:\\Users\\APraveen\\PycharmProjects\\mainproj\\RedBus\\testdata\\travel.xlsx")
json = df.to_json(orient = 'values')
print(json)