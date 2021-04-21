"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer umprograma que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta."""

saltos = []

atleta = str(input("Nome do atleta:"))
for d in range(1, 6):
    salto = float(input(f"{d}º Salto:"))
    saltos.append(salto)

print('-'*15)
print('\033[1m'f"Atleta: {atleta}")
print('\033[1m'f"1º salto: {saltos[0]}")
print('\033[1m'f"2º salto: {saltos[1]}")
print('\033[1m'f"3º salto: {saltos[2]}")
print('\033[1m'f"4º salto: {saltos[3]}")
print('\033[1m'f"5º salto: {saltos[4]}"'\033[m')
print('-'*15)

media = sum(saltos)/5

print('\033[7m'f"Resultado:"'\033[m')
print('\033[7m'f"Atleta: {atleta}"'\033[m')
print('\033[7m'f"Saltos: {saltos}"'\033[m')
print('\033[7m'f"Média: {media}"'\033[m')