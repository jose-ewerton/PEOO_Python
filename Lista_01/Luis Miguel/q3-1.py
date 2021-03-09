op = []
idade = []
p = 0
while p < 15:
  """
  forneca a opinião das pessoas como 1 = ruim, 2 = regular, 3 = bom
  """
  idade.append(int(input("qual a idade da pessoa?:")))
  op.append(int(input("qual o nivel de opniao?:")))
  p += 1

media = sum(idade) / len(idade)
print(f"a media da idade do grupo eh: {media} anos")
qreg = op.count(2) #count(op)
print(f"{qreg} pessoas votaram regular")
pbom = (op.count(2) / len(op)) * 100
print(f"{pbom}% das pessoas votaram bom")