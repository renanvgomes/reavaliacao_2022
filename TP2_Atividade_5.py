# Faça um algoritmo que leia uma opção de um menu sendo [1] Soma, [2] Subtração, [3] Multiplicação e [4] Divisão.
# Se a opção for válida, o programa deverá ler os operandos, realizar a operação e mostrar o resultado. 
# Caso contrário, o programa deverá exibir uma mensagem de operação inválida.

print("[1] Soma")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
menu = int(input("Escolha a operação desejada do menu: "))
if (menu == 1):
    print("Opção escolhida: Soma")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é = ", resultado)
elif (menu == 2):
    print("Opção escolhida: Subtração")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("O resultado da subtração é = ", resultado)
elif (menu == 3):
    print("Opção escolhida: Multiplicação")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("O resultado da multiplicação é = ", resultado)
elif (menu == 4):
    print("Opção escolhida: Divisão")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão é = ", resultado)
else:
    print("Opção inválida")
print("Fim do programa")
