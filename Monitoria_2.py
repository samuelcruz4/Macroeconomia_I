# -*- coding: utf-8 -*-
"""
''' Monitoria 1 -  Macroeconomia I, 2023'''

Baseado nos cursos: 
 -  "Introdução à Ciência da Computação com Python Parte 1"
https://www.coursera.org/learn/ciencia-computacao-python-conceitos
 - "Introdução à Ciência da Computação com Python Parte 2"
de Fabio Kon (IME-USP) no Coursera (gratuitos para visualização)
https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2

É possível obter o certificado do curso para membros da comunidade USP. 
Caso tenha interesse, acesse: https://jornal.usp.br/universidade/nova-parceria-oferece-mais-cursos-on-line-a-comunidade-usp-na-plataforma-coursera/

"""

##############################################################################


''' EXECUÇÃO CONDICIONAL '''

x = -1
if x < 0:
    print("número negativo")
# Observações:
# É obrigatório o uso do ":" na expressão do condicional, não esqueça.
# O Python só reconhece o código se estiver com a identação (tabulação) correta.
# Para o comando funcionar, deve-se selecionar todo o código e rodar com F9


# Incluindo comando "else", caso a condição seja falsa
x = 1
if x < 0:
    print("número negativo")
else:                             # Também com ":"
    print("zero ou número positivo")
# Note que o "else" é escrito sem indentação, ao mesmo nível do "if"


# Incluindo mais possíveis condições
x = 0
if x < 0:
    print("número negativo")
elif x == 0:                 # else + if
    print("zero")
else:
    print("número positivo")
    
# ou também, pode incluir mais uma condicional dentro (cuidado com indentação!)
x = 0
if x < 0:
    print("número negativo")
else:
    if x > 0:
        print("número positivo")
    else:
        print("zero")
        
        
#  QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/1cG2Z/execucao-condicional



############################################################################################################################################################################################################
''' CRIAÇÃO DE FUNÇÕES '''

# Função simples de soma de dois inputs
def some(x, y):  # Exigindo 2 argumentos
    soma = x + y
    return soma 

some(10, 15)
some(45, 13)


# Ou pode ser feito de uma forma mais direta

def mult(a, b):  
    return a * b 


mult(15, 46)
mult(5, 82)


# Função não necessariamente precisa ter algum input
def erro(a): 
 return print("Acesso Negado")

erro()


# Exemplo de cálculo de temperatura
temperaturaFarenheit = 68 
temperaturaCelsius = (temperaturaFarenheit - 32) * 5 / 9
temperaturaCelsius

'''Crie uma função com o cálculo anterior, com um parâmetro'''



def Calcular_Temperatura_Celsius(tempFarenheit): # Note que a vairável "tempFarenheit" só é utilizada nesta função
    return (tempFarenheit - 32) * 5 / 9

# tempFarenheit é uma variável "temporária" que só funcionada dentro da função.
# O seu valor vai ser inserido ao digitar o comando (ver abaixo).
# "return" é o comando para dizer qual é o ouput desta função (graus Celsius)

Calcular_Temperatura_Celsius(68)
Calcular_Temperatura_Celsius(106)


# QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/exam/mJrGn/funcoes



############################################################################################################################################################################################################
""" REPETIÇÃO / LOOP USANDO WHILE """
# Na repetição utilizando "while", precisamos, primeiramente, criar uma variável 
# indicadora de passagem, que representará as iterações do loop.Ela servirá de base 
# para criarmos as expressões condicionais. 

i = 0                     # indicador de passagem
while i <= 10:
    print(2 ** i)
    i = i + 1             # Atualiza o indicador de passagem


# No exemplo abaixo, a condição sempre será verdadeira: nunca terminará o loop
i = 0
while i > -1:
    print(2 + i)
    i += 1                # Equivalente a i = i + 1
# Para PARAR O LOOP, clique no quadrado vermelho do lado esquerdo -->


# QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/moDKn/repeticao-com-while


# Exemplo 1: achar a temperatura em Farenheit equivalente a 35ºC
# (usar a função Calcular_Temperatura_Celsius criada dentro de um loop)
temperaturaFarenheit = 0
while Calcular_Temperatura_Celsius(temperaturaFarenheit) < 35:
    temperaturaFarenheit += 1
    
print(temperaturaFarenheit, "graus Farenheit é equivalente a",
      Calcular_Temperatura_Celsius(temperaturaFarenheit), "graus Celsius")


