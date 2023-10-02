# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:51:48 2023

@author: savia
"""
## a)
def bisecao_a(func, interv, tol):
    """ (Função, [limite inferior, limite superior], tolerância) -> raiz """
    x_H = interv[1]
    x_L = interv[0]
    norm = x_H - x_L
    
    while norm > tol:
        x_m = (x_H + x_L) / 2
        
        if func(x_m) > 0:
            x_L = x_m
        else:
            x_H = x_m
            
        norm = x_H - x_L
        
    return x_m

### b)
    
## definindo inicialmente a função que nos foi dada
def func_b(x):
    return x**3 - 10*x**2 + 5

# Agora aplicando esta função a nossa função da bissecao criada anteriormente

raiz_b = bisecao_a(func_b, [0,1], 1e-10)

### Testando nossa raiz

print(round(func_b(raiz_b), 5))



#### c)
##A cada iteração, o tamanho do intervalo cai pela metade, então precisamos calcular quantas iterações 
## são necessárias para que o intervalo fique menor do que a tolerância dada. 
## tol = (xH - xL)/2**n --> 2**n = (xH-xL)/tol ---> log_2((xH-xL)/tol) = n


from math import log as log  # Para usar função log()
from math import ceil as ceil  # Para usar função ceil(): retorna 1º nº inteiro acima de um número dado


def bisecao_c(func, interv, tol):
    """ (Função, [limite inferior, limite superior], tolerância) -> raiz """
    x_H = 1
    x_L = 0
    norm = x_H - x_L
    ## ceil arredonda o número para cima
    n = ceil(log((x_H - x_L) / tol, 2))  # Quantidade de iterações
    
    for i in range(n):
        x_m = (x_H + x_L) / 2
        
        if func(x_m) > 0:
            x_L = x_m
        else:
            x_H = x_m
        
    return x_m


# Aplicando a função bisecao() com a função dada
raiz_c = bisecao_c(func_b, [0, 1], 1e-10)

# Confirmando que a nova função produz o mesmo resultado do calculado no item (b)
print("Raiz do item (b) =", round(raiz_b, 10), "=", round(raiz_c, 10), "= Raiz do item (c)")







##### Exercício 3

import numpy as np
##############################################################
# Construção da distribuição estacionária de \pi
##############################################################

pi = np.array([ [2/3, 1/3],
                [1/3, 2/3]])
    
    
# definindo guess inicial para phi_bar
PI_bar = np.array([5/6, 1/6])


norm_PI, tol_PI = 1, 1e-4

while norm_PI>tol_PI:
    PI_prime = np.dot( np.transpose(pi) , PI_bar )
    norm_PI = np.max(abs(PI_prime - PI_bar))
    PI_bar = np.copy(PI_prime)
    
print(PI_bar)