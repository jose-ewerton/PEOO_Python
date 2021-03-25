''' Uma classe empresa que é composta por departamentos e agrega funcionarios da classe funcionario '''

class Empresa:
    def __init__(self,nome,cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.departamentos = []
        self.total_funcionarios = 0

    def inserir_departamento(self,nome,sala):
        self.departamentos.append(Departamento(nome,sala))
    
    def listar_departamentos(self):
        for departamento in self.departamentos:
            print(f"Nome: {departamento.nome_departamento}, Sala: {departamento.sala}, Total de funcionários: {departamento.numero_funcionarios}")

    def acessar_departamentos(self,sala):
        for departamento in self.departamentos:
            if departamento.sala == sala:
                return departamento
            
            
    def total_func_empresa(self):
        for departamento in self.departamentos:
            self.total_funcionarios += departamento.total_func()
        print(f'Total de funcionários da empresa: {self.total_funcionarios}')



class Departamento:
    def __init__(self, nome, sala):
        self.nome_departamento = nome
        self.sala = sala
        self.numero_funcionarios = 0
        self.funcionarios = []
    
    def inserir_funcionario(self,funcionario):
        self.funcionarios.append(funcionario)
        self.numero_funcionarios += 1

    def listar_funcionarios_no_dep(self):
        print(f'Total de funcionários: {self.numero_funcionarios}')
        for funcionario in self.funcionarios:
            print(funcionario.nome)
    
    def total_func(self):
        return self.numero_funcionarios

            

class Funcionario:
    def __init__(self,nome):
        self.nome = nome