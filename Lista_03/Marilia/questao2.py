#função
def contador(n):
    return len((str(n)))

#código principal e saída
n = str(input('informe um número: ')).strip()
print('o número informado tem {} dígitos!'.format(contador(n)))

