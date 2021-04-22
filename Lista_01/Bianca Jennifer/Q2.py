imp=[]
pr=[]
va=0
for c in range(10):
    b=int(input("digite um número: "))
    for g in range(1,b+1):
        if b%g==0:
            va=va+1
    if va<=2 and va!=1:
        pr.append(b)                    
    if b%2!=0:
        imp.append(b)
    va=0    
print("Soma dos valores primos: ",sum(pr))
print("Soma dos valores impares: ",sum(imp))        
       
