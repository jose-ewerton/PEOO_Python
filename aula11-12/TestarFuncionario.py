from funcionario import Funcionario

novoFuncionario = Funcionario()#crie uma instancia da classe = objeto
novoFuncionario.nome = 'Luiz' #aqui eu estou criando um novo atributo e não acessando os da classe!

novoFuncionario.cpf = '1234567890' # método setter
print(novoFuncionario.nome,novoFuncionario.cpf) # método getter

print(novoFuncionario.__dict__) #lista no formato de dicionario o que tenho no objeto da classe


