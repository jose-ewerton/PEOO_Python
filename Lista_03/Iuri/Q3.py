def converta(hora, minu):
    if 0 < hora <= 12 and 0 < minu < 60:
        print(f'{hora}:{minu} AM')
    elif 12 < hora < 24 and 0 < minu < 60:
        print(f'{hora - 12}:{minu} PM')
    else:
        print('Valor inválido')


while True:
    hora = int(input('Hora: '))
    minu = int(input('Minuto: '))
    converta(hora,minu)
    print('='*12)
    n = (input("Deseja continuar com a conversão? "))
    if n != "sim": break

