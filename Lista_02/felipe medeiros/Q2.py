'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado 
do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um 
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:'''

Nome= str(input("atleta: "))
N = len(Nome)
if N > 1:
	pulo1 = float(input(" salto: "))
	pulo2 = float(input("salto: "))
	pulo3 = float(input("salto: "))
	pulo4 = float(input("salto: "))
	pulo5 = float(input("salto: "))
	media = (pulo1 + pulo2 + pulo3 + pulo4 + pulo5)/5 

print("Resultado:")
print("Nome do atleta:", Nome)
print("Saltos:", pulo1, "-", pulo2, "-", pulo3, "-", pulo4, "-", pulo5)
print("Media dos saltos: ",round(media,2), "m")