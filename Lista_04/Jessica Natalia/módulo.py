def soma(*aaa):
    '''A função recebe uma sequência de argumentos variáveis e retorna a soma total.'''
    print(sum(aaa))

def acres(x):
    '''A função recebe um valor real e acrescenta 50%.'''
    print(x*1.5)  

def concat(*bbb):
    '''A função recebe parâmetros String variáveis e retorna à concatenação.'''
    for j in bbb:
        print(j,end="")
    print("")

def retorna_ultimo(**ccc):
    '''A função recebe uma sequência variável de parâmetros nomeados e retorna o último elemento enviado'''
    j = len(ccc)
    n = 1

    for x,y in ccc.items():
        if n == j:
            print (f'O último elemento enviado foi {x}: {y}')
        else:
            n += 1
