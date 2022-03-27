# Faça um algoritmo que leia uma sequência de números inteiros terminado por zero e mostre a soma, média, o maior número e o menor número da sequência.

soma = 0
media = 0
maior_numero = 0
menor_numero = 0
cont = 0
num_ok = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range (0, 100, 10):
    numero = int(input("Você digitará 10 números entre o intervalo de 0 até 100: "))
    if numero in (num_ok):
        soma = (soma + numero)
        media = (soma / 10)
        if (maior_numero == 0) and (menor_numero == 0) and (cont < 1):
            maior_numero = numero
            menor_numero = numero
            cont +=1
        elif numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero
    else:
        print("Número inválido! Serão aceitos números terminados com 0")
print ("O resultado da soma dos números digitados é de: ", soma)
print ("A média dos número digitados é de: " , media)
print ("O maior número digitado foi o : " , maior_numero)
print ("O menor número digitado foi o: " , menor_numero)