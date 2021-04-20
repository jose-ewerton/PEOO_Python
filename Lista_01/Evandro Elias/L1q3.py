print("=================================================================================================================")
print("Vote como 1 = regular, 2 = bom, 3 = otimo")
opnion = []
idade = []
x = 0
while x <= 15:
  
  idade.append(int(input("qual a sua idade?")))
  opnion.append(int(input("Qual a sua opinião sobre o filme?:")))
  x += 1


m = sum(idade) / len(idade)
print(f"A média das idades das pessoas que responderam ótimo:{m}")
vr = opnion.count(1)
print(f"A quantidade de pessoas que responderam regular:{vr}")
pb = (opnion.count(2) / len(opnion)) * 100
print(f"{pb}% a porcentagem de pessoas que responderam bom entre todos os espectadores analisados.")
