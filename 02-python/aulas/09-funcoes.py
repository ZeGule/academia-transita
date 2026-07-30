"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 09 - Funções

Data: 28/07/2026
Dia da Academia: 9
Tempo de estudo: ~3 horas

Objetivo:

Aprender a criar funções para organizar programas,
evitar repetição de código e reutilizar soluções
em diferentes partes do sistema.

Nesta aula conheceremos:

• def
• parâmetros
• argumentos
• return
• reutilização de funções

============================================================
"""


# ============================================================
# Exemplo 1 - Primeira função
# ============================================================

def mensagem():
    print("Bem-vindo ao sistema!")


mensagem()

# Explicação:
#
# def cria uma função.
#
# A função fica "guardada" até ser chamada.
#
# Apenas criar a função não executa o código.
#
# A execução acontece quando fazemos:
#
# mensagem()


# ============================================================
# Exemplo 2 - Função com parâmetro
# ============================================================

def mostrar_nome(nome):
    print("Olá", nome)


mostrar_nome("Erick")

# Explicação:
#
# nome é um parâmetro.
#
# Um parâmetro funciona como uma variável criada
# apenas para existir dentro da função.
#
# Quando chamamos:
#
# mostrar_nome("Erick")
#
# o parâmetro nome recebe o valor "Erick".


# ============================================================
# Exemplo 3 - Mais argumentos
# ============================================================

mostrar_nome("Noah")
mostrar_nome("Gleyciane")

# Explicação:
#
# A mesma função pode ser utilizada diversas vezes.
#
# Apenas mudamos o argumento enviado.
#
# Isso evita repetir código.


# ============================================================
# Exemplo 4 - Dois parâmetros
# ============================================================

def somar(a, b):
    resultado = a + b
    print(resultado)


somar(10, 5)

# Resultado:
#
# 15

# Explicação:
#
# A função recebe dois parâmetros.
#
# Dentro dela podemos utilizar esses valores
# normalmente para realizar cálculos.


# ============================================================
# Exemplo 5 - Utilizando return
# ============================================================

def somar(a, b):
    return a + b


resultado = somar(10, 5)

print(resultado)

# Explicação:
#
# Diferente do print(),
# o return devolve um valor para quem chamou
# a função.
#
# Esse valor pode ser armazenado em uma variável,
# utilizado em outro cálculo ou exibido depois.


# ============================================================
# Exemplo 6 - Calculando bônus
# ============================================================

def calcular_bonus(producao):
    return producao * 0.10


producao = int(input("Produção: "))

bonus = calcular_bonus(producao)

print()
print("Produção:", producao)
print("Bônus:", bonus)

# Explicação:
#
# A função resolve apenas um problema:
#
# calcular o bônus.
#
# Ela não pede dados ao usuário
# nem imprime resultados.
#
# Essa responsabilidade fica para o programa
# principal.


# ============================================================
# Primeiras ideias importantes
# ============================================================

"""
Até aqui aprendemos que:

Uma função é uma pequena ferramenta.

Ela recebe informações.

Processa essas informações.

E pode devolver um resultado.

Quanto menor a responsabilidade de uma função,
mais fácil ela costuma ser de entender,
testar e reutilizar.

Começamos também a separar o programa em duas partes:

• Programa principal

Responsável por conversar com o usuário.

• Funções

Responsáveis por resolver pequenos problemas.

Essa separação deixa o código muito mais organizado.
"""

# ============================================================
# Exemplo 7 - Calculando média
# ============================================================

def calcular_media(a, b):
    media = (a + b) / 2
    return media


nota1 = int(input("Primeira nota: "))
nota2 = int(input("Segunda nota: "))

print()
print("Média:", calcular_media(nota1, nota2))

# Explicação:
#
# A função recebe duas notas,
# calcula a média
# e devolve o resultado através do return.
#
# Quem decide o que fazer com esse resultado
# é o programa principal.


# ============================================================
# Exemplo 8 - Funções trabalhando juntas
# ============================================================

def calcular_salario(horas, valor_hora):
    return horas * valor_hora


def calcular_inss(salario):
    return salario * 0.10


print("==== Calculadora de horas trabalhadas ====")

horas = int(input("Horas trabalhadas: "))
valor_hora = float(input("Valor da hora: "))

salario = calcular_salario(horas, valor_hora)
inss = calcular_inss(salario)
liquido = salario - inss

print()
print("Salário bruto:", salario)
print("INSS:", inss)
print("Salário líquido:", liquido)

# Explicação:
#
# Cada função possui apenas uma responsabilidade.
#
# calcular_salario()
#
# calcula o salário.
#
# calcular_inss()
#
# calcula o desconto.
#
# O programa principal organiza
# o fluxo das informações.


# ============================================================
# Ideia do Engenheiro
# ============================================================

"""
Uma boa função resolve apenas um problema.

Quanto menor for sua responsabilidade,
mais fácil será reutilizá-la,
testá-la e corrigir erros.

