import pandas as pd



df = pd.read_csv('datos.csv')

print(df.groupby('Ciudad')['Edad'].mean().reset_index(name='Media Edad'))





