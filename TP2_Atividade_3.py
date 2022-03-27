# Faça um algoritmo que leia dois números e mostre o maior número.

num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))

if (num1 > num2):
    print("O maior número é = ", num1,)
elif (num1 < num2):
    print("O maior número é =", num2)
else:
    print("Os números são iguais")
print("Fim do programa")