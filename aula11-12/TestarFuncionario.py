from funcionario import Funcionario

novoFuncionario = Funcionario()
novoFuncionario.nome = 'Luiz' #aqui eu estou criando um novo atributo e não acessando os da classe!

novoFuncionario.cpf = '1234567890'
print(novoFuncionario.nome,novoFuncionario.cpf)

print(novoFuncionario.__dict__) #lista no formato de dicionario o que tenho no objeto da classe



