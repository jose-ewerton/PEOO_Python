from lista6q3_pessoa import Pessoa
from lista6q3_endereco import Endereco

a = int(input('serão 1 ou 2 pessoas? '))
if a > 2:
    print(f'como o máximo é 2, irei entender {a} como 2')
    a = 2
print('===============================')
print('Primeira pessoa:')

nome = input('Qual o seu nome?')
cpf = input("Qual seu cpf?")
rg = input('Qual seu RG?')
end = int(input('Você tem 1 ou 2 endereços?'))
if end > 2:
    print(f'como o máximo é 2, então irei entender {end} como "2"')
    end = 2
rua = input('Qual o nome da sua rua?')
ndr = input('Qual o número da sua residência?')
cdd = input('Qual o nome da sua cidade?')
estd = input('Qual estado você vive?')
pais = input('Qual país você mora?')


pessoa1 = Pessoa(f'{nome}' , f'{cpf}' , f'{rg}')
endereco1 = Endereco(f'{ndr}', f'{rua}', f'{cdd}', f'{estd}', f'{pais}')

if end == 2:
    print('===== 2º endereço =====')
    rua2 = input('Qual o nome da rua do seu 2º endereço?')
    ndr2 = input('Qual o número da sua 2º residência?')
    cdd2 = input('Qual o nome da sua 2º cidade?')
    estd2 = input('Qual o seu segundo estado onde vive?')
    pais2 = input('Qual o segundo país onde vive?')
    endereco2 = Endereco(f'{ndr2}', f'{rua2}', f'{cdd2}', f'{estd2}', f'{pais2}')
    pessoa1.add_endereco(endereco2)

pessoa1.add_endereco(endereco1)

if a == 2:
    print('=======================================')
    print('Agora vamos para a segunda pessoa:')


    nome2p = input('Qual o seu nome?')
    cpf2p = input("Qual seu cpf?")
    rg2p = input('Qual seu RG?')
    end2p = int(input('Você tem 1 ou 2 endereços?'))
    if end2p > 2:
        print(f'como o máximo é 2, então irei entender {end2p} como "2"')
        end = 2
    rua2p = input('Qual o nome da sua rua?')
    ndr2p = input('Qual o número da sua residência?')
    cdd2p = input('Qual o nome da sua cidade?')
    estd2p = input('Qual o nome do seu estado?')
    pais2p = input('Qual país você mora?')


    pessoa2 = Pessoa(f'{nome2p}', f'{cpf2p}', f'{rg2p}')
    endereco3 = Endereco(f'{ndr2p}', f'{rua2p}', f'{cdd2p}', f'{estd2p}', f'{pais2p}')
    if end2p == '2':
        rua2p2 = input('Qual o nome da rua do seu 2º endereço?')
        ndr2p2 = input('Qual o número da sua 2º residência?')
        cdd2p2 = input('Qual o nome da sua 2º cidade?')
        estd2p2 = input('Qual o seu segundo estado onde vive?')
        pais2p2 = input('Qual o segundo país onde vive?')
        endereco4 = Endereco(f'{ndr2p2}', f'{rua2p2}', f'{cdd2p2}', f'{estd2p2}', f'{pais2p2}')
        pessoa2.add_endereco(endereco4)

    pessoa2.add_endereco(endereco3)

    pessoa2.listar_endereco()

pessoa1.listar_endereco()
