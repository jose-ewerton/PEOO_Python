#Faça um programa, com uma função que necessite de um número variável de argumentos não
#nomeados e forneça a soma e quantidade de argumentos informados.

def soma(*args): # definir a função soma com o números de argumentos
    result = 0
    cont = 0
    for elem in args:
        result += elem
        cont += 1
    return  result





print(soma(2,2,2))
