import matplotlib.pyplot as plt

temperatura = [20, 25, 30, 35, 40]
humedad = [40, 35, 30, 25, 20]

# Crear el gráfico de dispersion
plt.scatter(temperatura,humedad)
# Personalizar el gráfico
plt.title('Gráfico de dispersion',loc='left')
plt.xlabel('Temperatura')
plt.ylabel('Humedad') 
# Mostrar el gráfico
plt.show()