s_altura = 0
m_alta = 0
h_baixo = 0
h_170 = 0
h_pesado = 0
h = 0
m = 0

for p in range(1, 4):
    print('''{} PESSOA'''.format(p))
    genêro = str(input("Genêro[M/F]: ")).strip().upper()
    peso = int(input("Peso: "))
    altura = int(input("Altura: "))
    s_altura += altura
    if genêro in 'M':
        h += 1
    else:
        m += 1

    if altura >= 1.70 and genêro in 'M':
        h_170 += 1
    if p == 1 and genêro in 'M':
        h_baixo = altura
        h_pesado = peso


    if genêro in 'M' and altura < h_baixo:
        h_baixo = altura
    if genêro in 'M' and peso > h_pesado:
        h_pesado = peso


    if p == 1 and genêro in 'F':
        m_alta = altura
    if genêro in 'F' and altura > m_alta:
        m_alta = altura

mediaaltura = s_altura/3
porcentagem_h = h*100/3
porcentagem_m = m*100/3

print("média altura:{}\nmulher mais alta{}\nhomem mais baixo{}\nhomens com mais de 1,70:{}"
"\nhomem mais pesado{}kg\nporcentagem de homens {}%"
"\nporcentagem de mulheres{}%".format(mediaaltura, m_alta, h_baixo, h_170, h_pesado, porcentagem_h, porcentagem_m))