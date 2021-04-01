# Crie um programa que faça 5 perguntas.

# O programa deve emitir uma Classificação  dessa pessoa no crime 

# Se a pessoa responder positivamenta  duas questões "Suspeita" 

# Entre 3 e 4 como "Cúmplice"

# E 5 como "Assassino" 

# Caso contrario ela será clasivicada como "Inocente"

perg = [ ]
perg.append(input("Telefonou para a vítima? Responda '1' para sim e '0' para Não:"))
perg.append(input("Esteve no local do crime? Responda '1' para sim e '0' para Não:" ))
perg.append(input("Mora perto da vítima? Responda '1' para sim e '0' para Não:"))
perg.append(input("Devia para a vítima? Responda '1' para sim e '0' para Não:"))
perg.append(input("Já trabalhou com a vítima? Responda '1' para sim e '0' para Não:"))

soma = 0
for n in perg:
    soma += int( n )
if soma < 2:
    print("Inocente")
elif soma== 2:
    print("Suspeita")
elif soma <= 4 :
    print("Cúmplice")
if soma== 5:
    print("Assassino")

