colocado = 'Primeiro','Segundo','Terceiro','Quarto','Quinto'
melhor_salto = pior_salto = contagem = media_saltos = total_saltos = media= 0
atleta = ' '
while atleta != '':
    atleta = input("Atleta: ")
    if atleta == '':
        break
    for c in range(0, 5):
        salto = float(input(f"{colocado[c]} salto: "))
        contagem += 1
        media_saltos += 1
        if salto > melhor_salto:
            melhor_salto = salto
        if salto < pior_salto or contagem == 1:
            pior_salto = salto
        total_saltos += salto
        media = total_saltos / media_saltos


print(f"Melhor salto: {melhor_salto}")
print(f"Pior salto: {pior_salto}")
print(f"Media dos demais saltos: {media:.2f}")
print("\n")
print("Resultado final: ")
print(f"{atleta}: {media:.2f}")