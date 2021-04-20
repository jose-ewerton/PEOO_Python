def int(x):
    return len((str(x)))

x = str(input('Digite um número: ')).strip()
print(f'Esse numero tem {int(x)} digito(s)')
