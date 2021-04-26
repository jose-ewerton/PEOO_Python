#Faça um programa, cum uma função que necessite de um número variável de argumentos não
#nomeados e forneça a soma e quantidade de argumentos informados.

def soma(*ls):
  s = 0
  for n in ls:
    s = s + n
  print("A soma dos {} é {}".format(ls,s))

soma(1, 1, 1)
soma(12, 46, 49, 9)



