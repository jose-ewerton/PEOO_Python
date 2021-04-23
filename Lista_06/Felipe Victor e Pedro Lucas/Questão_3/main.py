from pessoa import Pessoa
from endereço import Endereco

pessoa1 = Pessoa('Luís','002469','000111')
endereco1 = Endereco('666','rua x','Tártaro','Submundo','Grecia')
endereco2 = Endereco('69','Joaquim Marques','Cubatão','RS','Brasil')

pessoa1.adc_endereco(endereco1)
pessoa1.adc_endereco(endereco2)

pessoa1.listar()
