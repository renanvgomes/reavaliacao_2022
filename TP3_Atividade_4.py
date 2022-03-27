# Faça um algoritmo que leia uma sequência de n números inteiros e mostre a soma, média, o maior número e o menor número da sequência.

soma = 0
media = 0
maior_numero = 0
menor_numero = 0
cont = 0
n = int(input("Quantos números deseja verificar? "))
for i in range (n):
    numero = int(input("Digite um número: "))
    soma = (soma + numero)
    media = (soma / n)
    if (maior_numero == 0) and (menor_numero == 0) and (cont < 1):
        maior_numero = numero
        menor_numero = numero
        cont +=1
    elif numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero
print ("O resultado da soma dos números digitados é de: ", soma)
print ("A média dos número digitados é de: " , media)
print ("O maior número digitado foi o : " , maior_numero)
print ("O menor número digitado foi o: " , menor_numero)