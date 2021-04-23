soma = 0
soma2 = 0
media = 0
porcen = 0
po = 0
for c in range(1, 15 + 1):
    print(f'-=-=-=-=-=- {c}ª Pessoa -=-=-=-=-=-= ')
    idade = int(input('Qual a sua idade: '))
    opiniao = int(input('Qual e a sua opinão sobre o filme [Ótimo - 3, Bom - 2, Regular - 1]: '))

    if opiniao == 1:
        soma2 += opiniao
    if opiniao == 2:
        po = (c / 100)
        porcen = 100 * po
    if opiniao == 3:
        soma += idade
        media = soma / c
print(f'A média das idades das pessoas que responderam ÓTIMO foi: {media} ')
print(f'A quantidade de pessoas que responderam REGULAR foi: {soma2} ')
print(f'A porcentagem de pessoas que responderam BOM entre todos os espectadores foi: {porcen} % ')
