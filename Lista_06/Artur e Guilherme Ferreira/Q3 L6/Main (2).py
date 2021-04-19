from pessoa import Pessoa
from endereco import Endereco

pessoa1 = Pessoa('Artur','00000','000111')
endereco1 = Endereco('555','rua x','cidade x','estado x','país x')
endereco2 = Endereco('556','rua y','cidade y','estado y','país y')

pessoa1.add_endereco(endereco1)
pessoa1.add_endereco(endereco2)

pessoa2 = Pessoa('Presidente','00001','000222')
endereco3 = Endereco('655','rua z','cidade z','estado z','país z')
endereco4 = Endereco('656','rua y','cidade w','estado w','país w')

pessoa2.add_endereco(endereco3)
pessoa2.add_endereco(endereco4)

pessoa1.listar_endereco()
pessoa2.listar_endereco()