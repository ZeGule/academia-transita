"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 04 - Entrada de Dados (input)

Data: 13/07/2026
Dia da Academia: 4
Tempo de estudo: ~2 horas

Objetivo:
Aprender como receber informações do usuário utilizando
input(), armazenar esses dados em variáveis e entender
como o Python trata essas entradas.

============================================================
"""


# ============================================================
# Exemplo 1 - Primeiro contato com input()
# ============================================================

nome = input("Qual é o seu nome? ")

print("Olá", nome)

# Explicação:
# input() exibe uma mensagem e aguarda uma resposta.
# O valor digitado pelo usuário é armazenado na variável.


# ============================================================
# Exemplo 2 - Entrada de múltiplos dados
# ============================================================

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")

print("Olá", nome)
print("Você tem", idade, "anos.")

# Observação:
# Mesmo digitando um número, a idade ainda é uma str.


# ============================================================
# Exemplo 3 - Verificando o tipo recebido
# ============================================================

valor = input("Digite algo: ")

print(type(valor))

# Sempre retorna:
# <class 'str'>


# ============================================================
# Exemplo 4 - Convertendo entrada para número
# ============================================================

idade = int(input("Qual é a sua idade? "))

print("No próximo ano você terá", idade + 1, "anos.")

# Explicação:
# O input recebe uma str.
# O int() converte essa str para inteiro.


# ============================================================
# Exemplo 5 - Cadastro simples
# ============================================================

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
profissao = input("Qual é a sua profissão? ")

print("==============================")
print("Cadastro realizado!")
print()
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Profissão:", profissao)
print("==============================")


# ============================================================
# Conceitos importantes
# ============================================================

"""
input()

→ Recebe informações digitadas pelo usuário.

→ Sempre retorna uma string (str).

→ Para realizar cálculos, é necessário converter
  o valor utilizando funções como int() ou float().


Exemplo:

idade = input("Idade: ")

A variável idade será:

str


idade = int(input("Idade: "))

A variável idade será:

int
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ input() permite que o usuário envie informações ao programa.

✓ Tudo recebido pelo input() é inicialmente uma str.

✓ Variáveis podem armazenar informações recebidas pelo usuário.

✓ Conversões são necessárias quando queremos realizar
  operações matemáticas.

✓ Um programa pode receber dados, processar informações
  e apresentar resultados.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. Qual o tipo padrão retornado pelo input()?

# 2. Por que precisamos usar int() antes de realizar
#    cálculos com uma idade recebida pelo usuário?

# 3. Qual a diferença entre:
#
# idade = input()
#
# e
#
# idade = int(input())


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 02 - Variáveis

Aprendi que variáveis armazenam informações.

Nesta aula, essas informações passaram a vir de uma fonte
externa: o usuário.


Aula 03 - Tipos de Dados

Aprendi que cada valor possui um tipo.

Nesta aula, utilizei esse conhecimento para entender por que
input() retorna str e quando preciso converter valores.
"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que:

Percebi que após as aulas estou entendendo melhor os codigos, está praticando a habilidade de ler e enteder o codigo é essencial, após isso ao escrever o codigo se tornou mais facil a leitura


Sugestões:

- Como foi criar um programa recebendo informações reais.

- O que mudou na forma de enxergar o código.

- O que chamou atenção sobre input().

- Alguma dúvida que ficou para estudar depois.
"""