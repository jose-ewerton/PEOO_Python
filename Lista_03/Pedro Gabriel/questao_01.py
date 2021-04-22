"""Faça um programa, cum uma função que necessite de um número variável de argumentos não
nomeados e forneça a soma e quantidade de argumentos informados."""


def Num(arg):
    arg = [] #Argumentos informados.
    R = input("Vai usar com letras ou numeros, responda usando L para letras e N para numeros: ")

    if R == "N":
        i = 0
        while 0 < 1:
            arg.append(float(input("Escreva um numero: ")))

            print("Numero de argumentos armazenados: ")
            print(len(arg))
            print("Soma total dos argumentos: ")
            print(sum(arg))

    elif R == "L":
        i = 0
        while 0 < 1:
            arg.append((input("Ecreva um caractere: ")))

            print("Numero de argumentos armazenados: ")
            print(len(arg))


Num(1)


