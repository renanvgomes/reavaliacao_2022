# Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.

numero = float(input("Entre com um número: "))
if(numero < 0):
    print("O número = ", numero, "é negativo")
elif (numero == 0):
    print("Número zero")
elif (numero >= 1):
    print("Número = ", numero, "é posítivo")
print("Fim do programa")