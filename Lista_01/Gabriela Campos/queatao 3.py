#receba a idade e a opinião de 15 espectadores de um cinema em relação
#um determinado filme, sendo ótimo - 3, bom - 2, regular -1
#calcule e informe

#média das idades das pessoas que responderam ótimo;
#quantidade de pessoas que responderam regular;
#a porcentagem de pessoas que responderam bom entre todos os espectadores analisados

o = 0 #otimo
bom = 0
r = 0 #regular
media = 0

for t in range (1,16):
    idade = int(input("sua idade: "))
    opiniao = int(input("qual sua opinião sobre o filme?\n1 = REGULAR\n2 = BOM\n3 = OTIMO\nInforme: "))
    if opiniao == 3:
        media += idade
        o += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 1:
        r += 1
    else:
        print ("NÚMERO INVÁLIDO")
        break

media = media/o
p = bom*100/15

print ("A média de idade dos telespectadores que responderam ÓTIMO é ",media," anos.")
print (r,"% pessoas acharam o filme REGULAR.")
print (p,"% de todas as pessoas responderam BOM.")
