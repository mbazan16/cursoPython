import pandas as pd

datos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Luis', 'Ana','Lucas','Ines','Leo'],
    'Edad': [25, 30, 18, 40, 35,23,65,34],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao','Madrid', 'Barcelona', 'Sevilla']
}

df = pd.DataFrame(datos)
print("------------------ 5 primeros ------------------")
print(df.head())#Por defecto son los 5 primeros
print("------------------ 7 primeros ------------------")
print(df.head(7)) #  7 primeros
print("------------------ 7 primeros Slicing ------------------")
print(df[:7]) #  7 primeros
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

