def contador(n):

    return len((str(n)))

 

n = str(input('diga algum número: ')).strip()

print('o número informado tem {} dígitos!'.format(contador(n)))
