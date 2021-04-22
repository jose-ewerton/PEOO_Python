so = 0
qr = 0
pb = 0

print(''' 
Olá, este é um programa para você dar sua opinião do filme que assistiu.
cuja classificação consiste em:
Digite "1" para REGULAR;
Digite "2" para BOM;
Digite "3" para ÓTIMO;
''')
for c in range (1,16):
    print('---------- {}ª PESSOA ----------'.format(c))
    i = int(input('Informe sua idade, por favor:'))
    c = int(input('Informe sua opinião:'))

    if c == 3:
        so = so + c
    if c == 1:
        qr = qr + 1
    if c == 2:
        pb = pb + 1

pbg = (100 * pb) / 5
mo = so / 5

print('A média dos que responderam ótimo é {}'.format(mo))
print('Foram {} pessoas que responderam "regular"(1)'.format(qr))
print('Do total, {}% foi das pessoas que responderam "bom"(2)'.format(pbg))
