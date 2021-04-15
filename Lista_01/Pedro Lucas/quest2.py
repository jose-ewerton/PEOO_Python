num = []
imp = []
a = 0
b = 0
mult = 0
i = 0

while i < 10:
    num.append (int (input ("Digite um valor: ")))
    i += 1

    for cont in num:
        if cont % 2 != 0:
            imp.append (cont)

for a in range (10):
    for b in range (1, num[a] + 1):
        if num[a] % b == 0:
            mult += 1
    if mult == 2:
        b += num[a]
    a += 1
    mult = 0

Impares = sum (set (imp))

print ("A soma dos números impares são de", Impares)

print ("A soma dos números primos são de", b)