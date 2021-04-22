print('\n')
print('='*50)
print('               LISTA 3 QUESTÃO 3')
print('='*50)
def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} AM')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} PM')
    else:
        print('Valor inválido')


while True:
    h = int(input('Digite as horas: '))
    m = int(input('Digite os minutos: '))
    converta(h,m)
    print('='*50)
    n = (input("Deseja continuar com a conversão? "))
    if n != "sim": break

print("Fim do programa!")

