#função
def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print('{}:{} AM'.format(h, m))
    elif 12 < h < 24 and 0 < m < 60:
        print("{}:{} PM".format(h-12, m))
    else:
        print('Valor inválido')


#código principal
while True:
    h = int(input("Hora:"))
    if h == 777:
        break
    m = int(input("Minutos:"))
    converta(h, m)
    print("digite 777 pra parar")