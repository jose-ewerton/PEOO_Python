def contador_caracteres():
    q_caracteres = 0
    n = int (input ("Digite um número:"))
    while ( n > 1 ):
        n = n / 10
        q_caracteres = q_caracteres + 1
    print("A quantidade de caracteres inserido foi:",q_caracteres)

contador_caracteres()