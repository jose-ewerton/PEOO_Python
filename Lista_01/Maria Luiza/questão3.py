"""Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
a um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
a. A média das idades das pessoas que responderam ótimo;
b. A quantidade de pessoas que responderam regular;
c. A porcentagem de pessoas que responderam bom entre todos os espectadores analisados."""

ótimo = 0
regular = 0
bom = 0
médiaótimo = 0

for p in range(1, 16):
    idade = int(input("Digite sua idade: "))
    opnião = int(input("Qual sua opnião sobre o filme?"
              "3 - ótimo, 2 - bom , 1 - regular:"))
    if opnião == 3:
        médiaótimo += idade
        ótimo += 1
    elif opnião == 2:
        bom += 1
    elif opnião == 1:
        regular += 1
    else:
        print('\033[31m'"NÚMERO INVÁLIDO"'\033[31m')
        break

médiaótimo = médiaótimo/ótimo
porcentagem = bom*100/15
print('\033[1m'f"A média de idade das pessoas que responderam 'ÓTIMO' foi {médiaótimo}")
print(f"{regular} pessoas responderam 'REGULAR'!")
print(f"{porcentagem:.2f}% das pessoas responderam 'BOM' entre todos os espectadores analisados!"'\033[m')