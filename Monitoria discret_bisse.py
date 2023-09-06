# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:26:24 2023

@author: savia
"""

# importando os pacotes requeridos
import numpy as np
import matplotlib.pyplot as plt
# definição de parametros e objetos ####################################
beta, delta = .58, 5
y = 38
n_c = 46
c_grid = np.linspace(0,y,n_c)

## Definição das funçoes  ####################################################
def F(x):
    deriv = x**(-delta) - beta*( (y-x)**(-delta) )
    return deriv

# F = lambda x: x**(-delta) - beta*( (y-x)**(-delta) )
#############################################################################
# Método Discretização
# F = []
F_grid = np.zeros( n_c )
# for c in c_grid:
# for i_c in range(n_c):
#     c = c_grid[i_c]
for i_c, c in enumerate(c_grid):
    F_grid[i_c] =  c**(-delta) - beta*( (y-c)**(-delta) ) 

i_c_star_new = np.argmin(abs(F_grid))
c_star_new = c_grid[i_c_star_new]

# Visualizando a derivada da objetivo
fig, ax = plt.subplots()
ax.plot(c_grid, F_grid)
ax.plot(c_grid, [0]*n_c, 'r')
plt.show()

# Método Bisection
c_min, c_max = 0, y
F_tol, c_tol = 1e-3, 1e-7
while True:
    c_med = (c_min+c_max)/2
    
    F_med = F(c_med)
    print(F_med,'[',c_min,c_med,c_max,']')
    
    if F_med < 0:
        c_max = c_med
    elif F_med > 0:
        c_min = c_med
    if abs(F_med)<F_tol and abs(c_max-c_min)<c_tol:
        break
            



# Solução Analítica
c_star = y / (1+beta**(1/delta))

print('Consumo ótimo: ',c_star)
print('Consumo ótimo (aproximado por discretização): ',c_star_new)
print('Consumo ótimo (aproximado por bisection): ',c_med)

