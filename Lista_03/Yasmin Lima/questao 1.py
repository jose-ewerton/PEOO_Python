n = []

s = []

 

def somaequantidade(a):

    quantidade = len(n)

    soma = sum(s)

    print("Quantidade dos números: {}".format(quantidade))

    print("Somando os números:".format(soma))

 

while True:

    a = int(input("digite algum número:"))

    print("digite 'bolodechocolate' pra parar")

    n.append(a)

    s.append(a)

 

    if a == bolodechocolate:

        n.pop()

        s.pop()

        print(somaequantidade(a))

        break
