"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 07 - Laços de Repetição (for)

Data: 22/07/2026
Dia da Academia: 7
Tempo de estudo: ~3 horas

Objetivo:
Aprender a utilizar o laço de repetição for para executar
um bloco de código uma quantidade conhecida de vezes,
utilizando range(), acumuladores, contadores e comparações.

============================================================
"""


# ============================================================
# Exemplo 1 - Primeiro contato com o for
# ============================================================

for numero in range(5):
    print(numero)

# Explicação:
# range(5) gera:
#
# 0
# 1
# 2
# 3
# 4
#
# O último número nunca é incluído.


# ============================================================
# Exemplo 2 - Repetindo mensagens
# ============================================================

for numero in range(3):
    print("Olá")

print("Fim")

# Explicação:
# O print("Olá") pertence ao for.
# O print("Fim") está fora da repetição.


# ============================================================
# Exemplo 3 - Definindo início e fim
# ============================================================

for numero in range(2, 11):
    print(numero)

# Explicação:
# Começa em 2.
# Vai até 10.
# O 11 é o limite excluído.


# ============================================================
# Exemplo 4 - Utilizando o passo
# ============================================================

for numero in range(2, 11, 2):
    print(numero)

# Resultado:
#
# 2
# 4
# 6
# 8
# 10

# Explicação:
# O terceiro número representa o passo.
# Neste caso, pula de 2 em 2.


# ============================================================
# Exemplo 5 - Contagem regressiva
# ============================================================

for numero in range(10, 0, -1):
    print(numero)

print("Lançamento!")

# Explicação:
# Quando contamos para trás,
# o passo precisa ser negativo.


# ============================================================
# Exemplo 6 - Conferência de crachás
# ============================================================

print("===== CONFERÊNCIA DE TURNO =====")

for operador in range(1, 6):
    print()
    print("Operador", operador)
    cracha = input("Passe o crachá: ")

print()
print("===== FIM DA CONFERÊNCIA =====")

# Explicação:
# O for é ideal quando já sabemos
# exatamente quantas repetições serão feitas.


# ============================================================
# Exemplo 7 - Somando produção
# ============================================================

total = 0

for operador in range(1, 6):
    producao = int(input("Produção: "))
    total += producao

print("Produção total:", total)

# Explicação:
# total funciona como um acumulador.
# A cada repetição recebe o valor anterior
# mais a produção atual.


# ============================================================
# Exemplo 8 - Encontrando o maior valor
# ============================================================

maior = 0

for operador in range(1, 6):
    producao = int(input("Produção: "))

    if producao > maior:
        maior = producao

print("Maior produção:", maior)

# Explicação:
# Sempre que encontrar um valor maior,
# a variável maior é atualizada.


# ============================================================
# Exemplo 9 - Contando operadores
# ============================================================

meta = 0

for operador in range(1, 6):
    producao = int(input("Produção: "))

    if producao >= 500:
        meta += 1

print("Operadores que bateram a meta:", meta)

# Explicação:
# meta funciona como um contador.
# Cada operador que atende à condição
# aumenta a contagem em 1.


# ============================================================
# Conceitos importantes
# ============================================================

"""
for

→ Utilizado quando sabemos quantas vezes
o código deve repetir.

range()

→ Define o intervalo da repetição.

range(fim)

Começa em 0.

range(inicio, fim)

Define início e fim.

range(inicio, fim, passo)

Permite avançar ou voltar de acordo
com o passo informado.

Padrões importantes aprendidos:

Acumulador

total += valor

Comparador

if valor > maior:

Contador

contador += 1
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ O for executa uma quantidade conhecida de repetições.

✓ range() define o intervalo da repetição.

✓ O último valor do range nunca é incluído.

✓ O terceiro parâmetro representa o passo.

✓ Posso utilizar passo negativo em contagens regressivas.

✓ Aprendi a criar acumuladores.

✓ Aprendi a encontrar o maior valor.

✓ Aprendi a contar quantas vezes uma condição acontece.

✓ Comecei a resolver problemas pensando
na lógica antes da sintaxe.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. Quando devo utilizar for em vez de while?

# 2. O que significa dizer que o último valor
#    do range() é excluído?

# 3. Qual a diferença entre:

# total += valor

# e

# contador += 1

# 4. Por que usamos um if para descobrir
#    o maior valor?

# 5. Explique com suas palavras o que é
#    um acumulador.


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 05

Utilizamos if para tomar decisões.

Nesta aula utilizamos if dentro do for.

Aula 06

Aprendemos while para repetir enquanto
uma condição fosse verdadeira.

Nesta aula aprendemos que for é melhor
quando já sabemos exatamente quantas
vezes a repetição acontecerá.
"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que:

# Pela primeira vez comecei a pensar na solução
# antes de pensar na sintaxe.

# Descobri que existem padrões que aparecem
# várias vezes na programação:
#
# - acumular
# - comparar
# - contar

# Entendi que o VS Code pode sugerir código,
# mas a ideia precisa ser minha.
# Se eu consigo explicar o motivo de cada linha,
# então estou usando a ferramenta a meu favor
# e não dependendo dela.

# Outra percepção importante foi que,
# mesmo ficando cinco dias sem estudar,
# os conceitos continuaram na minha cabeça.
# Isso mostrou que estou entendendo a lógica,
# e não apenas decorando comandos.

# Nesta aula senti que comecei a construir
# algoritmos, e não apenas escrever programas.

# Gostei muito do for porque ele torna o código
# mais limpo e evita criar contadores manuais
# como acontecia com o while.

# Também percebi que o if e o for trabalham
# muito bem juntos: o for controla a repetição
# e o if toma decisões dentro de cada volta.
"""