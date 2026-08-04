"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 10 - Metodos de Listas

Data: 04/08/2026
Dia da Academia: 10
Tempo de estudo: ~3 horas

Objetivo:
Aprender os principais métodos das listas do Python para
adicionar, inserir, remover, organizar e manipular dados.

============================================================
"""


# ============================================================
# Exemplo 1 - append()
# ============================================================

nomes = ["Erick", "Noah"]

nomes.append("Gleyciane")

print(nomes)

# Saída:
#
# ['Erick', 'Noah', 'Gleyciane']

# Explicação:
# append() adiciona um novo elemento
# sempre no final da lista.


"""
💡 Ideia do Engenheiro

Nem sempre sabemos todos os dados quando o programa
é iniciado.

Na maioria dos sistemas reais, a lista começa vazia
e vai sendo preenchida durante a execução.
"""


# ============================================================
# Exemplo 2 - insert()
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

nomes.insert(1, "João")

print(nomes)

# Saída:
#
# ['Erick', 'João', 'Noah', 'Gleyciane']

# Explicação:
# insert() permite escolher exatamente
# em qual posição o novo elemento será inserido.
#
# O primeiro parâmetro é o índice.
# O segundo é o valor.


"""
💡 Ideia do Engenheiro

Os índices não servem apenas para acessar elementos.

Também podem ser utilizados para inserir informações
em posições específicas da lista.
"""


# ============================================================
# Exemplo 3 - remove()
# ============================================================

nomes = ["Erick", "João", "Noah", "Gleyciane"]

nomes.remove("João")

print(nomes)

# Saída:
#
# ['Erick', 'Noah', 'Gleyciane']

# Explicação:
# remove() procura o elemento informado
# e o remove da lista.


# ============================================================
# Exemplo 4 - pop()
# ============================================================

nomes = ["Erick", "João", "Noah", "Gleyciane"]

ultimo = nomes.pop()

print("Elemento removido:", ultimo)
print("Lista:", nomes)

# Saída:
#
# Elemento removido: Gleyciane
# Lista: ['Erick', 'João', 'Noah']

# Explicação:
# pop() remove o último elemento da lista
# e também retorna esse elemento.
#
# Esse retorno pode ser armazenado
# em uma variável.


"""
💡 Ideia do Engenheiro

Foi nesta aula que ficou claro que alguns métodos
do próprio Python também utilizam o conceito
de return aprendido na Aula 09.

O pop() não apenas remove um elemento.
Ele devolve esse elemento para quem chamou
o método.
"""


# ============================================================
# Exemplo 5 - pop(indice)
# ============================================================

nomes = ["Erick", "João", "Noah", "Gleyciane"]

removido = nomes.pop(1)

print("Removido:", removido)
print("Lista:", nomes)

# Saída:
#
# Removido: João
# Lista: ['Erick', 'Noah', 'Gleyciane']

# Explicação:
# Quando informamos um índice,
# pop() remove exatamente aquele elemento.
#
# Assim como append(), pop() também
# retorna um valor.
# ============================================================
# Exemplo 6 - sort()
# ============================================================

numeros = [8, 3, 15, 1, 10]

numeros.sort()

print(numeros)

# Saída:
#
# [1, 3, 8, 10, 15]

# Explicação:
# sort() organiza os elementos da própria lista
# em ordem crescente.


"""
💡 Ideia do Engenheiro

sort() não cria uma nova lista.

Ele reorganiza a lista existente.

Depois da execução, a variável continua sendo
a mesma, porém agora organizada.
"""


# ============================================================
# Exemplo 7 - reverse()
# ============================================================

numeros = [8, 3, 15, 1, 10]

numeros.reverse()

print(numeros)

# Saída:
#
# [10, 1, 15, 3, 8]

# Explicação:
# reverse() apenas inverte a ordem atual
# dos elementos.
#
# Ele NÃO organiza a lista.


"""
💡 Ideia do Engenheiro

