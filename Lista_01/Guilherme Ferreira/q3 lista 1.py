nota = []
idade = []
c = 0
while c <= 15:
  """
  forneca a opinião das pessoas como 1 = ruim, 2 = regular, 3 = bom
  """
  idade.append(int(input("qual a idade da pessoa?:")))
  nota.append(int(input("qual o nivel de opniao?:")))
  c += 1


media = sum(idade) / len(idade)
print(f"a media da idade do grupo eh: {media} anos")
qreg = nota.count(1)
print(f"{qreg} pessoas votaram regular")
pbom = (nota.count(2) / len(nota)) * 100
print(f"{pbom}% das pessoas votaram bom")
