# -*- coding: utf-8 -*-
"""
''' Monitoria 1 -  Macroeconomia I, 2023'''

Baseado no curso: "Introdução à Ciência da Computação com Python Parte 1"
https://www.coursera.org/learn/ciencia-computacao-python-conceitos

É possível obter o certificado do curso para membros da comunidade USP. 
Caso tenha interesse, acesse: https://jornal.usp.br/universidade/nova-parceria-oferece-mais-cursos-on-line-a-comunidade-usp-na-plataforma-coursera/

"""


############################################################################################################################################################################################################
''' Operações Básicas'''

1 + 1       # Soma
2 - 3       # Subtração

2 * 3       # Multiplicação
2 / 2       # Divisão

6 // 2      # Parte inteira da divisão
6 % 4       # Resto da divisão

6 ** 2      # Potenciação
4 ** (1/2)  # Radiciação

 
# QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/N1e0Z/tipos-de-dados


############################################################################################################################################################################################################
''' Atalhos no Spyder'''

# Selecionar a linha e apertar F9, roda a linha selecionada
(8 + 4 ** 3) / 9

4 + 2
# O mesmo racicínio se aplica ao selecionar mais de uma linha   
(8 + 4 ** 3) / 9
8 + 4

# O # é utilizado para comentar o código
# Também pode ser utilizado o '''''' ou """""", onde o comentário fica realçado

# Selecionar varia linha e utilizar o atalho Ctrl + 1 comenta todas as linhas

# 7 * 4
# 15 + 7
# 5**2 + 12

############################################################################################################################################################################################################
''' Atribuições da Variáveis e Objetos'''

x = 10    # o "=" cria uma variável
x
type(x)   # Comando que tem como output o tipo da variável, nete caso é um integer

y = 5/2
y
type(y)   # y é um float (semelhante aos números Reais) 


# Alterando Valores
x = 100
x

x = x + 5    # Acrescenta 5 ao valor de x
x

# Ou de forma equivalente
x = 100
x

x =+ 5    # Esta operção pode ser feita com qualquer operado " -, *, /, **, etc"
x

# Soma de variáveis, desde que as variáveis sejam de tipos consistentes
y = 3.5
soma = x + y  
soma
type(soma) # float


# NESTE CASO, ao alterarmos o valor de "x" após criar "soma", não altera "soma"
x
x *= 2
x
soma


# Variáveis com textos
palavra = "Olá"  # Também pode ser com aspas simples: 'Olá'
palavra
type(palavra)  # Objeto é um string (texto)
len(palavra)  # Função que traz o tamanho do string

# Concatenação de texto com números
print("A soma é", round(soma, 1))  # Já inclui espaçamento entre os argumentos
# round() foi usado para arredondar "soma" com 1 casa decimal



############################################################################################################################################################################################################
''' EXPRESSÕES BOOLEANAS '''
# Valor lógico Verdadeiro ou Falso

13 < 9
1 <= 4
10 > 5
2 >= 2

9**2 == 80 + 1      # As expressões são exatamente iguais
100 != 10*5         # "!=" representa o diferente
not 100 == 10*5     # o "not" nega o valor que o segue

type(100 == 10**2)  # tipo bool


10 = 10 # Erro! O símbolo de "=" é uma forma de ATRIBUIÇÃO de valor a uma variável

# Objeto boolean pode ser aplicado a uma variável também
idade = 15
maioridade = 18
pode_dirigir = idade >= maioridade
pode_dirigir
type(pode_dirigir)


# Expressões Compostas
x = 200
x < 0 or x**2 > 100
x < 0 and x**2 > 100
not (x < 0 and x**2 > 100)  # "not" nega tudo em parênteses


''' Tabela de Precedência de Operadores '''

# Nível 7 (maior preferência) - exponenciação: **
# Nível 6 - multiplicação: *, /, //, %
# Nível 5 - adição: +, -
# Nível 4 - relacional: ==, !=, <=, >=, >, <
# Nível 3 - lógico: not
# Nível 2 - lógico: and
# Nível 1 - lógico: or


# QUIZ: https://www.coursera.org/learn/ciencia-computacao-python-conceitos/quiz/40vwN/expressoes-booleanas



############################################################################################################################################################################################################
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
def some(a, b):  # Exigindo 2 argumentos
    soma = a + b
    return soma 

some(10, 15)
some(45, 13)


# Ou pode ser feito de uma forma mais direta

def some(a, b):  
    return a + b 


some(15, 46)
some(5, 82)


# Função não necessariamente precisa ter algum input
def erro(): 
 return print("Acesso Negado")

erro()


# Exemplo de cálculo de temperatura
temperaturaFarenheit = 68 
temperaturaCelsius = (temperaturaFarenheit - 32) * 5 / 9
temperaturaCelsius

# Criação de uma função com o cálculo anterior, com um parâmetro
def Calcular_Temperatura_Celsius(tempFarenheit): # Note que a vairável "tempFarenheit" só é utilizada nesta função
    return (tempFarenheit - 32) * 5 / 9

# tempFarenheit é uma variável "temporária" que só funcionada dentro da função.
# O seu valor vai ser inserido ao digitar o comando (ver abaixo).
# "return" é o comando para dizer qual é o ouput desta função (graus Celsius)

Calcular_Temperatura_Celsius(68)
Calcular_Temperatura_Celsius(86)


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

while perc_pop_nao_vacinada > 0:
    perc_pop_nao_vacinada *= 0.9  # Equivalente a perc_pop_nao_vacinada = perc_pop_nao_vacinada * 0.9
    meses += 1                    # Note que o código não para de rodar, pois ele chegar a um valor próx de zero
print(meses)                      # mas não exatamente zero.   

# Então podemos estabelecer % da população que seria razoável considerar como 
# "toda população" Digamos que esse percentual seja 99,9%
perc_pop_nao_vacinada = 1
meses = 1
tolerancia = 0.01

while perc_pop_nao_vacinada > tolerancia:
    perc_pop_nao_vacinada = perc_pop_nao_vacinada * 0.9
    meses += 1
print("São necessários", meses, "meses para vacinar toda população")



     