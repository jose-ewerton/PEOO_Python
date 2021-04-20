'''receber uma sequencia de argumentos variaveis e retorna a soma.'''
def soma(*x):
    s = sum(x)
    print ("soma dos elementos",s)

'''retorna o acrescimo de 50%.'''
def acrescimo(x):
    print ("O valor mais o acrescimo é",x*1.5)
    
'''String e retorna a concatenacao destes.'''
def concatenacao(*x):
    print("Após a concatenação: ",end="")
    for i in x:
        print(i,end="")
    print("")

'''sequencia variavel de parametros nomeados e retorna a chave e o valor do ultimo elemento enviado'''
def funcao(**x):
    z = len(x)
    y = 1

    for i in x.keys():
        if y == z:
            print("O ultimo elemento enviado",i,end=": ")
            y = 1
        else:
            y += 1
    
    for i in x.values():
        if y == z:
            print(i)
        else:
            y += 1 
