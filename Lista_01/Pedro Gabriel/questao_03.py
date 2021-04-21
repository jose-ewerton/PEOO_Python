"""Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
a um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
a. A média das idades das pessoas que responderam ótimo;
b. A quantidade de pessoas que responderam regular;
c. A porcentagem de pessoas que responderam bom entre todos os espectadores
analisados."""


ida = [] #Idade.
nota = []
i = 0

while i < 15:
    print("Para classicar sua opiniao sobre esse filme use 3 para otimo, 2 para bom e 1 para regular.")
    ida.append(int(input("Escreva sua idade: ")))
    nota.append(int(input("Digite sua opinião: ")))
    i += 1

total = sum(ida)

print("A media das idades dos participantes foi de: ", total / len(ida))

n = [] #Número.
p = [] #Porcetagem.
for cont in nota:
    if ((cont % 2 != 0) and (cont == 1)):
        n.append(cont)
    if (cont % 2 == 0):
        p.append(cont)

print(list(ida))
print(list(nota))

P = (len(p) / 15) * 100
print("O numero de pessoas que responderam regular foi", len(n))
print(round(P), "% que votaram bom.")
