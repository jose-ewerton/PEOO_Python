def num(*args):
    print('A soma dos argumentos é {}'.format(float(sum(args))))

num(1,2,4.6)

def quan(*args):
    print('A quantidade de argumentos é {}.'.format(len((args))))

quan(1,2,4.6)