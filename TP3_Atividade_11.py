# Faça um algoritmo que leia uma sequência de números terminada em zero e mostre para cada número lido se ele é primo ou não.
print("O intervalo que será testado é de 10 até 90")
cont = 0
for i in range(10, 100, 10):
    print(i, end = " ")
    if (10, 20, 30, 40, 50, 60, 70, 80, 90 % i == 0):
        cont += 1
    elif(cont == 1):
        print()
        print("São primos!")
        print(i)
else:
    print()
    print("Não são primos!")