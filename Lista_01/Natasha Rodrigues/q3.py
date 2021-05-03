'''
Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
a um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
a. A média das idades das pessoas que responderam ótimo;
b. A quantidade de pessoas que responderam regular;
c. A porcentagem de pessoas que responderam bom entre todos os espectadores
analisados.
'''
somidade = 0
medidade = 0
totregular = 0
porbom = 0
bom = 0 
for p in range(1, 5):
    print('----- {}° Pessoa -----'.format(p))
    idade = int(input('Informe sua idade:'))
    opiniao = str(input('Informe sua opinião em relação ao filme. Digite 3 para ótimo, 2 para bom e 1 para regular:')) 

    if opiniao in '3':
        somidade += idade
        medidade = somidade / 4
    if opiniao in '1':
        totregular += 1
    if opiniao in '2':
        bom += 1
    
porbom = bom*100 / 4
    
print('-'*12)
print('A média de idade dos espectadores que responderam "ótimo" é de {}'.format(medidade))
print('A quantidade de pessoas que respoderam "regular" foi {}'.format(totregular))
print('A porcentagem de pessoas que responderam "bom" entre todos os espectadores analisados foi de {}%'.format(porbom))