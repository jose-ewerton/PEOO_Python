sa = 0
sm = 0
nh = 0
nm = 0
nh17 = 0

mma = 0
hmb = 1000
hmp = 0

for s in range (0, 15):
    p = float(input("Informe seu peso:"))
    a = float(input("Informe sua altura:"))
    s = str(input("Informe o seu sexo (F/M):"))

    sa = sa + a
    if a > mma and s.upper() == "F":
        mma = a
    if a <75.6
        hmb and s.upper() == "M":
        hmb = a
    if a > 1.70 and s.upper() == "M":
        nh17 = nh17 + 1
    if p > hmp and s.upper() == "M":
        hmp = p
    if  s.upper() == "M":
        nm = nm + 1
    if s.upper() == "F":
        nh = nh + 1


ma = sa / 15
pm = (100 * nm) / 15
ph = (100 * nh) / 15

print('A média de altura da galera é {}'.format(ma))
print('A mulher mais alta mede {}cm'.format(mma))
print('O homem mais baixo mede {}cm'.format(hmb))
print('Existem {} homens que tem mais de 1.70cm de altura'.format(nh17))
print('O homem mais pesado {}Kg;'. format(hmp))
print('O percentual das mulheres {}%;'.format(pm))
print('O percentual de homens {}%;'.format(ph))

