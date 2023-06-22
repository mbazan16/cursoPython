import pandas as pd



df = pd.read_csv('datos.csv')
print("------------------ 5 primeros ------------------")
print(df.head())#Por defecto son los 5 primeros
print("------------------ 10 primeros ------------------")
print(df.head(10)) 
print("------------------ 10 primeros Slicing ------------------")
print(df[:10]) 
print("------------------ Cogemos los pares ------------------")
print(df[::2]) 
print("------------------ 7 ultimos ------------------")
print(df.tail(7)) #  7 ultimos
print("------------------ 7 ultimos  Slicing ------------------")
print(df[7:0:-1]) #  7 ultimos
print("------------------ Al reves ------------------")
print(df[::-1]) 
print("----------------- Nombres -------------------------")
print(df['Nombre'])


