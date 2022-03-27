# Faça um algoritmo que informe se um número é primo ou não. 
# Um número primo é aquele que é divisível por um e por ele mesmo. Por exemplo, 17 é um número primo.
num = int(input("Digite um número: "))
cont = 0
for i in range(2, num):
    if (num % i == 0):
        cont += 1
if(cont == 0):
    print("É primo!")
else:
    print("Não é primo!")