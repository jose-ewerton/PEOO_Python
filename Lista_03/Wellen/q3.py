def converter(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print('{}:{} AM'.format(h, m))
    elif 12 < h < 24 and 0 < m < 60:
        print('{}:{} PM'.format(h - 12, m))
    else:
        print('inválido')

print("Conversão de horas (de 24h para 12h)")
h = int(input("Digite a hora:"))
m = int(input("Digite os minutos:"))
converter(h, m)