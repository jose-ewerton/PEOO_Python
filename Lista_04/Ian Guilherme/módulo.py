def soma(*x):
    '''A funcao recebe uma sequencia de argumentos variaveis e retorna a soma destes.'''
    y = sum(x)
    print ("A soma dos elementos é",y)

def acrescimo(x):
    '''A funcao recebe um valor real e retorna o acrescimo de 50%.'''
    print ("O valor com acrescimo é",x*1.5)

def concat(*x):
    '''A funcao recebe uma sequencia de parametros String e retorna a concatenacao destes.'''
    print("Após a concatenação: ",end="")
    for i in x:
        print(i,end="")
    print("")

def func(**x):
    '''A funcao recebe uma sequencia variavel de parametros nomeados e retorna a chave e o valor do ultimo elemento enviado'''
    z = len(x)
    y = 1

    for i in x.keys():
        if y == z:
            print("O ultimo elemento enviado foi",i,end=": ")
            y = 1
        else:
            y += 1
    
    for i in x.values():
        if y == z:
            print(i)
        else:
            y += 1