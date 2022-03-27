# Faça um algoritmo que leia uma sequência de caracteres terminada por um ponto e mostre o número de vogais da frase. 
# Cada caractere deve ser digitado/lido separadamente.
# Exemplo:
# Entre com um caractere: a
# Entre com um caractere: @
# Entre com um caractere: x
# Entre com um caractere: 2
# Entre com um caractere: e
# Entre com um caractere: .
# Número de vogais: 2

cont = 0
carac = ""
vogais1 = ["A","E","I","O","U"]
vogais2 = ["a","e","i","o","u"]
while (carac != "."):
    carac = input("Digite um caractere: ")
    if (carac in vogais1) or (carac in vogais2):
        cont += 1
print ("Fim do programa, total de vogais: ", cont)
