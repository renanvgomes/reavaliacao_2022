# Faça um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste. 
# O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7.3%.
print('Atividade 05')
var1 = float(input('Qual o valor do salário?: '))
var2 = float(input('Qual o percentual do reajuste?: '))
salario_novo = var1 + ((var1 * var2)/100)
print('O valor do salário reajustado será: ', (salario_novo))