# Exemplo 2: suponha que queramos vacianar uma população. A cada mês é possível
# vacinar 10% das pessoas ainda não vacinadas. Em quantos meses é possível
# vacinar toda população?
perc_pop_nao_vacinada = 1
meses = 1

while perc_pop_nao_vacinada > 0.1:
    perc_pop_nao_vacinada *= 0.9  # Equivalente a perc_pop_nao_vacinada = perc_pop_nao_vacinada * 0.9
    meses += 1                    # Note que o código não para de rodar, pois ele chegar a um valor próx de zero
print(meses)                      # mas não exatamente zero.   

# Então podemos estabelecer % da população que seria razoável considerar como 
# "toda população" Digamos que esse percentual seja 99%
perc_pop_nao_vacinada = 1
meses = 1
tolerancia = 0.01

while perc_pop_nao_vacinada > tolerancia:
    perc_pop_nao_vacinada = perc_pop_nao_vacinada * 0.9
    meses += 1
print("São necessários", meses, "meses para vacinar toda população")


'''Crie um loop para encontrar o valor de t onde c1>c2 dado que c1+c2 = 2 e 
c2 = 2/(1+((1 - 0.9) / (1-0.95) * (0.9/0.95)**t) --- (inicie com t = 0 e
crie um c2 = 0.001)'''

 
       
t=0   
c2 = 0.001
while c2 < 1:
    t+=1
    c2 = 2 / (1 + ((1 - 0.9) / (1-0.95) * (0.9/0.95)**t))
t-1 

c2 = 2 / (1 + ((1 - 0.9) / (1-0.95) * (0.9/0.95)**14))
c2 = 2 / (1 + ((1 - 0.9) / (1-0.95) * (0.9/0.95)**13))
c2 = 2 / (1 + ((1 - 0.9) / (1-0.95) * (0.9/0.95)**12))

""" LISTAS """
# também chamado de coleção de objetos, vetor, array

lista = [1, 2, 3, 4, 5]
lista
len(lista)  # Comprimento (length) da lista

lista[0]  # Numeração começa no zero!
lista[4]  # 5º elemento da lista


# para acrescentar um novo elemento, usa-se ".append"
lista2 = []  # Lista vazia
lista2.append("oi")
len(lista2)  # Contém 1 elemento
lista2[0]  # 1º elemento


# Dentro de uma lista, pode ter elementos de tipos distintos
filme = ["O que é isso companheiro?", "Bruno Barreto", 1.83, 1997]
type(filme) # list
type(filme[0])  # string
type(filme[1])  # string
type(filme[2])  # float
type(filme[3])  # integer


# É possível alterar os valores dos objetos
filme[3] = 2001
filme

# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/ArJZT/listas



##############################################################################
""" MANIPULAÇÃO DE LISTAS """
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
len(primos)

primos[0:2]  # Note que traz um único elemento (é subtraído 1 do último nº)
primos[1:4]  # Traz 3 elementos (é subtraído 1 do último nº)

# Dividindo pela metade
primos[0:int(len(primos)/2)]  # Aqui int() transforma número float em integer
primos
primos[int(len(primos)/2):len(primos)]

# números iniciais e finais não precisavam ser informados
primos[:int(len(primos)/2)]
primos[int(len(primos)/2):]


# Clonando listas - CUIDADO!
# Ao clonar objetos e depois alterar um objeto original, não altera valor do clonado
a = 3
b = a
a
b

a = 5
a
b


# Isto NÃO É VÁLIDO para LISTAS - objetos dentro lista continuam referenciados
lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1
lista1
lista2

lista1[0] = "rosa"
lista1
lista2  # lista2 também mudou ao alterar apenas a lista1!

lista2[1] = "roxo"
lista1  # Se altero lista2, também altero lista1!
lista2 


# Forma alternativa que cria uma cópia da lista
lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1[:]  # Indicando todos elementos da lista1
lista1
lista2

lista1[0] = "rosa"
lista1
lista2  # Manteve-se no formato original


# Pertencimento a uma lista
"rosa" in lista1
"rosa" in lista2


# Repetição de Listas
primos
primos * 2  # Não multiplica por 2 os valores, duplica o tamanho da lista

primos_2 = [i*2 for i in primos]
primos_2


lista1
lista1 * 3




# Soma de listas
carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1
carnes3

# Remoção de objetos em listas
lista1
del lista1[1]
lista1


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/Uw2C6/manipulacao-de-listas

