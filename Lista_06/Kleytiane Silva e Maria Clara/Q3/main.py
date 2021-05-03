from pessoa import Pessoa

from endereço import Endereco


pessoa1  =  Pessoa ( 'Alexa' , '002 784-20' , '000111' )
endereco1  =  Endereco ( '750' , 'rua do amor' , 'Gramado' , 'Rio Grande do Sul' , 'Brasil' )
endereco2 = Endereco('111','Diana Kreiter','Cuiabá','MT','Brasil')

pessoa1.adc_endereco(endereco1)
pessoa1.adc_endereco(endereco2)


pessoa1.listar()