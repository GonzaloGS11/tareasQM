import numpy as np
import matplotlib.pyplot as plt

# Definimos los parametros de la funcion
a = 2.0
lambda_value = 0.8

x = np.linspace(-5, 5, 400) # Definimos el rango de valores de x

y = np.sqrt(lambda_value / np.pi) * np.exp(-lambda_value * (x - a)**2) # Definicion de la funcion a graficar

# Grafico 
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\rho (x)$', color='k', alpha= 0.8)
plt.title('Grafico funcion Gaussiana')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.5)

# Ploteo
plt.show()