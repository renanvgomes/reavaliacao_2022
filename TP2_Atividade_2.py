# Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.

numero = float(input("Entre com um número: "))
resto = numero % 2
if (resto == 0):
    print("O número = ", numero, "é par")
else:
    print("O número =", numero, "é ímpar")
print("Fim do programa")