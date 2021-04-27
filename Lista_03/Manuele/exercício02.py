
cont = 0
n = int(input("Digite um número inteiro (quanto dígitos preferir):"))
while ( n > 1 ):
    n = n / 10
    cont = cont + 1

print("A quantidade de caracteres inserido foi:",cont)