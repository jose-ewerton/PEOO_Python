print('Função para soma')
def soma(*args):
    x = 0
    for entradas in args:
        x += entradas
    return x


print(soma(4,8,10))