##############################################################################
""" IMPORTAÇÃO DE MÓDULOS / PACOTES """
# Importação do pacote "math"
import math
# https://docs.python.org/3/library/math.html

# Para usar uma função, é necessário escrever o nome do módulo antes da função
math.exp(1)
exp(9)  # Erro!


# Importação do pacote "numpy": pacote que mais utilizado na disciplina
# https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355
import numpy as np # pode dar um apelido para não ter que escrever o nome inteiro

A = np.array([1, 5, 7, 4])
print(A)  # Para visualizar matrizes/vetores é melhor usar o print()
numpy.array([1, 5]) # Erro!
#

A * 2 # Agora ele multilica os valores da A por 2
A + 2 

# Importação de apenas uma função de um módulo, sem ter que escrever o módulo
from math import log as log
log(math.exp(1))



##############################################################################
""" MATRIZES (LISTA DE LISTAS) """

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]  # Note que estamos criando listas dentro de uma lista
A

# Formas de "chamar" parte da matriz
A[0][0]  # 1ª linha e 1ª coluna
A[2][2]  # 3ª linha e 3ª coluna

A[0]  # 1ª linha da matriz
A[0][:]  # 1ª linha da matriz

[A[0][1]] + [A[1][1]] + [A[2][1]]  # 2ª coluna da matriz
# pega o elemento da 2ª coluna de cada linha, transforma em lista e "soma" (listas)

# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos-2/quiz/QUA4k/matrizes


# Uma outra forma de criar matriz é por meio do módulo NumPy
# Utiliza as listas no formato "array", que é mais eficiente e facilita operações
# https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/

# Para criar uma matriz no formato array usa-se a função "array" do NumPy
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]) 
A
print(A)  # Matriz em array é melhor visualizada usando print()
type(A)

# A sintaxe do array é diferente: apenas [,] (ao invés de [][])
A[0, 0]  # 1ª linha e 1ª coluna
A[2, 2]  # 3ª linha e 3ª coluna

A[0]  # 1ª linha da matriz
A[0, :]  # 1ª linha da matriz

A[:, 1]  # 2ª coluna da matriz

# Para criar uma matriz "vazia" (com zeros), usa-se a função zeros() do NumPy
B = np.zeros([5, 8])
B
type(B)

# Para saber as dimensões de uma matrix usamos a função len()
len(B)  # Número de linhas de B
len(B[0])  # Número de elementos na 1ª linha de B (ou seja, número de colunas)


# Preenchendo primeira coluna de uma matriz:

for i in range(len(B)):
    B[i,0] = i+1
    
B

# Preenchendo terceira linha de uma matriz:

for i in range(len(B)):
    B[2,i] = 5 - i
    
B

# Exemplo de preenchimento de matrizes - Tabela da Tabuada
# Criação de uma matriz "vazia" (com zeros)
nrow = 9  # Número de Linhas
ncol = 10  # Número de Colunas
matrix = np.zeros([nrow, ncol])
print(matrix)

# Loops para preenchimento da matriz vazia usando FOR
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i, j] = (i + 1) * (j + 1)
        
print(matrix)

'''Crie uma variável beta2 = 0.95'''
'''Crie uma matriz de zeros com 18 linhas e 2 colunas'''
'''Faça um loop para preencher a primeira coluna dessa matriz com valores decrescentes
a partir do beta2 criado, onde a cada linha se reduza 0.05 da linha anterior'''



beta_2 = 0.95
tabela = np.zeros([18, 2])
for i in range(len(tabela)):
    tabela[i, 0] = beta_2 - (i + 1) * 0.05



""" REPETIÇÃO / LOOP USANDO FOR """
# Na repetição utilizando "for", criamos/atualizamos uma variável que percorre
# todos os elementos/objetos de uma lista.

# Repetição usando "for"
for i in [1, "oi", 7, 99.2]:
    print(i)

i  # Note que i se mantém no último valor após acabar o loop

# for dentro de um for
for i in [1, "oi", 7, 99.2]:
    print(i)
    for j in ["a","b"]:
        print(j)


# Criação de uma lista com sequência de números
help(range)  # Para visualizar ajuda do comando: range(start, stop[, step])
# Se preencher apenas um argumento de range(), começa no 0 e termina no nº - 1
# Se step for omitido, é igual a 1 (só pode ser um integer)

# função RANGE é importante para criar uma lista com números em sequência
for i in range(0, 10):
    print(i)
# Note que vai de 0 até 9 (ao invés de 10)


# Loop equivalente ao anterior, mas fazendo apenas 1 input
for i in range(10):
    print(i)
