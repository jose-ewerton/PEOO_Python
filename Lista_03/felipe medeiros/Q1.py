'''Faça um programa, cum uma função que necessite de um número variável de argumentos não 

nomeados e forneça a soma e quantidade de argumentos informados.'''

def Num(a):
	a = []
	R = input("Vai usar com letras ou numeros, responda usando L para letras e N para Numeros: ")
	
	if R == "N":
		i = 0
		while 0 < 1:
			a.append(float(input("Digite um numero: ")))
			
			print("Numero de argumentos armazenados: ")
			print(len(a))
			print("Soma total dos argumentos")
			print(sum(a))
	
	elif R == "L":
		i = 0
		while 0 < 1:
			a.append((input("Digite um Caractere: ")))
			
			print("Numero de argumentos armazenados: ")
			print(len(a))

Num(1)	