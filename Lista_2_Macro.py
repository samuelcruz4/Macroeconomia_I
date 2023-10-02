# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:57:55 2023

@author: savia
"""

### Lista 2
### Exercício 2
### a)

## Carregando módulos necessários
import numpy as np
import matplotlib.pyplot as plt


## Definição de Parâmetros
beta, sigma = .98, 2
delta, alpha = .08, .44

barA, a_max, n_a = 0, 60, 100
a_grid = np.linspace(-barA, a_max, n_a)

pi = np.array([[.4, .5, .1],
               [.3, .2, .5],
               [.2, .4, .4]])

y_min, y_max, n_y = 1e-2, 1, len(pi)
y_grid = np.linspace(y_min, y_max, n_y)

rho = 1/beta - 1
r_min, r_max = -delta, rho


## Função utilidade CRRA
def U(x, sigma):
    return (x**(1-sigma) - 1) / (1 - sigma)

def RCE(beta, sigma):
    """ (beta, sigma) --> (r, K_r, w)  """
    V = np.zeros((n_y, n_a))  # Chute inicial da função valor
    d_path, K_path, Ea_path, r_path = [], [], [], []  # Listas para preenchimento

    r_L, r_H = r_min, r_max
    norma_r, tol_r, it = 1, 1e-6, 0
    while norma_r > tol_r:
        it += 1
        # Atualizando valor de r
        r = (r_L+r_H)/2
        # Criando objeto de L-barra para acumular a oferta de trabalho
        barL = 0


        # Definindo guess inicial para distribuição dos tipos, PI.
        PI_bar = np.ones(n_y)
        PI_bar = PI_bar / sum(PI_bar)  # Normalizando


        # Encontrando a distribuição estacionária
        norm_PI, tol_PI = 1, 1e-4
        while norm_PI > tol_PI:
            PI_prime = np.dot(np.transpose(pi), PI_bar)
            norm_PI = np.max(abs(PI_prime - PI_bar))
            PI_bar = PI_prime[:]  # ou np.copy(PI_prime)


        # Acumulando as ofertas de trabalho por tipo, dada distribuição estacionária PI_bar
        for i_y, y in enumerate(y_grid):
            barL += y * PI_bar[i_y]

        # Construção da demanda de capital
        aux = alpha * barL**(1 - alpha) / (r + delta)
        K_r = aux ** (1 / (1 - alpha))


        # Cálculo do salário
        w = (1 - alpha) * (K_r / barL)**alpha


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Preenchimento da função objetivo e construção da função valor (Operador de Bellman)
        norm_V, tol_V = 2, 1e-5
        while norm_V > tol_V:

            # Preenchimento da função objetivo
            F_OBJ = np.zeros((n_y, n_a, n_a))
            for i_a, a in enumerate(a_grid):
                for i_y, y in enumerate(y_grid):
                    for i_aa, aa in enumerate(a_grid):

                        # Cálculo do consumo
                        c = w*y + (1+r)*a - aa

                        # Preenchimento na função objetivo
                        if c <= 0:
                            F_OBJ[i_y, i_a, i_aa] = -np.inf
                        else:
                            F_OBJ[i_y, i_a, i_aa] = U(c, sigma) + beta*np.dot(pi[i_y,:], V[:, i_aa])


            # Construção da função valor (Operador de Bellman)
            TV = np.zeros((n_y, n_a))
            iG = np.zeros((n_y, n_a), dtype=np.int64)

            for i_a, a in enumerate(a_grid):
                for i_y, y in enumerate(y_grid):
                    TV[i_y, i_a] = np.max(F_OBJ[i_y, i_a,:])
                    iG[i_y, i_a] = np.argmax(F_OBJ[i_y, i_a,:])

            norm_V = np.max(abs(TV - V))  # Atualizando valor da norma
            V = TV[:]  # Alterando valor de V para próxima iteração


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Construção da função de transição

        # Empilhando as variáveis de estado em dimensão única
        Q = np.zeros((n_y*n_a, n_y*n_a))  # Importante começar ZERADO!

        # Fixando estado corrente (current)                 
        for i_y in range(n_y):
            for i_a in range(n_a):
                c_state = i_y*n_a + i_a  # encontrando índice em Q (de dimensão única)

                # Fixando próximo estado (next)
                for i_yy in range(n_y):
                    for i_aa in range(n_a):
                        n_state = i_yy*n_a + i_aa

                        # Verificando se há migração para a' para acumular
                        if i_aa == iG[i_y,i_a]:
                            Q[c_state, n_state] += pi[i_y,i_yy]


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Construção da distribuição estacionária
        phi_bar = np.ones(n_y * n_a)  # Minúsculo
        phi_bar = phi_bar / sum(phi_bar)  # Normalizando a 1

        norm_phi, tol_phi = 1, 1e-4
        while norm_phi > tol_phi:
            phi_prime = np.dot(np.transpose(Q), phi_bar)
            norm_phi = np.max(abs(phi_prime - phi_bar))
            phi_bar = phi_prime[:]


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Construção da oferta de capital Ea
        Ea_r = 0

        for i_a, a in enumerate(a_grid):
            for i_y, y in enumerate(y_grid):
                c_state = i_a + (n_a * i_y)
                i_aa = iG[i_y, i_a]
                aa = a_grid[i_aa]
                Ea_r += aa * phi_bar[c_state]


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Construção do excesso de demanda do capital
        d_r = K_r - Ea_r


        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # # Guardando os resultados
        d_path.append(d_r)
        K_path.append(K_r)
        Ea_path.append(Ea_r)
        r_path.append(r)

        if d_r > 0:
            r_L = r
        elif d_r < 0:
            r_H = r

        norma_r = r_H - r_L

    
    return r, K_r, w


# Usando a função construída para resolver o problema
r_ss, K_r_ss, w_ss = RCE(beta, sigma)

# print some info
print("-"*100)
print(" The interest rate is:", r_ss)
print("\n The capital-labor rate is:", K_r_ss)  # Aqui deveria ser valor de k
print("\n The wage rate is:", w_ss)
print("-"*100)


#item b

beta_grid = np.linspace(0.7, 0.98, 3)
tab_beta = np.zeros((len(beta_grid), 2))

for i_beta, beta in enumerate(beta_grid):
    tab_beta[i_beta, 0] = beta
    tab_beta[i_beta, 1] = RCE(beta, sigma)[0]
    print(np.round(tab_beta[i_beta], 5))

plt.plot(tab_beta[:, 0], tab_beta[:, 1])



sigma_grid = np.linspace(0.5, 2, 3)
tab_sigma = np.zeros((len(sigma_grid), 2))

for i_sigma, sigma in enumerate(sigma_grid):
    tab_sigma[i_sigma, 0] = sigma
    tab_sigma[i_sigma, 1] = RCE(beta, sigma)[0]
    print(np.round(tab_sigma[i_sigma], 5))

plt.plot(tab_sigma[:, 0], tab_sigma[:, 1])