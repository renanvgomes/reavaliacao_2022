# Faça um algoritmo que calcule a área de um círculo, sendo que o comprimento do raio é informado pelo usuário.
# A área do círculo é calculada multiplicando-se Pi ao raio ao quadrado.

import math

print('Atividade 08')
var1 = float(input('Digite o comprimento do raio do círculo: '))

print('Calculando a área do círculo...')
print('A área do círculo será ', round((math.pi * var1 ** 2 ), 2))