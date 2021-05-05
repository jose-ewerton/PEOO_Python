def contador(v):
    return len((str(v)))
v = str(input('digite um número grande: ')).strip()
print('seu número tem {} dígitos'.format(contador(v)))