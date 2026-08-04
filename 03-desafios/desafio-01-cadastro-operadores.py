operadores = []
for operador in range(5):
    print("Cadastro de Operadores")
    operadores.append(input("Digite o nome do operador: "))
print()
print("==== Operadores cadastrado ====")
for operador in operadores:
    print(operador)
print()
operadores.remove(input("Digite o nome do operador que saiu do turno: "))
operadores.append(input("Digite o nome do operador que entrou no turno: "))
operadores.sort()
print()
print("==== TURNO ATUAL ====")
for operador in operadores:
    print(operador)
print()
print("Total de operadores no turno: ", len(operadores))
