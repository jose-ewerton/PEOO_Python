def hora_ampm(horas, minutos):
    if (horas == 0 or horas == 24):
        print(f'12:{minutos} PM')
    elif (horas > 12 and horas < 24):
        print(f'{horas-12}:{minutos} PM')
    elif (horas > 24):
        print("Horário invalido")
    else:
        print(f'{horas}:{minutos} AM')

while True:
    hora = int(input("Informe uma hora ou digite 0 para sair:"))
    minutos = int(input("Informe os minutos:"))
    if hora == 0:
     break
    elif minutos == 0:
     break
    hora_ampm(hora, minutos)