#Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
#a soma dos números primos.



n = []
ni = []
ci = 0
for c in range(1, 11):
    nu = int(input("Digite um número: "))
    n.append(nu)
    if nu %2 != 0:
        ni.append(nu)
    ff= sum(ni)
    ci+= 1

np= 0
npp= 0
nppp= 0
for cc in range (1, 11):
    for ccc in range(1, n [np]+1):
        if n [np] % ccc ==0:
            npp+=1

    if npp == 2:
            nppp += n[np]

    np += 1
    npp = 0




print("A soma dos números que são primos é de: ",nppp)
print("A soma dos números que são ímpares é de: ", ff)





