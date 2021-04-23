def soma(* Z):
    '''Recebe uma sequência de argumentos variáveis e retorna a soma destes.'''
    y = sum(Z)
    print("A soma dos elementos é", y)


def acrescimo(m):
    '''Recebe um valor real e retorna o acréscimo de 50%.'''
    print("O valor com acrescimo é", m * 1.5)


def concat(*Z):
    '''Recebe uma sequência de parâmetros String e retorna a concatenação destes.'''
    print("Após a concatenação: ", end="")
    for i in Z:
        print(i, end="")
    print("")


def func(**p):
    '''Recebe uma sequência variável de parâmetros nomeados e retorna a chave e o valor do ultimo elemento enviado'''
    z = len(p)
    y = 1

    for i in p.keys():
        if y == z:
            print("O ultimo elemento enviado foi", i, end=": ")
            y = 1
        else:
            y += 1

    for i in p.values():
        if y == z:
            print(i)
        else:
            y += 1