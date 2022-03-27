# Faça um algoritmo que leia um intervalo inferior e superior, e mostre os números primos existentes no intervalo. 
# Por exemplo, o algoritmo recebe 5 e 10, e mostra como saída 5 e 7. 
# Além disso, o algoritmo deve mostrar a quantidade de números primos encontrados no intervalo.
inteiro = True
primo = []
cont = 0
while(inteiro):
    try:        
        num1 = int(input("Digite o primeiro número do intervalo: "))
        num2 = int(input("Digite o segundo número do intervalo: "))
        if(num1 < num2):
            inteiro = False
    except:
        print("Erro: Digite apenas números inteiros")
for i in range(num1, num2 + 1):
    num_primo = True
    for j in range(2, i):
        if (i % j == 0):
            num_primo = False
            break
    if (num_primo):
        primo.append(i)
        cont += 1
print("Total de números primos: ", cont)
print("Os números primos são ", primo)