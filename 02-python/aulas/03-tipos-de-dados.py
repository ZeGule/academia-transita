"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 03 - Tipos de Dados

Data: 13/07/2026
Dia da Academia: 4
Tempo de estudo: ~2 horas

Objetivo:
Compreender os principais tipos de dados do Python,
aprender a identificá-los, convertê-los e entender
como eles influenciam o comportamento do programa.

============================================================
"""

# ============================================================
# Exemplo 1 - String (str)
# ============================================================

nome = "Erick"

print(nome)
print(type(nome))

# Saída esperada:
#
# Erick
# <class 'str'>
#
# Explicação:
# str representa textos.
# Textos são escritos entre aspas.


# ============================================================
# Exemplo 2 - Inteiro (int)
# ============================================================

idade = 29

print(idade)
print(type(idade))

# Saída esperada:
#
# 29
# <class 'int'>
#
# Explicação:
# int representa números inteiros.


# ============================================================
# Exemplo 3 - Float
# ============================================================

altura = 1.74

print(altura)
print(type(altura))

# Saída esperada:
#
# 1.74
# <class 'float'>
#
# Explicação:
# float representa números com casas decimais.


# ============================================================
# Exemplo 4 - Booleano
# ============================================================

trabalha = True

print(trabalha)
print(type(trabalha))

# Saída esperada:
#
# True
# <class 'bool'>
#
# Explicação:
# bool representa valores lógicos:
# True (verdadeiro)
# False (falso)


# ============================================================
# Exemplo 5 - O operador +
# ============================================================

print("10" + "5")
print(10 + 5)

# Saída esperada:
#
# 105
# 15
#
# Explicação:
# Entre strings, o operador + concatena (junta textos).
# Entre inteiros, o operador + realiza uma soma.


# ============================================================
# Exemplo 6 - Mistura de tipos
# ============================================================

# print("10" + 5)

# Resultado esperado:
#
# TypeError
#
# Explicação:
# O Python não converte automaticamente texto em número.
# É necessário realizar a conversão manualmente.


# ============================================================
# Exemplo 7 - Conversão de tipos
# ============================================================

idade = "29"

print(type(idade))

idade = int(idade)

print(type(idade))

# Saída esperada:
#
# <class 'str'>
# <class 'int'>
#
# Explicação:
# int() tenta converter um valor para inteiro.


# ============================================================
# Exemplo 8 - Conversão inválida
# ============================================================

# idade = "vinte e nove"
# idade = int(idade)

# Resultado esperado:
#
# ValueError
#
# Explicação:
# Apenas strings que representam números podem ser
# convertidas para int.


# ============================================================
# Conceitos importantes
# ============================================================

"""
Tipos básicos do Python

str
→ Representa textos.

int
→ Representa números inteiros.

float
→ Representa números decimais.

bool
→ Representa valores lógicos (True ou False).


Funções aprendidas

print()
→ Exibe informações na tela.

type()
→ Retorna o tipo do valor armazenado.

int()
→ Tenta converter um valor para inteiro.


Observações

• O tipo do dado influencia o comportamento das operações.

• "10" + "5" gera "105".

• 10 + 5 gera 15.

• O Python não tenta adivinhar sua intenção.

• Quando a conversão não é possível,
  o Python gera um erro.
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ Existem diferentes tipos de dados.

✓ O mesmo valor visual pode possuir tipos diferentes.

✓ O operador + muda de comportamento conforme o tipo.

✓ Posso identificar o tipo de um valor utilizando type().

✓ Posso converter strings numéricas utilizando int().

✓ Nem toda string pode ser convertida para inteiro.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. Qual a diferença entre 10 e "10"?

# 2. Por que "10" + "5" não resulta em 15?

# 3. O que a função type() retorna?

# 4. O que faz a função int()?

# 5. Por que int("123") funciona?

# 6. Por que int("vinte e três") gera erro?

# 7. O que significa dizer que o tipo do dado influencia
#    o comportamento do programa?


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 02 - Variáveis

Nesta aula descobri que uma variável não possui
um tipo fixo.

Ela pode armazenar diferentes tipos de dados
durante a execução do programa.

O tipo depende do valor armazenado naquele momento.
"""


# ============================================================
# Caderno de engenharia
# ============================================================

"""
Reflexões:

me recordei de alguns pontos sobre input, realmente não lembrava que ele retorna uma string, e que para receber um número é necessário fazer a conversão com int().
não lembrava como era usado o int() para converter uma string em número, e que se a string não for um número válido, o Python gera um ValueError porém era muito ilogico que funcionasse para strings que não são números, mas que possuem números dentro, como "123abc", e que o Python não consegue converter isso para inteiro.
foi uma aula bem produtiva, de recordação e tambem de aprendizado. coisas que decorei, mas que não sabia o porque.

"""