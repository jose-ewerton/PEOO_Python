"""Função que recebe uma sequência de argumentos variáveis e retorna a soma total."""


def soma(*argumentos):
    print("Valores para a soma: ")
    x = 0
    for entradas in argumentos:
        x += entradas
    return x


"""Função que recebe um valor real e acrescenta 50%."""


def acrescimo(a):
    a = float(input("Digite um número: "))
    a = a * 1.50
    return a


"""Função que recebe parâmetros String variáveis e retorna à concatenação."""


def concatenacao(*strings):
    print("strings aka 'texto' para serem concatenados")
    x = ""
    for str in strings:
        x += " " + str
    return x


"""função que recebe uma sequência variável de parâmetros nomeados e retorna o
último elemento enviado (chave e valor)."""


def dicionario(**dict):
    print("Dicionários aka 'chave = 'valor'' ")
    for chave, valor in dict.items():
        print("{} é {}".format(chave, valor))