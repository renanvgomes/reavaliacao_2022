# Uma progressão aritmética é uma sequência numérica em que cada termo, a partir do segundo, é igual a soma do termo anterior com uma constante. 
# A constante é calculada como sendo a diferença entre o segundo e o primeiro número. 
# Faça um algoritmo que receba dois números inteiros e, a partir dessa informação, gere uma sequência em progressão aritmética.

num1 = 0
num2 = 0
res = 0
const = 0
res_final = 0
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if (num1 < num2):
    n = int(input("Digite o número de rodadas que deseja que o programa calcule: "))
    for i in range (n):        
        const = num2 - num1
        res = res + const
        res_final = res + num2
        print(res_final)
else: ("O primeiro número precisa ser menor que o segundo número")