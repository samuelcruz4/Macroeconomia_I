# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:04:00 2023

@author: savia
"""

##############################################################
# Importação de módulos/pacotes
##############################################################
import numpy as np
import matplotlib.pyplot as plt

##############################################################
# Definição de parâmetros e objetos
##############################################################
beta, sigma = .95, 10
delta, alpha = .04, .3

barA, a_max, n_a = 0, 20, 20
a_grid = np.linspace( -barA, a_max, n_a )

pi = np.array([ [2/3, 1/3],
                [1/3, 2/3]])

y_min, y_max, n_y = 1, 5, len(pi)
y_grid = np.linspace( y_min, y_max, n_y )

rho = 1/beta - 1
r_min, r_max, n_r = -delta, rho, 20
r_grid = np.linspace( r_min, r_max, n_r )


##############################################################
# Definição de funções
##############################################################
def U(x):
    return (x**(1-sigma) - 1) / (1-sigma)
# U = lambda x: (x**(1-sigma) - 1) / (1-sigma)


V = np.zeros( (n_y, n_a) )


##############################################################
# Construção da distribuição estacionária de \pi
##############################################################
# definindo guess inicial para phi_bar
PI_bar = np.ones( n_y )
PI_bar = PI_bar / sum(PI_bar)

norm_PI, tol_PI = 1, 1e-4
while norm_PI>tol_PI:
    PI_prime = np.dot( np.transpose(pi) , PI_bar )
    norm_PI = np.max(abs(PI_prime - PI_bar))
    PI_bar = np.copy(PI_prime)

##############################################################
# Construção da oferta agregada de trabalho
##############################################################
barL = 0
for i_y, y in enumerate(y_grid):
    barL += y * PI_bar[i_y]


d_path, K_path, Ea_path = [], [], []

for i_r, r in enumerate(r_grid):
    print('taxa juros: ',r)
    ##############################################################
    # Construção da demanda de capital
    ##############################################################
    # F(K,L) = K^\alpha * L^(1-\alpha)
    # F_k(K,L) =\alpha K^(\alpha-1) * L^(1-\alpha)
    # r + delta = F_k(K_r, barL) = \alpha K_r^(\alpha-1) * barL^(1-\alpha)
    # K_r^(1-\alpha) =  \alpha  * barL^(1-\alpha) / (r + delta)
    # K_r = ( \alpha  * barL^(1-\alpha) / (r + delta) ) ^ ( \frac{1}{(1-\alpha)} )
    aux = alpha  * (barL**(1-alpha)) / (r + delta)
    K_r = aux ** ( 1/(1-alpha) )
    
    
    # F(K,L) = K^\alpha * L^(1-\alpha)
    # F_L(K,L) =(1-\alpha) K^\alpha * L^(-\alpha)
    # w = F_L(K_r, barL) = (1-\alpha) K^\alpha * L^(-\alpha)
    w = (1-alpha) * (K_r / barL) ** alpha
    
    
    
    ##############################################################
    # Problema do consumidor
    ##############################################################
    norm_V, tol_V = 2, 1e-5
    while norm_V>tol_V:
        print('norma convergência: ',norm_V)
        ##############################################################
        # Construção da função objetivo
        ##############################################################
        F_OBJ = np.zeros( (n_y, n_a, n_a) )
        for i_a in range(n_a):
            a = a_grid[i_a]
            for i_y in range(n_y):
                y = y_grid[i_y]
                for i_aa in range(n_a):
                    aa = a_grid[i_aa]
                    
                    c = w * y + (1+r) * a - aa
                    if c<=0:
                        F_OBJ[i_y, i_a, i_aa] = - np.inf 
                    else:
                        F_OBJ[i_y, i_a, i_aa] = U(c) + beta * np.dot( pi[i_y, :] , V[:, i_aa] )
                    
                    
        ##############################################################
        # Construção da função valor (operador Bellman)
        ##############################################################   
        TV = np.zeros( (n_y, n_a) )
        iG = np.zeros( (n_y, n_a), dtype=int )
        
        for i_a, a in enumerate(a_grid):
        # for i_a in range(n_a):
        #     a = a_grid[i_a]
            for i_y, y in enumerate(y_grid):
            # for i_y in range(n_y):
            #     y = y_grid[i_y]
                TV[i_y, i_a] = np.max( F_OBJ[i_y, i_a, :] )
                iG[i_y, i_a] = np.argmax( F_OBJ[i_y, i_a, :] )         
        
        norm_V = np.max(abs(TV-V))
        # print(norm_V)
        V = np.copy(TV)
    
    
    ##############################################################
    # Construção da função de transição
    ############################################################## 
    
    # Empilhando as variáveis de estado
    # [ (y_0, a_0), (y_0, a_1), (y_0, a_2), (y_0, a_3), (y_0, a_4),
    #   (y_1, a_0), (y_1, a_1), (y_1, a_2), (y_1, a_3), (y_1, a_4)]
    # [ (y'_0, a'_0), (y'_0, a'_1), (y'_0, a'_2), (y'_0, a'_3), (y'_0, a'_4),
    #   (y'_1, a'_0), (y'_1, a'_1), (y'_1, a'_2), (y'_1, a'_3), (y'_1, a'_4)]
    Q = np.zeros( ( n_y*n_a , n_y*n_a ) )
    # Fixando o 'current state'
    for i_a, a in enumerate(a_grid):
        for i_y, y in enumerate(y_grid):
            c_state = i_a + n_a * i_y
            # Fixando o 'next state'
            for i_aa, aa in enumerate(a_grid):
                for i_yy, yy in enumerate(y_grid):
                    n_state = i_aa + n_a * i_yy
                    # Verificando se há migração para aa
                    if iG[i_y, i_a] == i_aa:
                        # Q ( (a,y), (a', y') )
                        Q[c_state, n_state] += pi[i_y, i_yy]
                    else:
                        Q[c_state, n_state] += 0
    
    # Q _(mxn)
    # operador linear definido por Q * v mapeia R^n em R^m
                        
    ##############################################################
    # Construção da distribuição estacionária
    ##############################################################
    # definindo guess inicial para phi_bar
    phi_bar = np.ones( n_y*n_a )
    phi_bar = phi_bar / sum(phi_bar)
    # phi_bar /= sum(phi_bar)
    
    norm_phi, tol_phi = 1, 1e-4
    while norm_phi>tol_phi:
        print('searching for invariant distribution: ',norm_phi)
        # phi_prime = np.transpose(Q) * phi_bar
        phi_prime = np.dot( np.transpose(Q) , phi_bar )
        norm_phi = np.max(abs(phi_prime - phi_bar))
        phi_bar = np.copy(phi_prime)
    
    

    print('invariant distribution was found')
    ##############################################################
    # Construção da oferta de capital
    ##############################################################
    Ea_r = 0
    for i_a, a in enumerate(a_grid):
        for i_y, y in enumerate(y_grid):
            c_state = i_a + n_a * i_y
            i_aa = iG[i_y, i_a]
            aa = a_grid[i_aa]
            Ea_r += aa * phi_bar[c_state]
    
    ##############################################################
    # Construção do excesso de demanda do capital
    ##############################################################
    d_r = K_r - Ea_r
    d_path.append(d_r)
    K_path.append(K_r)
    Ea_path.append(Ea_r)
    print('excesso de demanda foi construido')

print('vejamos graficamente o excesso de demanda')
fig, ax = plt.subplots()
ax.plot(r_grid, Ea_path)
# plt.plot(r_grid, K_path)
# plt.plot(r_grid, d_path)
# plt.plot(r_grid, [0]*n_r, 'r--')
plt.show()