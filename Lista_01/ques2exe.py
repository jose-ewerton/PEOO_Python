prinum = []
impnum = []
x = []
rnum = []
cont = 0
cont2 = 0
cont3 = 0
while cont < 10:
    num = int(input("Digite um número: "))
    if num%2 == 1:
        impnum.append(num)

    cont += 1
valor = len(impnum)
while cont3 < valor:
    if impnum[cont2] % 2 > 0:
        prinum.append(impnum)
        cont2 += 1
    cont3 += 1
print("")
print("NÚMEROS ÍMPARES: ", impnum)
somaimp = sum(impnum)
print("SOMA DOS NÚMEROS ÍMPARES: ", somaimp)
print("")

print(prinum)
#print("NÚMEROS PRIMOS: ", prinum)
#somapri = sum(prinum)
p#rint("SOMA DOS NÚMEROS PRIMOS: ", somapri)


#print("Os números primos são: % " %prinum)


