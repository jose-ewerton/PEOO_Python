'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
não for informado o nome do atleta.
'''

classificação = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
contagem = 0
media_saltos = 0
total_saltos = 0
media = 0
atleta = ' '

while atleta != '':
    atleta = input("Informe o nome do atleta: ")
    if atleta == '':
        break
    for c in range(1, 6):
        salto = float(input("Informe a distãncia do salto:"))

contagem = contagem + 1
media_saltos = media_saltos + 1
total_saltos = total_saltos + salto
media = total_saltos / media_saltos

print("=-"*30)
print("Atleta: {}".format(atleta))
print(f"Media dos demais saltos: {media:.2f}")
print("Resultado final: ")
print(f"{atleta}: {media:.2f}"
