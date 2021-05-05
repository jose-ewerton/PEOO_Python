#valores iniciais
ótimo = 0
regular = 0
bom = 0
médiaótimo = 0

#código principal
for p in range(1, 6):
    idade = int(input("idade: "))
    op = int(input("digite o número referente a sua opnião sobre o filme?"
              " 1=regular/2=bom/3=ótimo:"))
    if op == 3:
        médiaótimo += idade
        ótimo += 1
    elif op == 2:
        bom += 1
    elif op == 1:
        regular += 1
    else:
        print("NÚMERO INVÁLIDO")
        break

#valores finais
médiaótimo = médiaótimo/ótimo
porcentagem = bom*100/5

#saída
print("As pessoas que responderam 'ÓTIMO' tem em média {} anos.".format(médiaótimo))
print("{} pessoas acharam o filme 'REGULAR'!".format(regular))
print("{:.2f}% de todas as pessoas responderam 'BOM'!".format(porcentagem))