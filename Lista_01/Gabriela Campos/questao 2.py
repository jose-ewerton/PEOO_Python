#receber 10 numeros
#calcular e exibir soma de numeros impares e numeros primos


i = list()
p = list()
si = 0 #soma dos impares
sp = 0 #soma dos primos

for num in range (1,11):
    n = int(input("informe um número: "))
    if n % num == 0:
        sp += n
        p.append(n)
    elif n % num != 0:
        si += n
        i.append(n)
print ("são números primos: ", p)
print ("são números impares: ", i)
print ("soma dos númmeros primos: ", sp)
print ("soma dos números ímpares: ", si)
