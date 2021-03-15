pm = pf = tot170 = totH = totM = soma = quant = altura = média = maior = menor = 0
while True:
    peso = float(input('Qual é o seu peso? (Kg) '))
    altura = float(input(' Qual é sua altura? (m) '))
    sexo = ' '
    soma += altura
    quant += 1
    if quant == 1:
        maior = menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
        if altura > 1.70:
            tot170 += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        totH += 1
    if sexo == 'F':
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f' No total temos {totH} homens cadastrados')
print(f'E temos {totM} mulheres cadastras')
média = soma / quant
Soma = totM + totH
pf = int((totM/Soma)*100)
pm = int((totH/Soma)*100)
print('tivemos {} dados mostrados sobre a altura e a média foi {}'.format(quant, média, soma))
print('A maior altura indicada foi {} e a menor foi {}'.format(maior, menor))
print('Total de pessoas com mais de 1.70 de altura foi {}'.format(tot170))
print('O percentual de homens foi {}'.format(pm))
print('O percentual de mulheres foi {}'.format(pf))