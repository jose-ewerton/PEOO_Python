print("="* 50)
print("                    DESAFIO 2" )
print("="* 50)
z = 0
n = list()
nome = (input("Qual é o nome do atleta? "))

for c in range(1,6):
    n.append(int(input("Digite a distância alcançada no {}º salto:  ".format(c))))
    z+1

med_saltos = sum(n)/len(n)
print('='*50)
print("Atleta: ", nome,"\n" "saltos: ", n,"\n" "Média dos saltos: ", med_saltos )
