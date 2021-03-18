otimo = []
bom = []
regular = []
soma = []
numero = 1
while numero < 16:
    print (numero,'*Individuo.')
    idade = int(input('Digite a idade: '))
    opiniao = float(input('Digite a opinião,(3-ótimo ,2-bom, 1-regular): '))
    if opiniao == 3:
        soma.append(idade)
    if opiniao == 3:
        otimo.append(1)
        numero = numero+1
    elif opiniao == 1:
        regular.append(1)
        numero = numero+1
    elif opiniao == 2:
        bom.append(1)
        numero = numero+1
    else:
        print('Resposta inválida! Tente de novo.')
media = sum(soma)
total = len(otimo)
resultado = len(regular)
fins = len(bom)
print('A média das idades das pessoas que responderam ótimo: ',media/total)
print('A quantidade de pessoas que responderam regular: ',resultado)
print ('A porcentagem de pessoas que responderam bom entre todos os espectadores analisados: Bom =',fins*6.6,',Ótimo =',total*6.6,',Regular =',resultado*6.6)



