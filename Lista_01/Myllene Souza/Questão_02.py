# Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
#  a soma dos números primos.

s = 0
sp  = 0
cont = 0
for c in range (1,11):
    n = int(input("Digite um número: "))
    if not(n % 2 == 0):   
        s = n + s
    for c1 in range (1, n+1):
        if n % c1 == 0:
            cont = cont +1
    
    if cont == 2:
        sp = sp + n 
        
    cont = 0

print ("Soma dos números impares: ", s,"Soma dos números primos: ", sp)    

    