# Python adota como padrão o zero para iniciar as numerações


# Sequência de 2 em 2
for i in range(0, 10, 2):
    print(i)
# Note que não imprime o "último valor" (10)


# PRACTICE QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/vPfhP/repeticao-com-for

'''Escreva um codigo que encontre o perıodo t∗ para o qual cˆ1t − cˆ2t 
troca de sinal para β1s genericos.

Fixe β2 = 0.95. tem-se que c1+c2 = 2 e 
c2_t = 2 / (1 + ((1 - beta_1) / (1 - beta_2 ) ) * ( beta_1 / beta_2 )** t )
(dica: crie uma matriz, pode ser 18x2 para preencher com possiveis valores
de beta_1 na primeira coluna e os t* para cada beta_1 utilizado'''

beta_2 = 0.95  # valor de beta_2 fixado

# Criando e preenchendo matriz com beta_1 e t*
tabela = np.zeros([18, 2])  # criando matriz de zeros 18 x 2 para preenchimento

# Loop para preenchimento de possíveis \beta_1 < \beta_2 e t* para c1_t - c2_t
# mudar de sinal (quando c2_t > 1, pois c2_t = 2 - c1_t, no equilíbrio)
for i in range(len(tabela)):
    tabela[i, 0] = beta_2 - (i + 1) * 0.05
    
    # Calcular consumo inicial do indivíduo 2 (c2_0)
    t = 0
    c2_t = - np.inf # um valor pequeno arbitrário para entrar no loop
    
    while c2_t < 1:
        # Como c1_t + c2_t = 2, só precisamos verificar se c2_t > 1 ou c1_t < 1
        c2_t = 2 / (1 + ((1 - tabela[i,0]) / (1 - beta_2)) * (tabela[i,0] / beta_2) ** t)
        t += 1
    tabela[i, 1] = t - 1 # tem que ser t-1 pois o Python não atualiza
    # automaticamente o valor de c2_t

print(tabela)

##############################################################################
""" GRÁFICOS """
import matplotlib.pyplot as plt  # Módulo para fazer gráficos
import numpy as np  # Módulo para trabalhar com matrizes

# Faremos um gráfico da função y = 2^x
calculo_exponencial = np.zeros([15, 2])  # Uma coluna para x e outra para y

# Vamos preencher a matriz
for i in range(len(calculo_exponencial)):
    calculo_exponencial[i, 0] = i - 4  # Preenchendo a coluna de x (de -4 a 10)
    calculo_exponencial[i, 1] = 2 ** calculo_exponencial[i, 0]  # cálculo de y

print(calculo_exponencial)


# Criação do gráfico
fig, ax = plt.subplots()  # Cria a base (em branco) do gráfico
ax.plot(calculo_exponencial[:, 0], calculo_exponencial[:, 1],  # Coluna 0 no eixo x e coluna 1 no y
        '-o',  # Formato da linha e ponto do gráfico
        label='$y = 2^x$')  # Descrição da legenda
ax.legend()  # Faz aparecer a legenda
# ax.set_ylim([0, 1])  # tamanho mínimo e máximo vertical (corte núm. neg.)
# ax.set_xlim([-4, 0])  # tamanho mínimo e máximo horizontal (corte núm. neg.)
ax.set_xlabel('$x$')  # Descrição do eixo x
ax.set_ylabel('$y$')  # Descrição do eixo y
ax.set_title('Gráfico de $y = 2^x$')  # Título
plt.show()  # Plot do gráfico com os comandos dados


# Criação do gráfico
fig, ax = plt.subplots()  # Cria a base (em branco) do gráfico
ax.plot(tabela[:, 0], tabela[:, 1],  # Coluna 0 no eixo x e coluna 1 no y
        '-o',  # Formato da linha e ponto do gráfico
        label='$t^*(\\beta_1, \\beta_2)$')  # Descrição da legenda
ax.legend()  # Faz aparecer a legenda
ax.set_ylim([0, 15])  # tamanho mínimo e máximo vertical
ax.set_xlim([0.00, 0.95])  # tamanho mínimo e máximo horizontal
ax.set_xlabel('$\\beta_1$')  # Descrição do eixo x
ax.set_ylabel('$t^*(\\beta_1, \\beta_2)$')  # Descrição do eixo y
ax.set_title('Gráfico de $t^*(\\beta_1, \\beta_2)$ por $\\beta_1$')  # Título
plt.show()  # Plot do gráfico com os comandos dados


