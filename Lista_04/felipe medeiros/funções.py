'''A funcao recebe uma sequencia de argumentos variaveis e retorna a soma destes.'''
def soma(*x):
    y = sum(x)
    print ("A soma dos elementos é",y)

'''A funcao recebe um valor real e retorna o acrescimo de 50%.'''
def acrescimo(x):
    print ("O valor mais o acrescimo é",x*1.5)
    
'''A funcao recebe uma sequencia de parametros String e retorna a concatenacao destes.'''
def concatenacao(*x):
    print("Após a concatenação: ",end="")
    for i in x:
        print(i,end="")
    print("")

'''A funcao recebe uma sequencia variavel de parametros nomeados e retorna a chave e o valor do ultimo elemento enviado'''
def funcao(**x):
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