#Faça um programa, cum uma função que necessite de um número variável de argumentos não
#nomeados e forneça a soma e quantidade de argumentos informados.

def arg (a):
    a = []
    i = 0
    while 0 == i:
        a.append (float (input ("Digite um argumento:")))
        print ("A quantidade de argumentos são", len (a))
        print ("A soma do valor dos argumentos são", sum (a))


arg(10)