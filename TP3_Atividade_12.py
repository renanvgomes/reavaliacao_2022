# Faça um algoritmo que leia uma opção de um menu sendo [1] Soma, [2] Subtração, [3] Multiplicação e [4] Divisão. 
# Se a opção for válida, o programa deverá ler os operandos, realizar a operação e mostrar o resultado. 
# Caso contrário, o programa deverá exibir uma mensagem de operação inválida. O programa termina quando o usuário digita 0.

FIM = 0

def entra_opcao():
    opcao_ok = False
    while (not opcao_ok):
        try:
            opcao = int(input("Entre com uma opção: "))
            if (opcao < 0) or (opcao > 4):
                print("Erro: opção inválida")
            else:
                opcao_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return opcao

def menu():
    opcao_ok = False
    while (not opcao_ok):
        print("Menu")
        print("[1] - Soma")
        print("[2] - Subtração")
        print("[3] - Multiplicação")
        print("[4] - Divisão")
        print("[0] - Sair")
        return entra_opcao()

def entra_operando():
    dado_ok = False
    while (not dado_ok):
        try:
            op = float(input("Entre com um número: "))
            dado_ok = True
        except ValueError:
            print("Entrada inválida")
    dado_ok = False
    return op

def soma(op1, op2):
    result = op1 + op2
    return result

def subtracao(op1, op2):
    result = op1 - op2
    return result

def multiplicacao(op1, op2):
    result = op1 * op2
    return result

def divisao(op1, op2):
    if (op2 == 0):
        return "Erro: operando inválido"
    result = op1 / op2
    return result
    
opcao = menu()
while (opcao != FIM):
    op1 = entra_operando()
    op2 = entra_operando()
    if (opcao == 1):
        print("Soma = ", soma(op1, op2))
    elif (opcao == 2):
        print("Subtração = ", subtracao(op1, op2))    
    elif (opcao == 3):
        print("Multiplicação =", multiplicacao(op1, op2))
    elif (opcao == 4):
        print("Divisão =", divisao(op1, op2))
    else:
        print("Erro: opção inválida")
    opcao = menu()
print("Fim do programa")