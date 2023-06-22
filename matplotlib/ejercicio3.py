import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May','Jun','Jul','Ag','Sep','Oct','Nov','Dic']
ventas = []

for mes in meses:
    venta=float(input(f'Ventas para el mes {mes}: '))
    ventas.append(venta)

# Crear el gráfico de barras
plt.bar(meses, ventas,align='center') 
# Personalizar el gráfico
plt.title('Gráfico en barras',loc='left')
plt.xlabel('Meses')
plt.ylabel('Ventas') 
# Mostrar el gráfico
plt.show()