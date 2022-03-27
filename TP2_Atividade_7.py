# Faça um algoritmo que calcule e mostre o novo valor de um salário a partir das seguintes regras: 
# salários de até R$ 1.000,00 recebem 30% de aumento
# salários de até R$ 2.000,00 recebem 25%
# salários de até R$ 3.000,00 recebem 20%
# salários de até R$ 4.000,00 recebem 15%
# salários acima de R$ 4.000,00 recebem apenas 10%.

print("[1] Até R$1.000")
print("[2] Entre R$1.001 até R$2.000")
print("[3] Entre R$2.001 até R$3.000")
print("[4] Entre R$3.001 até R$4.000")
print("[5] Acima de R$ R$4.000")
menu = int(input("Escolha a sua faixa salarial: "))
if (menu == 1):
    print("Salários de até R$1.000")
    salario = float(input("Digite o seu salário [Ex.: 1000]: "))
    if (salario <= 1000):
        print("Calculando seu salário...")
        resultado = (salario * 1.30)
        print("O seu novo salário será: ", round(resultado, 4))
    else:
        print("Salário inválido para essa opção")
elif (menu == 2):
    print("Salários entre R$1.001 até R$2.000")
    salario = float(input("Digite o seu salário [Ex.: 1001]: "))
    if (salario >= 1001) and (salario <= 2000):
        print("Calculando seu salário...")
        resultado = (salario * 1.25)
        print("O seu novo salário será: ", round(resultado, 4))
    else:
        print("Salário inválido para essa opção")
elif (menu == 3):
    print("Salários entre R$2.001 até R$3.000")
    salario = float(input("Digite o seu salário [Ex.: 2001]: "))
    if (salario >= 2001) and (salario <= 3000):
        print("Calculando seu salário...")
        resultado = (salario * 1.20)
        print("O seu novo salário será: ", round(resultado, 4))
    else:
            print("Salário inválido para essa opção")
elif (menu == 4):
    print("Salários entre R$3.001 até R$4.000")
    salario = float(input("Digite o seu salário [Ex.: 3001]: "))
    if (salario >= 3001) and (salario <= 4000):
        print("Calculando seu salário...")
        resultado = (salario * 1.15)
        print("O seu novo salário será: ", round(resultado, 4))
    else:
        print("Salário inválido para essa opção")
elif (menu == 5):
    print("Salários acima de R$4.000")
    salario = float(input("Digite o seu salário [Ex.: 4001]: "))
    if (salario > 4000):
        print("Calculando seu salário...")
        resultado = (salario * 1.10)
        print("O seu novo salário será: ", round(resultado, 4))
    else:
        print("Salário inválido para essa opção")
else:
    print("Opção inválida")
print("Fim do programa")