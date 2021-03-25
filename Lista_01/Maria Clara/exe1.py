soma = 0
media = 0
homens = 0
menos = 0
baixo = ''
mulher = 0
alta = ''
homem = 0
pesado = ''
percem = 0
percef = 0
totH = 0
totM = 0
cont = 0
for c in range(1, 3):
    print(f'-=-=-=-=-=- {c}ª Pessoa -=-=-=-=-=-= ')
    nome = str(input('Qual é o seu nome: '))
    altura = float(input('Qual é a sua altura: '))
    peso = float(input('Qual é seu peso: '))
    sexo = str(input('Qual o seu gênero (M/F): '))
    soma += altura
    cont += 1
    if altura > 170 and sexo == 'Mm':
        homens += 1
    if c > altura and sexo in 'Mm':
        menos = altura
        baixo = nome
    if c < altura and sexo in 'Ff':
        mulher = altura
        alta = nome
    if c > peso and sexo in 'Mm':
        homem = peso
        pesado = nome
    elif sexo in 'Ff':
        totM += 1
        percef = 100 * (c/totM)
    elif sexo in 'Mm':
        totH += 1
        percem = 100 * (c/totH)
media = soma / 2
print(f'A média de altura do grupo {media:.2f}')
print(f'O nome da mulher mais alta: {alta}')
print(f'O nome do homem mais baixo: {baixo}')
print(f'O número de homens com mais de 1,70 m de altura: {homens}')
print(f'O homem mais pesado: {pesado}')
print(f'O percentual de homens: {percem} e o de mulheres: {percef} ')
