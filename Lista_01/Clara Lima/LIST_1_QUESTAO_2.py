print('\n')
print('='*50)
print("              LISTA 1 QUESTÃO 2"   )
print('='*50)

#Receber 10 numeros
#Calcular a soma dos numeros
#imprimir a soma dos numeros pares
#imprimir a soma dos numeros impares
primos = []
impares = []
a = 0

for i in range(1,11):
    num = int(input("Digite %iº número: "%i))
    if num % 2 == 0:
        primos.append(num)
    else:
        impares.append(num)
print("="*50)
print("O somatório dos números pares é: ", sum(primos))
print("O somatório dos números ímpares é: ", sum(impares))
    
	
