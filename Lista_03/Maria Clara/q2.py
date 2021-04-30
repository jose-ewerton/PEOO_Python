def tamanho(z):
    a = str(z)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)


num = int(input("Digite um número: "))
print(f'Esse número tem:',tamanho(num), 'dígitos')