print('\n')
print("="*30)
print('           LISTA 4')
print('='*30)
def soma(*n):  # A função soma, irá somar os valores digitado pelo usuário.
    x = sum(n)
    print("Soma dos elementos: ", x)

def acrescimo(n): # A função acrescimo, irá calcular o acréscimo de um determinado número digitado pelo usuário.
    porc = n*50/100+n
    print("Acrescimo de: {}%".format(porc))

def concatenacao(*n): # A função concatenacao, irá fazer concatenação de um determinado caractere digitado pelo usuário.
    print("Concatenação: ", end="")
    for c in n:
        print(c, end="")



