# Faça um algoritmo que calcule a área de uma esfera, sendo que o comprimento do raio é informado pelo usuário. 
# A área da esfera é calculada multiplicando-se 4 vezes Pi ao raio ao quadrado.

import math

print('Atividade 09')
var1 = float(input('Digite o comprimento do raio da esfera: '))
print('Calculando a área da esfera...')
print('A área da esfera será ', round((4 * math.pi * var1 ** 2 ), 2))