# -*- coding: utf-8 -*-
"""
Monitoria 04/06/2023 

"""

# Importando os módulos necessários
import numpy as np  # NumPy com o "apelido" np
from math import log as log  # Apenas função log do módulo math
import matplotlib.pyplot as plt  # Módulo para fazer gráficos


##############################################################################
""" Exercício 2 """

# Fazendo as suposições iniciais 
k_grid = np.linspace(4, 6, 201)  # Possíveis valores de k e k'
beta = 1 / 1.05
alpha = 0.3
delta = 0.05
sigma = 1  # Para itens (c) e (d), usar 1; para item (e), usar 0.5 e 2
z = 1

n_k = len(k_grid)  # Tamanho do vetor de valores de k e k'

# Criando lista de arrays de função valor e função política
v0 = np.zeros(n_k)
vn = [v0]

g0 = np.zeros(n_k)
gn = [g0]


# Loop das iterações enquanto (while) é menor do que dada distância
tol_norma = 1e-5  # Tolerância de distância entre funções valor (0.00001)
norma = np.inf  # Valor inicial da norma = infinito
n = 0  # Contador de iterações

while norma > tol_norma: 
    # Aplicar a cada iteração Operador de Bellman em objetos genéricos Tv e Tg
    Tv = np.zeros(n_k)
    Tg = np.zeros(n_k)
    f_obj = np.zeros((n_k, n_k))
    n += 1
    
    for i in range(n_k):
        for j in range(n_k):
            if k_grid[j] >= 0 and k_grid[j] <= z*k_grid[i]**alpha + (1 - delta)*k_grid[i]:
                if sigma == 1:  # Utilidade na forma log
                    f_obj[i,j] = log(z*k_grid[i]**alpha + (1 - delta)*k_grid[i] - k_grid[j]) + beta*vn[n-1][j]
                else:  # Utilidade na forma de razão
                    f_obj[i,j] = ((z*k_grid[i]**alpha + (1 - delta)*k_grid[i] - k_grid[j])**(1 - sigma) - 1) / (1 - sigma) + beta*vn[n-1][j]
            else:
                f_obj[i,j] = - np.inf
        Tv[i] = np.max(f_obj[i,:])
        Tg[i] = np.argmax(f_obj[i,:])
        
    # Quando acabar loop de linha, jogar função valor em vn e política em gn
    vn.append(Tv)
    gn.append(Tg)
    norma = max(abs(vn[n] - vn[n-1]))


# Trocando índice em gn por valores de k'
for indice in gn:
    for i in range(len(indice)):
        indice[i] = k_grid[int(indice[i])]


# Visualização gráfica da convergência da função valor
fig, ax = plt.subplots()

# Inclusão de cada função valor no gráfico
ax.plot(k_grid, vn[0], label='$v_0$')
ax.plot(k_grid, vn[1], label='$v_1$')
ax.plot(k_grid, vn[2], label='$v_2$')
ax.plot(k_grid, vn[4], label='$v_4$')
ax.plot(k_grid, vn[10], label='$v_{10}$')
ax.plot(k_grid, vn[25], label='$v_{25}$')
ax.plot(k_grid, vn[50], label='$v_{50}$')
ax.plot(k_grid, vn[100], label='$v_{100}$')
ax.plot(k_grid, vn[n], label='$v_{convergido}$')

# Legendas
ax.set_xlabel('Capital')
ax.set_ylabel('Função Valor')
ax.set_title('Convergência da Função Valor')
ax.legend()

plt.show()


# Visualização gráfica da convergência da função política
fig, ax = plt.subplots()

# Inclusão de cada função valor no gráfico
ax.plot(k_grid, gn[1], label='$g_1$')
ax.plot(k_grid, gn[2], label='$g_2$')
ax.plot(k_grid, gn[3], label='$g_5$')
ax.plot(k_grid, gn[10], label='$g_{10}$')
ax.plot(k_grid, gn[n], label='$g_{convergido}$')
ax.plot(k_grid, k_grid, '--', label='45 graus')

# Limites do gráfico
# ax.set_ylim([4.5, 5.3])  # tamanho mínimo e máximo vertical
# ax.set_xlim([4.5, 5.3])  # tamanho mínimo e máximo horizontal

# Legendas
ax.set_xlabel('Capital')
ax.set_ylabel('Função Política')
ax.set_title('Convergência da Função Política')
ax.legend()

plt.show()


# Encontrar numericamente o capital estocástico k*
p = int(np.round(np.random.uniform(0, n_k - 1, size = 1), 0))  # aleatório
print("Índice inicial do capital (aleatorizado):", p)  # Índice randomizado

while k_grid[p] != gn[n][p]:  # até termos k = k'
    p = np.where(k_grid == gn[n][p])[0][0]  # Aplica o índice de k' em k

print("Índice do capital estacionário:", p)  # Índice do capital estacionário
g_ss = k_grid[p]
print("Capital estacionário k* =", np.round(g_ss, 3))

# Consumo estacionário c* - a partir do k*
c_ss = z * k_grid[p]**alpha + (1-delta)*k_grid[p] - k_grid[p]
print("Consumo estacionário c* =", np.round(c_ss, 3))


# Calcular a função consumo c = f(k) + (1 - \delta) k - k'
cn = z * k_grid**alpha + (1-delta)*k_grid - gn[n]

# Visualização gráfica da função política de consumo
fig, ax = plt.subplots()

# Inclusão de cada função valor no gráfico
ax.plot(k_grid, cn, label='$c_{convergido}$')

# Legendas
ax.set_xlabel('Capital')
ax.set_ylabel('Função Política de Consumo')
ax.set_title('Função Política de Consumo dado Capital')
ax.legend()

plt.show()



