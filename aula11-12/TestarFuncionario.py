from funcionario import Funcionario

novoFuncionario = Funcionario()
print(novoFuncionario.horas_trabalhadas)
novoFuncionario.nome = "Ewerton"
novoFuncionario.cpf = "12345678910"
novoFuncionario.valor_por_hora = -25.50
print(novoFuncionario.nome, novoFuncionario.cpf, novoFuncionario.valor_por_hora)
