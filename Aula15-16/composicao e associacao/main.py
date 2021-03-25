from classes import Funcionario, Departamento, Empresa

func = Funcionario("João")
func2 = Funcionario("Ana")
func3 = Funcionario("Paulo")
dep = Departamento("Logística",1) #como pegar esse departamento e inserir na empresa!!?


#Agregação
print("------------------AGREGAÇÃO---------------------------")
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
#emp.inserir_departamento(dep) #fiz uma composição! Errado fiz uma agregação, na composição o objeto deve ser criado dentro da classe em um método, caso contrário é agregação e são objetos independentes,posso até destruir os dois ao mesmo tempo mais a nível de programação não seria composição;


#forma correta
print("------------------COMPOSIÇÃO---------------------------")
emp = Empresa("TecnoVida","00.000.000/0001")
emp.inserir_departamento("TI","001")
dep2 = emp.acessar_departamentos("001")
#print(dep2.nome_departamento)
dep2.inserir_funcionario(func)
dep2.inserir_funcionario(func2)
dep2.inserir_funcionario(func3)
dep2.listar_funcionarios_no_dep()

emp.listar_departamentos()
emp.total_func_empresa()

print("--------------------INSERINDO MAIS UM DEPARTAMENTO E FUNCIONARIOS-------------------------")
emp.inserir_departamento("Administração","002")
dep2 = emp.acessar_departamentos("002")
print(dep2.nome_departamento)
dep2.inserir_funcionario(func)
dep2.inserir_funcionario(func2)
dep2.inserir_funcionario(func3)
dep2.listar_funcionarios_no_dep()

emp.listar_departamentos()
emp.total_func_empresa()




print("--------------------INSERINDO MAIS UM DEPARTAMENTO E FUNCIONARIOS-------------------------")
emp.inserir_departamento("RH","003")
dep2 = emp.acessar_departamentos("003")
print(dep2.nome_departamento)
dep2.inserir_funcionario(func)
dep2.inserir_funcionario(func2)
dep2.inserir_funcionario(func3)
dep2.listar_funcionarios_no_dep()

emp.listar_departamentos()
emp.total_func_empresa()





