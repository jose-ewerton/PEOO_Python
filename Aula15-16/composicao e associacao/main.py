from classes import Funcionario, Departamento, Empresa

func = Funcionario("João")
func2 = Funcionario("Ana")
func3 = Funcionario("Paulo")
dep = Departamento("Logística",1) #como pegar esse departamento e inserir na empresa!!?
emp = Empresa("Empresa X","00.000.000/0001")

#Agregação

dep.inserir_funcionario(func)  #agregação do funcionario no departamento
dep.inserir_funcionario(func2)
dep.inserir_funcionario(func3)
dep.listar_funcionarios_no_dep()



''' del func deleta o objeto, variaveis etc.
print(dep.nome_departamento)
print(func.nome)
'''

#Composição


#Paramos por aqui, voltamos com mais detalhes de composição
emp.inserir_departamento(dep) #fiz uma composição!
emp.listar_departamentos()











