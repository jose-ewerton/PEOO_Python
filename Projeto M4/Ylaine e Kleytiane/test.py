list1 = []
list = []
while True:
    n = input('Nome: ')
    i = int(input('Idade: '))
    if i >= 60:
        list1.append([n])
    if i <= 59:
        list.append([n])
    res = input('Quer continuar?[S/N]')
    if res in 'Nn':
        break
resp = input('Quer limpar as listas?[S/N]')
if resp in 'Ss':
 list.clear()
 list1.clear()
print('A lista de pacientes preferências foi',  list1)
print('A lista geral com ordem de chegada',  list)