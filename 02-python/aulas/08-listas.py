"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 08 - Listas em Python

Data: 28/07/2026
Dia da Academia: 8
Tempo de estudo: ~3 horas

Objetivo:
Aprender a trabalhar com listas em Python, entendendo como
armazenar vários valores em uma única variável, acessar
elementos por índices, percorrer listas com for, adicionar,
remover e contar elementos.

============================================================
"""


# ============================================================
# Exemplo 1 - Criando uma lista
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

print(nomes)

# Explicação:
#
# Uma lista permite armazenar vários valores dentro de uma
# única variável.
#
# Neste caso, a variável nomes possui três elementos.
#
# Diferente de criar:
#
# nome1 = "Erick"
# nome2 = "Noah"
# nome3 = "Gleyciane"
#
# A lista organiza todos os dados juntos.


# ============================================================
# Exemplo 2 - Acessando elementos por índice
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

print(nomes[0])
print(nomes[1])
print(nomes[2])

# Resultado:
#
# Erick
# Noah
# Gleyciane
#
# Explicação:
#
# O Python utiliza índices para acessar elementos.
#
# Índices começam em 0:
#
# 0 = Erick
# 1 = Noah
# 2 = Gleyciane
#
# A posição do elemento é diferente da contagem humana.


# ============================================================
# Exemplo 3 - Alterando elementos da lista
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

nomes[1] = "Maria"

print(nomes)

# Resultado:
#
# ["Erick", "Maria", "Gleyciane"]
#
# Explicação:
#
# O índice 1 que antes guardava Noah foi substituído.
#
# A quantidade de elementos continua igual.
# Apenas o conteúdo da posição foi alterado.


# ============================================================
# Exemplo 4 - Percorrendo uma lista com for
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane"]

for nome in nomes:
    print(nome)

# Explicação:
#
# O for percorre cada elemento da lista.
#
# Primeira volta:
# nome recebe "Erick"
#
# Segunda volta:
# nome recebe "Noah"
#
# Terceira volta:
# nome recebe "Gleyciane"
#
# Não é necessário acessar os índices manualmente.


# ============================================================
# Exemplo 5 - Somando valores de uma lista
# ============================================================

total = 0

producoes = [520, 480, 610, 450, 700]

for producao in producoes:
    print("Produção:", producao)
    total += producao

print("Produção total:", total)

# Explicação:
#
# O for percorre todos os valores da lista.
#
# O acumulador total guarda a soma das produções.
#
# A lógica é a mesma aprendida na Aula 07.
#
# A diferença é que agora os dados vêm de uma lista.


# ============================================================
# Exemplo 6 - Encontrando o maior valor da lista
# ============================================================

maior = 0

producoes = [520, 480, 610, 450, 700]

for producao in producoes:

    if producao > maior:
        maior = producao

print("Maior produção:", maior)

# Explicação:
#
# A cada repetição o programa compara o valor atual
# com o maior valor encontrado até aquele momento.
#
# Quando encontra um valor maior, atualiza a variável maior.


# ============================================================
# Exemplo 7 - Contando elementos que atendem uma condição
# ============================================================

meta = 500
qtd = 0

producoes = [520, 480, 610, 450, 700]

for producao in producoes:

    if producao >= meta:
        qtd += 1

print("Operadores que bateram a meta:", qtd)

# Explicação:
#
# O contador aumenta sempre que a condição for verdadeira.
#
# A mesma lógica já havia sido utilizada na Aula 07,
# mas agora aplicada a uma lista.


# ============================================================
# Exemplo 8 - Adicionando elementos com append()
# ============================================================

nomes = []

nomes.append("Erick")
nomes.append("Noah")

print(nomes)

# Resultado:
#
# ["Erick", "Noah"]
#
# Explicação:
#
# append() adiciona um novo elemento ao final da lista.
#
# Uma lista pode começar vazia e ser construída durante
# a execução do programa.


# ============================================================
# Exemplo 9 - Criando uma lista dinamicamente
# ============================================================

nomes = []

for qtd in range(5):
    nomes.append(input("Digite um nome: "))

print(nomes)

# Explicação:
#
# O programa começa com uma lista vazia.
#
# A cada repetição:
#
# 1 - recebe um nome do usuário.
# 2 - adiciona esse nome na lista.
#
# O resultado é uma lista criada durante a execução.


# ============================================================
# Exemplo 10 - Removendo elementos com remove()
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane", "João"]

nomes.remove("João")

print(nomes)

# Resultado:
#
# ["Erick", "Noah", "Gleyciane"]
#
# Explicação:
#
# remove() exclui um elemento específico da lista.
#
# Ao remover um elemento, os índices dos próximos elementos
# podem mudar.


# ============================================================
# Exemplo 11 - Descobrindo o tamanho da lista com len()
# ============================================================

nomes = ["Erick", "Noah", "Gleyciane", "João"]

print(len(nomes))

# Resultado:
#
# 4
#
# Explicação:
#
# len() retorna a quantidade de elementos existentes.
#
# Neste caso, a lista possui quatro nomes.


# ============================================================
# Exemplo 12 - Cadastro de operadores
# ============================================================

operadores = []

for qtd in range(5):
    print("Cadastro de operadores")
    operadores.append(input("Digite o nome a ser cadastrado: "))

print()
print("Total de operadores:", len(operadores))

print()
print("Operadores:")

for operador in operadores:
    print(operador)

# Explicação:
#
# Este exercício reuniu vários conceitos:
#
# - lista vazia
# - for
# - range()
# - input()
# - append()
# - len()
# - percorrer lista
#
# Foi o primeiro programa da Academia onde uma lista foi
# criada completamente durante a execução.


# ============================================================
# Conceitos importantes
# ============================================================

"""
Lista

