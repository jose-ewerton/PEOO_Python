'''
Nessa parte ele irá somar todos os valores dados.
'''
def soma(*b):
    result = sum(b)
    print (f'O somatorio dos números informados é {result}')

'''
Usei esse valor e multipliquei por 1.5.
'''
def acres(b):
    print (f'Somando o aumento com o valor será: {b*1.5}')

'''
Os valores são recebido em str, colocamos esses valores em uma variavel para
concatenar.
"'''"'"

def concat(*b):
    b1 = ''
    for str in b:
        b1 += str
    return b1

'''
Criei uma função, que vai receber intens e,exibir na tela
'''
def func(**b):
    for nome, sobrenome in b.items():
        print(f'{nome} {sobrenome}')