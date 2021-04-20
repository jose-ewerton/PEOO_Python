#Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
# um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
# A média das idades das pessoas que responderam ótimo;
# A quantidade de pessoas que responderam regular;
# A porcentagem de pessoas que responderam bom entre todos os espectadores analisados

lnotas = []
lidades = []

for c in range (0, 15):
  lidades.append(int(input("Qual é a sua idade:")))
  lnotas.append(int(input("Qual é a sua opinião (3=ótimo, 2=bom, 1=regular)?:")))

m= sum(lidades) / len(lidades)
reg = lnotas.count(1)
bom= (lnotas.count(2) / len(lnotas)) * 100

print("A média de idades é de:",m,"Pessoas.")
print("A quantidade de pessoas que responderam regular foram de:",reg,"pessoas.")
print("A porcentagem de pessoas dentre todas que responderam bom foi de:",bom,"%")