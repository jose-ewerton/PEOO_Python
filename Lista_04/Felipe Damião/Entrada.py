'''Por aqui, ela recebe números(argumentos) que resultará em uma soma.'''
def soma(*variavel):
    total = sum(variavel)
    print ("A soma é",total)

'''Ao recebe um valor real, retornará com um aumento de 50%.'''
def acrescimo(variavel):
    print ("O valor mais o aumento é",variavel*1.5)
    
'''Desta vez, ela vai ganhar uma sequência de String e retornará a concatenação.'''
def concatenacao(*variavel):
    print("Depois da concatenação: ",end="")
    for lista in variavel:
        print(lista,end="")
    print("")

'''Por último, ganhará uma sequência com parametros nomeados e retornará tanto a chave, como o valor do último elemento.'''
def funcao(**variavel):
    conjunto = len(variavel)
    total = 1

    for lista in variavel.keys():
        if total == conjunto:
            print("O ultimo elemento enviado foi",lista,end=": ")
            total = 1
        else:
            total += 1
    
    for lista in variavel.values():
        if total == conjunto:
            print(lista)
        else:
            total += 1