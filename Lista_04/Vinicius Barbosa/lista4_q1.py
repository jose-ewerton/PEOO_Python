'''Construa um módulo com as seguintes funções:
a. Uma função que recebe uma sequência de argumentos variáveis e retorna a soma total.
b. Uma função que recebe um valor real e acrescenta 50%.
c. Uma função que recebe parâmetros String variáveis e retorna à concatenação.
d. Uma função que recebe uma sequência variável de parâmetros nomeados e retorna o
último elemento enviado (chave e valor).'''



def som(*a):
    #Essa função recebe argumentos de variáveis e soma eles
    b = sum(a)
    print("O resultado de sua soma é de", b)

def porc(x):
    #A funcao recebe uma sequencia de argumentos variaveis e retorna a soma destes.
    print(x+(0.5* x))

def con(*y):
    #Já essa retorna a concatenação dos parâmetros String e variáveis.
    x = ''
    for z in y:
        x += z
    return x
print(con())

def seq(**y):
    #Por fim essa retorna os ultimos elementos.
    for x, z in y.items():
        print("{} é um(a) {}".format(x, z))