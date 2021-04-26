'''
Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, em
seguida calcule e informe:
a. A média de altura do grupo;
b. A mulher mais alta e o homem mais baixo;
c. O número de homens com mais de 1,70 m de altura;
d. O homem mais pesado;
e. O percentual de homens e de mulheres
'''
somalt = 0
medalt = 0
mulheralta = 0
nomealta = 0
homembaixo = 0
nomebaixo = 0
tothomem1_70 = 0
homempeso = 0
nomepeso = 0
h = 0
m = 0
for p in range(1, 5):
    print('----- {}° Pessoa -----'.format(p))
    nome = str(input('Informe o nome:')).strip()
    altura = float(input('Informe a altura:'))
    peso = float(input('Informe o peso:'))
    sexo = str(input('Informe o sexo [M/F]:')).strip()
    somalt += altura
    if p == 1 and sexo in 'Ff':
        mulheralta = altura
        nomealta = nome
    if sexo in 'Ff' and altura > mulheralta:
        mulheralta = altura
        nomealta = nome
    if p == 1 and sexo in 'Mm':
        homembaixo = altura
        nomebaixo = nome
    if sexo in 'Mm' and altura < homembaixo:
        homembaixo = altura
        nomebaixo = nome
    if sexo in 'Mm' and altura > 1.70:
        tothomem1_70 += 1
    if p == 1 and sexo in 'Mm':
        homempeso = peso
        nomepeso = nome
    if sexo in 'Mm' and peso > homempeso:
        homempeso = peso
        nomepeso = nome
    if sexo in 'Mm':
        h += 1
    else:
        m += 1
porhomem = h*100 / 4
pormulher = m*100 / 4
print('-'*12)
medalt = somalt / 4
print('A média de altura do grupo é {}'.format(medalt))
print('A mulher mais alta tem {} de altura e se chama {}'.format(mulheralta, nomealta))
print('O homem mais baixo do grupo tem {} de altura e se chama {}'.format(homembaixo, nomebaixo))
print('A quantidade de homens com mais de 1.70 é de {}'.format(tothomem1_70))
print('O homem mais pesado do grupo tem {}kg e se chama {}'.format(homempeso, nomepeso))
print('O percentual de homens é de {}% e o de mulheres de {}%'.format(porhomem, pormulher))