print("="*40)
print( "           1º LISTA (QUESTÃO 3)        ")
print("="*40)
print("\n")
#receber a idade de 15 espectadores de um cinema
#receber a opnião  em relação a um determinado filme
#se ótimo(-3), se bom(-2), se regular(-1)
#calcular a média das idades das pessoas que responderam ótimo
#calcular a quantidade das pessoas que responderam regular
#calcular a porcentagem de pessoas que responderam bom entre todos os espectadores
#informar o resultado das somas

a = 0
b = 0
d = 0
idade = []

for c in range(1, 16):
    idade.append(int(input("{}° espectador, digite sua idade: ".format(c))))
    c = int(input("Digite um número conforme sua opinião sobre o filme (se ótimo: 3, se bom: 2, se regula: 1): "))

    if c == 3:
        d += c

    elif c == 2:
        b += 1

    else:
        a += 1

media = sum(idade) / len(idade)
por = (100 * b) / 15

print("A média de idade: {}".format(media))
print("A quantidade de respostas regulares: {}".format(a))
print("A procentagem de respostas, bom entre todos os espectadores: {}%".format(por))