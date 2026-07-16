"""
============================================================
Academia Transita
Módulo 02 - Python

Aula 06 - Laços de Repetição (while)

Data: 16/07/2026
Dia da Academia: 6
Tempo de estudo: ~3 horas

Objetivo:
Aprender a utilizar o laço while para repetir instruções
enquanto uma condição permanecer verdadeira, criando
programas interativos e sistemas que permanecem em execução
até que determinada condição seja atendida.

============================================================
"""


# ============================================================
# Exemplo 1 - Primeiro while
# ============================================================

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

print("Fim")

# Explicação:
# O while verifica a condição antes de cada repetição.
# Enquanto a condição for True, o bloco continuará sendo executado.


# ============================================================
# Exemplo 2 - Contagem regressiva
# ============================================================

contador = 10

while contador >= 1:
    print(contador)
    contador = contador - 1

print("Lançamento!")

# Explicação:
# O contador pode aumentar ou diminuir.
# O importante é que ele caminhe para tornar a condição False.


# ============================================================
# Exemplo 3 - Validação de senha
# ============================================================

senha = 0

while senha != 1234:
    senha = int(input("Digite a senha: "))

    if senha != 1234:
        print("Senha incorreta! Tente novamente.")

print("Acesso liberado!")

# Explicação:
# O programa continua solicitando a senha até que o valor
# correto seja informado.


# ============================================================
# Exemplo 4 - Menu simples
# ============================================================

opcao = 1

while opcao != 0:

    print("===== MENU =====")
    print("1 - Continuar")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

print("Sistema encerrado.")

# Explicação:
# O menu permanece ativo até que o usuário escolha sair.


# ============================================================
# Exemplo 5 - Mini Caixa Eletrônico
# ============================================================

saldo = 1000
opcao = 0

while opcao != 4:

    print()
    print("Bem-vindo ao banco!")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    print()

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Saldo: R$", saldo)

    elif opcao == 2:
        valor = float(input("Valor do saque: "))

        if valor <= saldo:
            saldo -= valor
            print("Saque realizado.")
            print("Novo saldo:", saldo)
        else:
            print("Saldo insuficiente.")

    elif opcao == 3:
        valor = float(input("Valor do depósito: "))
        saldo += valor
        print("Depósito realizado.")
        print("Novo saldo:", saldo)

    elif opcao == 4:
        print("Obrigado por utilizar o banco!")

    else:
        print("Opção inválida.")


# ============================================================
# Conceitos importantes
# ============================================================

"""
while

→ Significa "enquanto".

→ Repete um bloco de código enquanto a condição
for verdadeira.

Estrutura:

while condição:
    bloco

O Python verifica a condição antes de cada repetição.

Quando a condição se torna False,
o programa continua normalmente.
"""


# ============================================================
# Resumo da Aula
# ============================================================

"""
Hoje aprendi que:

✓ while cria repetições.

✓ A condição é verificada antes de cada repetição.

✓ Toda repetição precisa conseguir terminar.

✓ Caso a condição nunca fique False,
o programa entra em loop infinito.

✓ while pode ser usado para:

- Contadores
- Contagens regressivas
- Menus
- Validação de senha
- Sistemas interativos
"""


# ============================================================
# Perguntas para revisão
# ============================================================

# 1. O que significa while?

# 2. Quando o Python verifica a condição do while?

# 3. O que é um loop infinito?

# 4. O que faz o contador = contador + 1?

# 5. Por que o contador precisa ser atualizado?


# ============================================================
# Ligação com aulas anteriores
# ============================================================

"""
Aula 04

Aprendi a receber informações do usuário utilizando input().

Nesta aula, essas informações passaram a controlar
o fluxo de repetição do programa.


Aula 05

Aprendi a tomar decisões utilizando if, elif e else.

Nesta aula, while e if passaram a trabalhar juntos,
permitindo criar sistemas completos.
"""


# ============================================================
# Caderno de Engenharia
# ============================================================

"""
Hoje percebi que:

Aprendi que while não serve apenas para contadores.
Ele mantém um programa funcionando enquanto uma condição
for verdadeira.

Também percebi que toda repetição precisa ter uma forma
de terminar. Caso contrário, criaremos um loop infinito.

Ao construir o sistema do banco e o controle de acesso,
comecei a pensar mais no comportamento do sistema do que
apenas na sintaxe do Python.


# ----------------------------------------------------------
# Anotações do aluno
# ----------------------------------------------------------

- Percebi que ler a condição do while em português evita
  muitos erros de lógica.

- Comecei a enxergar o programa como blocos:
  menu → escolha → decisão → volta ao menu.

- No exercício do banco imaginei a solução antes de
  começar a escrever o código.

- Descobri que operadores como += e -= são apenas formas
  reduzidas de atualizar uma variável.

- No sistema de controle de acesso percebi que escrevi
  "while crachá != 0", quando na verdade queria
  "while crachá != 123456". O erro não era no while,
  era na condição que eu mesmo escrevi.

- A principal evolução desta aula foi deixar de pensar
  apenas em linhas de código e começar a pensar no
  comportamento completo do sistema.
"""