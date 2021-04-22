'''
sum irá somar todos os valores dados
'''
def soma(*algo):
    resultado = sum(algo)
    print (f'O somatorio dos números informados é {resultado}')

'''
Aqui é apenas pegar o valor é multiplacar por 1.5
'''
def acres(algo):
    print (f'Somando o aumento com o valor será: {algo*1.5}')

'''
Os valores são dados em str, colocando esses valores em uma variavel para concatenar 
'''
def concatenacao(*algo):
    algo1 = ''
    for str in algo:
        algo1 += str
    return algo1

'''
os ** permitem que possa usar os valores em algo.items
'''
def func(**algo):
    for nome, sobrenome in algo.items():
        print(f'{nome} {sobrenome}')

