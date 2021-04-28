#valor inicial
saltos = []

#código principal
atleta = str(input("Nome:"))
for p in range(1, 6):
    salto = float(input(f"{p}º salto:"))
    saltos.append(salto)

media = sum(saltos)/5

#saída2
print("Resultado:")
print("Atleta: {}".format(atleta))
print("Saltos: {}".format(saltos))
print("Média: {}".format(media))