Programas grandes são construídos
unindo dezenas ou centenas
de pequenas funções.
"""


# ============================================================
# Exemplo 9 - Reutilizando funções
# ============================================================

def multiplicar(a, b):
    return a * b


valor1 = multiplicar(4, 5)
valor2 = multiplicar(2, 3)

total = valor1 + valor2

print(total)

# Resultado:
#
# 26

# Explicação:
#
# A mesma função foi utilizada
# duas vezes.
#
# Isso evita escrever
# a mesma lógica novamente.


# ============================================================
# Exemplo 10 - Organizando um programa
# ============================================================

def calcular_bonus(producao):
    return producao * 0.10


def calcular_salario(valor_hora, horas):
    return valor_hora * horas


print("===== Sistema =====")

horas = int(input("Horas: "))
valor_hora = float(input("Valor hora: "))
producao = int(input("Produção: "))

salario = calcular_salario(valor_hora, horas)
bonus = calcular_bonus(producao)

print()
print("Salário:", salario)
print("Bônus:", bonus)

# Explicação:
#
# Conforme o programa cresce,
# utilizar funções deixa o código
# muito mais organizado.
#
# Cada função resolve apenas
# uma pequena parte do problema.


# ============================================================
# Ideia do Engenheiro
# ============================================================

"""
Quando você escreve uma função,
está criando uma ferramenta.

Depois de pronta,
você não precisa mais pensar
em como aquela ferramenta funciona.

Basta utilizá-la.

É exatamente assim que sistemas grandes
são construídos.
"""

# ============================================================
# Conceitos importantes
# ============================================================

"""
def

→ Cria uma função.

Função

→ Um bloco de código reutilizável
que executa uma tarefa específica.

Parâmetro

→ Informação esperada pela função.

Argumento

→ Valor enviado para um parâmetro.

return

→ Devolve um resultado para quem
chamou a função.

Diferença importante

print()

Mostra uma informação na tela.

return

Entrega uma informação ao programa,
que poderá utilizá-la novamente.

Uma boa função:

✓ resolve apenas um problema;

✓ possui uma responsabilidade;

✓ pode ser reutilizada diversas vezes.
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ Funções evitam repetição de código.

✓ def cria uma função.

✓ Parâmetros recebem informações.

✓ Argumentos são os valores enviados.

✓ return devolve resultados.

✓ Uma função pode ser utilizada
diversas vezes.

✓ O programa principal organiza
a execução das funções.

✓ Comecei a dividir programas
em pequenas partes independentes.

✓ Aprendi a reutilizar cálculos
sem precisar escrever tudo novamente.
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1.
# O que significa criar uma função?

# 2.
# Qual a diferença entre parâmetro
# e argumento?

# 3.
# Para que serve o return?

# 4.
# Qual a diferença entre:

# print()

# e

# return

# 5.
# Por que funções deixam
# um programa mais organizado?


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 07

Aprendemos a utilizar o for
para repetir tarefas.

Agora colocamos essas tarefas
dentro de funções.

Aula 08

Aprendemos listas.

Nas próximas aulas,
funções e listas trabalharão juntas,
permitindo criar programas
cada vez maiores.
"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que:

# Pela primeira vez compreendi
# o verdadeiro objetivo das funções.

# Antes eu imaginava que elas apenas
# evitavam repetir código.
# Agora percebo que elas também
# ajudam a organizar o programa.

# O conceito de return demorou um pouco
# para fazer sentido.
# A compreensão veio quando percebi que
# uma função pode devolver um valor para
# continuar sendo utilizado pelo programa,
# em vez de apenas imprimir um resultado.

# Durante um exercício tentei utilizar
# uma variável criada dentro de outra
# função.
# Descobri que essa ideia não funcionava
# e encontrei uma solução recalculando
# os valores.

# Depois aprendi uma forma melhor:
# guardar o retorno da primeira função
# em uma variável e reutilizar esse
# resultado nas próximas etapas.

# Também percebi que existe diferença
# entre um programa funcionar e um
# programa estar bem organizado.

# Refatorar o código sem alterar
# o resultado faz parte do trabalho
# de um programador.

# Hoje comecei a enxergar funções
# como pequenas ferramentas
# independentes.

# Cada uma resolve apenas um problema.

# Juntas,
# conseguem construir programas
# muito maiores.

# Esta aula marcou uma mudança
# importante na minha forma de pensar.

# Pela primeira vez comecei a dividir
# um problema grande em pequenas partes,
# resolvendo cada uma separadamente.
"""


# ============================================================
# Status da Academia
# ============================================================

"""
Módulo 02 - Python

Aulas concluídas:

✓ Aula 01
✓ Aula 02
✓ Aula 03
✓ Aula 04
✓ Aula 05
✓ Aula 06
✓ Aula 07
✓ Aula 08
✓ Aula 09

Próxima aula:

Métodos de listas
"""