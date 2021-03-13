from conta import Conta #importando uma classe do arquivo conta;

c = Conta('112',"Aluno",12.23,1000) #instanciando um objeto da classe conta;
print(type(c)) #mostrando no terminal o type de conta;

c.deposita(100)
