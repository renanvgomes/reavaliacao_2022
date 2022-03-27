# Faça um algoritmo que apresente a sequência de Fibonacci. 
# A sequência começa com 0 e 1, e então produz o próximo número de Fibonacci somando os dois anteriores para formar o próximo. 
# Por exemplo, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946...

n = int(input("Sequência de Fibonacci, digite o número de rodadas que deseja que o programa calcule: "))
num1 = 0
num2 = 1
print(num1, num2, end = " ")
for i in range (n):
    res = num1 + num2
    num1 , num2 = num2, res
    print(res, end = " ")
    