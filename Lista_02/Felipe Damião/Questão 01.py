a = []
b = []
aa = ()
aaa = 0
bb = ()
bbb = 0
cc = ()
ccc = 0
dd = ()
ddd = 0
ee = ()
eee = 0

while aaa == 0:
    aa = str(input("Telefonou para a vítima?(Escreva gramaticalmente correto!):"))
    if aa == 'Sim':
        a.append(1)
        aaa = aaa+1 
    elif aa == 'Não':
        b.append(1)
        aaa = aaa+1
    else:
        print('Responda SIM ou NÃO e/ou escreva gramaticalmente correto!.')

while bbb == 0:
    bb = str(input("Esteve no local do crime?(Escreva gramaticalmente correto!):"))
    if bb == 'Sim':
        a.append(1)
        bbb = bbb+1 
    elif bb == 'Não':
        b.append(1)
        bbb = bbb+1
    else:
        print('Responda SIM ou NÃO e/ou escreva gramaticalmente correto!.')

while ccc == 0:
    cc = str(input("Mora perto da vitíma?(Escreva gramaticalmente correto!):"))
    if cc == 'Sim':
        a.append(1)
        ccc = ccc+1 
    elif cc == 'Não':
        b.append(1)
        ccc = ccc+1
    else:
        print('Responda SIM ou NÃO e/ou escreva gramaticalmente correto!.')

while ddd == 0:
    dd = str(input("Devia para a vitíma?(Escreva gramaticalmente correto!):"))
    if dd == 'Sim':
        a.append(1)
        ddd = ddd+1 
    elif dd == 'Não':
        b.append(1)
        ddd = ddd+1
    else:
        print('Responda SIM ou NÃO e/ou escreva gramaticalmente correto!.')

while eee == 0:
    ee = str(input("Já trabalhou com a vitíma?(Escreva gramaticalmente correto!):"))
    if ee == 'Sim':
        a.append(1)
        eee = eee+1 
    elif ee == 'Não':
        b.append(1)
        eee = eee+1
    else:
        print('Responda SIM ou NÃO e/ou escreva gramaticalmente correto!.')

f = sum(a)

if f == 0:
    print('O individuo é inocente.')
if f == 1:
    print('O individuo é inocente.')
elif f == 2:
    print('O individuo é suspeito.')
elif f == 3:
    print('O individuo é cúmplice.')
elif f == 4:
    print('O individuo é cúmplice.')
elif f == 5:
    print('O individuo é assassino.')



