# Faça um algoritmo que calcule a soma dos números de 1 a 100.

soma = 0
num = 0
num = 0
num = int(input("Digite 1 para começar: "))
if (num == 1):
    while (num >= 1) and (num <= 100):
        num = int(input("Digite um número de 1 até 100: "))
        if (num >= 1) and (num <= 100):
            soma += num
else:
    print("Número digitado está incorreto")
print("Fim do programa, o resultado da soma é: ", soma)
