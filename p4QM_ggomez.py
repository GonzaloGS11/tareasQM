import numpy as np
import matplotlib.pyplot as plt

# Definimos los parametros de la funcion
a = 2.0
lambda_value = 0.8

x = np.linspace(-5, 5, 400) # Definimos el rango de valores de x

y = (lambda_value) * np.exp(-2*lambda_value * (abs(x))) # Densidad de probabilidad

xx = 1/(2*(lambda_value)**2) # esto es <x^2>
x_1 = 0 # esto es <x> ==> <x>^2 = 0

sigma = np.sqrt(xx)

# Grafico de la función
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\rho (x)$', color='k', alpha= 0.8)

# Grafico de +- sigma
plt.axvline(x= -sigma, color='r', linestyle='-.', label='$-\sigma$')
plt.axvline(x= sigma, color='r', linestyle='--', label='$+\sigma$')

plt.title('Grafico funcion Gaussiana')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.5)

# Ploteo
plt.show()