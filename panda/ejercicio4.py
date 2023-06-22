import pandas as pd



df = pd.read_csv('datos.csv')

df_filtrado = df[df['Edad']>30] #Condicion: df['Edad']>30
print(df_filtrado)





