#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
#do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
#programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
#depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
#não for informado o nome do atleta.

soma_dos_saltos = 0 
saltos=[]
sequencia = ['primeiro','segundo','terceito','quarto','quinto']
while True:
    atleta = input("Informe o nome do atleta: ")
    if atleta == '':
        break
    else: 
        for c in range(0,5):
            saltos.append(float(input("{} salto:".format(sequencia[c]))))

media = sum(saltos)/len(saltos)

print("         Resultado        ")
print("atleta: ", atleta)
print(" Saltos: ", saltos)
print(" Media: ", media)
