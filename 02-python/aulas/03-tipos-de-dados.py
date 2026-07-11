"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 03 - Tipos de Dados

Objetivo:
Compreender por que diferentes tipos de dados existem
e como o Python os interpreta.

Pré-requisitos:
- Aula 01 - Olá Mundo
- Aula 02 - Variáveis

============================================================
"""

print("10" + "5")
print(10 + 5)
print("10" + str(5))

print(type("Erick"))
print(type(29))
print(type(1.74))
print(type(True))


# ============================================================
# Exemplo 1 - String (str)
# ============================================================

nome = "Erick"

print(nome)

# str representa textos.
# Textos são escritos entre aspas.


# ============================================================
# Exemplo 2 - Inteiro (int)
# ============================================================

idade = 29

print(idade)

# int representa números inteiros.


# ============================================================
# Exemplo 3 - Número decimal (float)
# ============================================================

altura = 1.74

print(altura)

# float representa números com casas decimais.


# ============================================================
# Exemplo 4 - Booleano (bool)
# ============================================================

trabalha = True

print(trabalha)

# bool representa valores lógicos:
# True (verdadeiro) ou False (falso).


# ============================================================
# Exemplo 5 - Verificando tipos
# ============================================================

print(type(nome))
print(type(idade))
print(type(altura))
print(type(trabalha))

# type() retorna o tipo do valor armazenado.


# ============================================================
# Resumo da Aula
# ============================================================

# str   -> texto
# int   -> número inteiro
# float -> número decimal
# bool  -> verdadeiro ou falso

# O tipo do dado influencia o comportamento das operações.

# Exemplo:
# "10" + "5" gera "105", pois são textos.
# 10 + 5 gera 15, pois são números.

# Uma variável pode receber valores de tipos diferentes
# ao longo da execução do programa.


# ============================================================
# Perguntas para Revisão
# ============================================================

# 1. Qual a diferença entre "10" e 10?
# 2. Por que "10" + "5" não gera 15?
# 3. O que a função type() retorna?
# 4. Uma variável pode mudar de tipo durante a execução?