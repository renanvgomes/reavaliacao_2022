# Faça um algoritmo que receba um número inteiro, que representa um determinado mês do ano, e mostre o nome do mês correspondente.
# Por exemplo, se for informado o número 2, algoritmo deverá exibir fevereiro. O algoritmo deve validar se a entrada está correta.

print("[1]: Janeiro")
print("[2]: Fevereiro")
print("[3]: Março")
print("[4]: Abril")
print("[5]: Maio")
print("[6]: Junho")
print("[7]: Julho")
print("[8]: Agosto")
print("[9]: Setembro")
print("[10]: Outubro")
print("[11]: Novembro")
print("[12]: Dezembro")
menu = int(input("Escolha o número de acordo com o mês desejado: "))
if (menu == 1):
    print("Janeiro")
elif (menu == 2):
    print("Fevereiro")
elif (menu == 3):
    print("Março")
elif (menu == 4):
    print("Abril")
elif (menu == 5):
    print("Maio")
elif (menu == 6):
    print("Junho")
elif (menu == 7):
    print("Julho")
elif (menu == 8):
    print("Agosto")
elif (menu == 9):
    print("Setembro")
elif (menu == 10):
    print("Outubro")
elif (menu == 11):
    print("Novembro")
elif (menu == 12):
    print("Dezembro")
else:
    print("Opção inválida")