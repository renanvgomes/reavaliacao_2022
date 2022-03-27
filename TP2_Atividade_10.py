# Faça um algoritmo que valide uma data, formada por dia, mês e ano. 
# Por exemplo, a data 30/2 é inválida, porém a data 29/2/2012 é válida.

from calendar import isleap

data = input("Digite a data nesse formato [dia/mês/ano] Ex.: 25/1/2021: ")
formato = data.split("/")
dia = int(formato[0])
mes = int(formato[1])
ano = int(formato[2])
print("Dia: ", formato[0])
print("Mês: ", formato[1])
print("Ano: ", formato[2])
if ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and (1 <= dia <= 31) and (0 <= ano <= 9999):         
    print("Data está correta ", data)
elif ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (1 <= dia <= 30) and (0 <= ano <= 9999):        
    print("Data está correta ", data)
elif (mes == 2) and (isleap(ano)) and (1 <= dia <= 29):
    print("Data está correta ", data)
elif (mes == 2) and (1 <= dia <= 28):
    print("Data está correta ", data)
else:
    print("Data no formato inválido")
print("Fim do programa")