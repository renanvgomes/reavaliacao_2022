# Faça um algoritmo que calcule o volume de uma caixa de água cilíndrica, sendo que os comprimentos do raio e a altura são informados pelo usuário.
# O volume é calculado multiplicando-se Pi, ao raio ao quadrado, a altura.

import math

print('Atividade 10')
var1 = float(input('Digite o comprimento do raio da caixa de água: '))
var2 = float(input('Digite a altura da caixa de água: '))
print('Calculando o volume da caixa de agua...')
resultado = round((math.pi * var1 ** 2 * var2), 2)
resultado_final = round(resultado, 2)
print('O volume da caixa de água será ', resultado_final)