# Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
# a um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
# a. A média das idades das pessoas que responderam ótimo;
# b. A quantidade de pessoas que responderam regular;
# c. A porcentagem de pessoas que responderam bom entre todos os espectadores analisados.

si = 0
med =0
cont =0
contr = 0
for c in range(0, 15):
    op = int(input("O que voçê achou do filme? Digite '3' para otimo, '2' para bom e '1' para regular' "))
    idade = int (input(" Qual a sua idade?"))

    if op == 3:
        si = si + idade
        cont = cont + 1
        med = si/cont
    elif op == 1:
        contr=  contr + 1

portcentualOR = ((contr+cont)*100)/15
portcentualB = 100 - portcentualOR
    
print ("A média das pessoas que responderam ótimo foi:",med)
print ("A quantidade de pessoas que responderam regular foi:",contr)
print("A porcentagem de pessoas que responderam bom foi:", portcentualB)