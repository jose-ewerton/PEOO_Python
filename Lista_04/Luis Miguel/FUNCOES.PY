"""
funcao para soma, args recebe varios argumentos como parametros, crio x para q eu possa retornar o resultado
"""
def soma(*args):
    print("valores para a soma")
    x = 0
    for entradas in args:
    	x +=  entradas
    return x
   
   

"""
funcao para acrescimo, bastante simples com apenas 1 parametro, multiplicado por 1.50
"""
def acrescimo(a):
    a = float(input("digite um numero: "))
    a = a * 1.50
    return a
    


"""
funcao para concatenar, os parametros devem ser dados em str, x eh uma string vazia que vai ser usada para concatenar as str
"""
def conca(*strings):
		print(" strings aka 'texto' para serem concatenados")
		x = ""
		for str in strings:
			x += " " + str
		return x
		


"""
retorna o ultimo item de um dicionario,  o ** permite q os parametros sejam retornados em dict
"""
def dicionario(**dict):
    print("dicionarios aka 'chave = 'valor'' ")
    for chave, valor in dict.items():
        print("{} é {}".format(chave, valor))
