

#recebe uma sequência de argumentos variáveis e retorna a soma total
def soma (*args): 
    res = 0
    for c in args:
        res += c
    return res    
#Uma função que recebe um valor real e acrescente 50%
def acrescimo ( valor):
    valor = valor + (valor/2)
    return valor

#Uma função que recebe parâmetros String variáveis e retorna à concatenação.
def concatenar (*args):
    palavra_concatenada = " "
    for c in args :
        palavra_concatenada += c 
    return palavra_concatenada  

#Uma função que recebe uma sequência variável de parâmetros nomeados e retorna o
 #último elemento enviado (chave e valor).

def quero_meu_diplomaaaa (**kwargs):
    for c , v in kwargs.items():
        chave = c
        valor = v
    ultimo = {chave: valor}
    return ultimo

