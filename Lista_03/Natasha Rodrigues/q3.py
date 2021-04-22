def cvrt(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f"{h}:{m} AM")
    elif 12 < h < 24 and 0 < m < 60:
        print(f"{h - 12}:{m} PM")
    else:
        print('Inválido')


while True:
    h = int(input('Informe a hora: '))
    if h == 999: break
    m = int(input('Informe o minuto: '))
    cvrt(h,m)
    print('-'*12)