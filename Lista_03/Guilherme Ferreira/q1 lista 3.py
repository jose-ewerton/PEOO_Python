<<<<<<< HEAD
def numero(*N):
    N = []
    while 0<1:
        N.append(float(input("digite um numero: ")))
        print(sum(N))

numero(1,2,2,3,4,5)
=======
def numero(*args):
    N = []
    N += args
    cont = 0
    while cont < 1:
        
        N.append(float(input("digite um numero: ")))
        continuar = str(input("continuar? S/N: "))
        if continuar == "S":
            cont = 0
        else:
            cont = 1
            
    print(sum(N))
numero(0)
>>>>>>> 692e22ea2340ba349368fae9b74aaf070c93cf4a
