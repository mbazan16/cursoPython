import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
ventas = [120, 85, 95, 150, 110]

# Crear el gráfico de barras
plt.bar(meses, ventas,align='center') 
# Personalizar el gráfico
plt.title('Gráfico en barras',loc='left')
plt.xlabel('Meses')
plt.ylabel('Ventas') 
# Mostrar el gráfico
plt.show()