# Faça um algoritmo que leia três números e mostre o maior número.

num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
num3 = float(input("Entre com o terceiro número: "))

if (num1 > num2) and (num1 > num3):
    print("O maior número é = ", num1,)
elif (num2 > num1) and (num2 > num3):
    print("O maior número é =", num2)
else:
    print("O maior número é =", num3)
print("Fim do programa")