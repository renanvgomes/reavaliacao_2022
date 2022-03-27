# Faça um algoritmo para mostrar a tabuada de 1 a 10.

print("[1] - Adição")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
operacao = int(input("Tabuada Infnet. Escolha a operação desejada: "))
if (operacao == 1):
    print("Opção 1 escolhida: Adição")
    num1 = int(input("Digite um número no intervalo de 1 até 10: "))
    num2 = int(input("Digite outro número no intervalo de 1 até 10: "))
    if (num1 >= 1) and (num1 <=10) and (num2 >= 1) and (num2 <=10):
        print("Processando...")
        resultado = num1 + num2
        print("O resultado da soma é: ", resultado)
    else:
        print("Número escolhido fora do intervalo de 1 até 10")    
elif (operacao == 2):
    print("Opção 2 escolhida: Subtração")
    num1 = int(input("Digite um número no intervalo de 1 até 10: "))
    num2 = int(input("Digite outro número no intervalo de 1 até 10: "))
    if (num1 >= 1) and (num1 <=10) and (num2 >= 1) and (num2 <=10):
        print("Processando...")
        if (num1 >= num2):
            resultado = num1 - num2
        elif (num2 >= num1):
            resultado = num2 - num1
        print("O resultado da subtração é: ", resultado)
    else:
        print("Número escolhido fora do intervalo de 1 até 10")    
elif (operacao == 3):
    print("Opção 3 escolhida: Multiplicação")
    num1 = int(input("Digite um número no intervalo de 1 até 10: "))
    num2 = int(input("Digite outro número no intervalo de 1 até 10: "))
    if (num1 >= 1) and (num1 <=10) and (num2 >= 1) and (num2 <=10):
        print("Processando...")
        resultado = num1 * num2
        print("O resultado da multiplicação é: ", resultado)
    else:
        print("Número escolhido fora do intervalo de 1 até 10")
elif (operacao == 4):
    print("Opção 4 escolhida: Divisão")
    num1 = int(input("Digite um número no intervalo de 1 até 10: "))
    num2 = int(input("Digite outro número no intervalo de 1 até 10: "))
    if (num1 >= 1) and (num1 <=10) and (num2 >= 1) and (num2 <=10):
        print("Processando...")
        if (num1 >= num2):
            resultado = num1 / num2
        elif (num2 >= num1):
            resultado = num2 / num1
        print("O resultado da divisão é: ", resultado)
    else:
        print("Número escolhido fora do intervalo de 1 até 10")
else:
    print("Opção inválida")
print("Fim do programa")