→ Estrutura que permite guardar vários valores dentro de uma
única variável.

Índice

→ Posição de um elemento dentro da lista.

O Python começa os índices em 0.

for

→ Permite percorrer todos os elementos de uma lista.

append()

→ Adiciona um elemento ao final da lista.

remove()

→ Remove um elemento específico da lista.

len()

→ Retorna a quantidade de elementos da lista.

Padrões reutilizados:

Acumulador:

total += valor


Comparação:

if valor > maior:


Contador:

contador += 1
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ Uma lista permite armazenar vários dados em uma única variável.

✓ Os elementos da lista possuem índices começando em 0.

✓ Posso percorrer uma lista utilizando for.

✓ O for pode receber diretamente cada elemento da lista.

✓ Posso adicionar elementos usando append().

✓ Posso remover elementos usando remove().

✓ Posso descobrir a quantidade de elementos usando len().

✓ Os algoritmos aprendidos no for continuam funcionando,
  mudando apenas a origem dos dados.

✓ Uma lista pode ser criada vazia e preenchida durante a
  execução do programa.

✓ Comecei a trabalhar com dados de forma mais parecida com
  sistemas reais.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. O que é uma lista em Python?

# 2. Por que os índices começam em 0?

# 3. Qual a diferença entre:
#
# nomes[1] = "Maria"
#
# e
#
# nomes.remove("Maria")


# 4. O que acontece quando utilizamos:
#
# nomes.append("Erick")


# 5. Qual a função do len()?


# 6. Qual a diferença entre:
#
# for numero in range(5)
#
# e
#
# for nome in nomes


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 04 e 05

Aprendemos estruturas condicionais.

Nesta aula utilizamos if dentro das listas para:
- encontrar maiores valores;
- contar elementos;
- criar regras.


Aula 06

Aprendemos while para repetições condicionais.

Agora utilizamos for para percorrer dados existentes.


Aula 07

Aprendemos for, acumuladores e contadores.

A Aula 08 mostrou que esses conceitos continuam sendo usados
quando os dados estão armazenados em listas.


Aula 08 representa a união:

Lista + For + If + Variáveis auxiliares

"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que:

# Listas começaram a fazer sentido quando entendi que elas
# permitem guardar vários dados dentro de uma única variável.

# No começo eu pensava em acessar elementos manualmente,
# usando índices como:
#
# nomes[0]
# nomes[1]
# nomes[2]
#
# mas percebi que o for permite trabalhar com todos os dados
# de forma muito mais eficiente.


# Um momento importante foi perceber que os algoritmos não
# mudam tanto.

# Na Aula 07 eu recebia valores pelo input().
#
# Na Aula 08 os valores já estavam em uma lista.
#
# A lógica de somar, comparar e contar continuou igual.


# Durante o exercício do append(), tive uma primeira tentativa
# errada:

# input("Digite um nome: ")
# nomes.append(nome)

# O programa pedia o nome, mas eu não estava guardando o valor
# digitado.

# Depois percebi que precisava utilizar o retorno do input:

# nomes.append(input("Digite um nome: "))

# Isso mostrou que uma função pode entregar um valor para outra.


# Também tive um erro usando:

# for operador in operadores()

# Percebi que estava tratando uma lista como se fosse uma
# função.

# A correção veio entendendo a diferença entre armazenar dados
# e executar comandos.


# Outro aprendizado importante foi perceber que o VS Code pode
# sugerir código, mas a lógica precisa ser minha.

# Quando eu sei o que quero construir e entendo cada linha,
# a ferramenta se torna um auxílio e não uma dependência.


# Nesta aula senti que comecei a trabalhar com estruturas mais
# próximas de sistemas reais.

# Uma lista de operadores, produção ou usuários é algo que
# aparece constantemente em programas de verdade.


# A maior evolução foi perceber que estou começando a pensar
# na solução antes de pensar na sintaxe.
"""