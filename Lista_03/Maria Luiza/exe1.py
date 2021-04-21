"""Faça um programa, cum uma função que necessite de um número variável de argumentos não
nomeados e forneça a soma e quantidade de argumentos informados."""

numeros = []
s = []

def soma_contador(a):
    tam = len(numeros)
    soma = sum(s)
    print('\033[1m'f"Você digitou {tam} números e soma deles é {soma}!"'\033[m')


while True:
    a = int(input("Digite um Número:"))
    print('\033[30m'"Quando quiser digite '999' para encerrar!"'\033[m')
    numeros.append(a)
    s.append(a)

    if a == 999:
        numeros.pop()
        s.pop()
        print(soma_contador(a))
        break