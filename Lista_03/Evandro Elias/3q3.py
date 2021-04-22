def converter(H, M):
    if 0 < H <= 12 and 0 < M < 60:
        print(f'{H}:{M} AM')
    elif 12 < H < 24 and 0 < M < 60:
        print(f'{H - 12}:{M} PM')
    else:
        print('Valor inválido')


while True:
    H = int(input('Hora: '))
    if H == 999: break
    M = int(input('Minuto: '))
    converter(H,M)
    print("-------------") 