No início é comum imaginar que reverse()
desfaz um sort().

Na verdade ele não conhece o histórico
da lista.

Ele apenas inverte a ordem atual dos
elementos.
"""


# ============================================================
# Exemplo 8 - clear()
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

nomes.clear()

print(nomes)

# Saída:
#
# []

# Explicação:
# clear() remove todos os elementos
# da lista.
#
# A lista continua existindo,
# apenas fica vazia.


# ============================================================
# Exemplo 9 - len()
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

print(len(nomes))

# Saída:
#
# 3

# Explicação:
# len() retorna a quantidade de elementos
# existentes na lista.


"""
💡 Ideia do Engenheiro

Uma lista vazia continua sendo uma lista.

Por isso:

nomes = []

é diferente de:

print(nomes)

A lista existe.
Ela apenas possui zero elementos.
"""


# ============================================================
# Conceitos importantes
# ============================================================

"""
append(valor)

→ Adiciona um elemento ao final da lista.


insert(indice, valor)

→ Insere um elemento em uma posição específica.


remove(valor)

→ Remove um elemento pelo valor.


pop()

→ Remove e retorna o último elemento.


pop(indice)

→ Remove e retorna o elemento
do índice informado.


sort()

→ Organiza os elementos
em ordem crescente.


reverse()

→ Inverte a ordem atual
dos elementos.


clear()

→ Remove todos os elementos
da lista.


len(lista)

→ Retorna a quantidade
de elementos.
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ append() adiciona elementos ao final.

✓ insert() permite inserir elementos
em posições específicas.

✓ remove() remove um elemento pelo valor.

✓ pop() remove e também retorna
o elemento removido.

✓ sort() organiza a lista.

✓ reverse() apenas inverte
a ordem atual da lista.

✓ clear() esvazia uma lista.

✓ len() retorna a quantidade
de elementos.

✓ Alguns métodos modificam a lista.

✓ Outros modificam a lista
e também retornam um valor.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. Qual a diferença entre append()
#    e insert()?

# 2. Qual a diferença entre remove()
#    e pop()?

# 3. O que acontece quando utilizamos
#    pop() sem guardar o retorno?

# 4. Qual a diferença entre sort()
#    e reverse()?

# 5. Para que serve clear()?

# 6. O que a função len() retorna?


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 08

Aprendemos a criar listas,
percorrer listas com for,
utilizar append(), remove()
e len().

Nesta aula ampliamos esse conhecimento,
aprendendo novos métodos para manipular
listas de maneira mais eficiente.


Aula 09

Aprendemos a criar funções
e utilizar return.

Nesta aula percebemos que alguns métodos
do próprio Python também retornam valores,
como acontece com pop().
"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que:

# As listas não servem apenas para armazenar
# informações. Elas possuem métodos próprios
# para manipular seus dados.

# O conceito de índice ficou mais sólido.
# Agora consigo enxergar que ele pode ser
# utilizado para acessar, alterar, inserir
# e remover elementos.

# O método pop() foi o maior aprendizado
# desta aula. Antes eu acreditava que ele
# apenas removia elementos. Agora entendo
# que ele também retorna o elemento removido,
# conectando diretamente com o conceito
# de return estudado na Aula 09.

# Durante o Mini Desafio Transita consegui
# desenvolver um pequeno sistema para cadastro
# de operadores utilizando listas, for,
# append(), remove(), sort() e len().

# Também percebi que algumas sintaxes,
# como "for item in lista", ainda exigem
# alguns segundos para vir à memória.
# Isso mostra que já conheço o conceito;
# agora preciso apenas ganhar repetição.

# Aprendi que boas decisões dependem
# do contexto. Em alguns casos faz sentido
# repetir uma mensagem dentro de um laço;
# em outros, basta exibi-la uma única vez.

# Nesta aula comecei a enxergar listas
# como estruturas que mudam durante
# a execução do programa, aproximando
# meus exercícios de situações reais
# encontradas em sistemas.
"""