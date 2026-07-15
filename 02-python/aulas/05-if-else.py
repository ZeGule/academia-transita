"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 05 - Estruturas de Decisão (if, elif e else)

Data: 15/07/2026
Dia da Academia: 5
Tempo de estudo: ~2 horas

Objetivo:
Aprender como criar programas capazes de tomar decisões
utilizando condições lógicas, comparações e estruturas
de decisão como if, elif e else.

Nesta aula o programa deixou de apenas executar comandos
em sequência e passou a escolher caminhos diferentes
dependendo dos dados recebidos.

============================================================
"""


# ============================================================
# Exemplo 1 - Primeira decisão utilizando if
# ============================================================

idade = 20

if idade >= 18:
    print("Maior de idade.")

print("Sistema encerrado.")


# Explicação:
# O if verifica uma condição.
#
# Caso a condição seja verdadeira (True), o bloco dentro
# dele será executado.
#
# Caso seja falsa (False), o programa continua normalmente.


# ============================================================
# Exemplo 2 - Utilizando else
# ============================================================

idade = 15

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")


# Explicação:
# O else representa o caminho contrário do if.
#
# Quando o if for False, o else será executado.


# ============================================================
# Exemplo 3 - Comparações retornam True ou False
# ============================================================

print(10 > 5)

print(10 < 5)

print(10 == 10)

print(10 == 8)


# Resultado:
#
# True
# False
# True
# False
#
#
# Explicação:
# Operadores de comparação sempre retornam valores booleanos.
#
# True  = verdadeiro
# False = falso


# ============================================================
# Exemplo 4 - Diferença entre = e ==
# ============================================================

idade = 29


if idade == 29:
    print("A idade é 29.")


# Explicação:
#
# =  serve para atribuição.
#
# Exemplo:
#
# idade = 29
#
# Estamos guardando o valor 29 dentro da variável.
#
#
# == serve para comparação.
#
# Exemplo:
#
# idade == 29
#
# Estamos perguntando se o valor da variável é igual a 29.


# ============================================================
# Exemplo 5 - Múltiplas decisões com elif
# ============================================================

idade = 65

if idade < 12:
    print("Não pode entrar.")
elif idade >= 60:
    print("Entrada preferencial.")
else:
    print("Entrada comum.")


# Explicação:
# elif significa "else if" (senão, se).
#
# Ele permite criar mais caminhos de decisão.
#
# O Python executa apenas o primeiro bloco verdadeiro.


# ============================================================
# Exemplo 6 - Sistema de classificação de corrida
# ============================================================

nome = input("Nome do corredor: ")
tempo = float(input("Tempo da corrida em minutos: "))

if tempo > 40:
    print(nome, "classificado como iniciante.")
elif tempo < 20:
    print(nome, "classificado como elite.")
else:
    print(nome, "classificado como intermediário.")


# Explicação:
# O programa recebe informações do usuário e transforma
# regras reais em decisões.
#
# O uso de float permite receber valores decimais.


# ============================================================
# Conceitos importantes
# ============================================================

"""
if

→ Cria uma condição que será verificada pelo programa.


else

→ Executa quando a condição do if for falsa.


elif

→ Significa "else if".

→ Permite criar condições intermediárias.


Operadores de comparação:

==  Igual

!=  Diferente

>   Maior que

<   Menor que

>=  Maior ou igual

<=  Menor ou igual


Todas as comparações retornam:

True

ou

False


O if utiliza esse resultado para decidir qual caminho seguir.


Indentação:

Em Python, os espaços definem quais linhas pertencem
a cada bloco.

A indentação não é apenas estética.

Ela faz parte da estrutura do código.
"""


# ============================================================
# Erros estudados
# ============================================================

"""
IndentationError

Acontece quando a indentação está incorreta.

Exemplo:

if idade >= 18:
    print("Maior")
        print("Erro")


O Python entende:

"Esse print pertence a quem?"


TypeError

Acontece quando tentamos realizar uma operação
incompatível entre tipos de dados.

Exemplo:

"29" + 1


Uma str não pode ser somada diretamente com um int.
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ Programas podem tomar decisões.

✓ if executa um bloco quando uma condição é verdadeira.

✓ else executa quando a condição é falsa.

✓ elif permite criar múltiplos caminhos.

✓ Comparações retornam True ou False.

✓ O operador = atribui valores.

✓ O operador == compara valores.

✓ A indentação define a organização dos blocos.

✓ É possível transformar regras do mundo real em
  algoritmos usando decisões.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. Qual a diferença entre:
#
# =
#
# e
#
# ==


# 2. O que uma comparação retorna?


# 3. Qual a diferença entre utilizar:
#
# if
# if
#
# e
#
# if
# elif
# else


# 4. Por que a indentação é importante no Python?


# 5. Por que o bool estudado na Aula 03 passou a fazer
# sentido quando aprendemos estruturas de decisão?


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 02 - Variáveis

Aprendi que variáveis armazenam informações.

Nesta aula, essas informações passaram a influenciar
o comportamento do programa.


Aula 03 - Tipos de Dados

Aprendi sobre bool.

Nesta aula, entendi que comparações geram valores
True ou False.


Aula 04 - Input

Aprendi a receber dados do usuário.

Nesta aula, utilizei esses dados para criar decisões.
"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que programação é transformar regras reais
em perguntas que o computador consegue responder.

Exemplos:

Uber:

O motorista aceitou a corrida?

True ou False.


Banco:

A senha está correta?

True ou False.


Gerdau:

O crachá está autorizado?

True ou False.


Um programa precisa dessas respostas para decidir
qual caminho seguir.


------------------------------------------------------------

Insight sobre comparação:

A comparação não executa uma ação.

Ela apenas responde uma pergunta.

O if utiliza essa resposta para decidir o fluxo.


------------------------------------------------------------

Insight sobre indentação:

A indentação não serve apenas para deixar o código bonito.

Ela define a quem cada linha pertence.

Uma forma de pensar:

"Esse print responde para quem?"


------------------------------------------------------------

Insight sobre elif:

Quando usei dois if separados, percebi que o programa
poderia executar duas respostas diferentes.

O elif existe para criar caminhos exclusivos.

Apenas uma condição será escolhida.


------------------------------------------------------------

Insight sobre representação de dados:

Ao criar o sistema de classificação de corrida, percebi
que representar uma informação corretamente também faz
parte da programação.

Um valor como:

38.59

não representa 38 minutos e 59 segundos.

Ele representa:

38 minutos + 0.59 minuto.

Aproximadamente:

38 minutos e 35 segundos.


------------------------------------------------------------

Evolução do programador:

Comecei a perceber que primeiro devo entender o problema
e criar a lógica em português antes de pensar na sintaxe.

A escrita do código fica mais natural quando a lógica
está clara.
"""