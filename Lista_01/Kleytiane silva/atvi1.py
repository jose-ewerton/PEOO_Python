medg = 0.0  # media
alt = 0.0  # altura
fea = 0.0  # mulheralta
mab = 0.0  # homembaixo
masp = 0.0  # homempesado
max = 0  # homem
fex = 0  # mulher

for c in range(1, 4):
    sexo = input('Digite a primeira letra do seu sexo, F para feminino ou M para masculino:')
    peso = float(input('Digite seu peso atual:'))
    alt = float(input('Digite sua altura:'))

    medg = alt + medg
    if sexo == 'F':
        if alt > fea or fea == 0.0:
            fea = alt
            fex = fex + 1

    elif sexo == 'M':
        if peso > masp:
            masp = peso
        if alt < mab or mab == 0.0:
            mab = alt
        if alt > 1.70:
            max = max

print("Média de altura das pessoas que responderam:", sum(alt)/len())
print('A média de altura do grupo avaliado na pesquisa:', sum(medg) / 3)
print('A mulher mais alta da pesquisa:', fea)
print('homem mais baixo da pesquisa:', mab)
print('O número de homens com mais de 1,70 m de altura:', max)
print('O homem mais pesado:', masp)
print('O percentual de homens que responderam essa pesquisa:', max)
print('O percentual de  mulheres que responderam essa pesquisa:', fex)
