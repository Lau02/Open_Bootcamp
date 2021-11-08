import pandas as pd


file = 'datos.xlsx'

df = pd.read_excel(file)

list = df['email'].unique()

print(list)

