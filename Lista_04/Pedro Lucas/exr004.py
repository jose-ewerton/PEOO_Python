print("retorna o ultimo item")
def ultimo(**dict):


    for key, value in dict.items():
        print("{} é {}".format(key,value))


print(ultimo(nome = "Pedro", Sobrenome = "Lima"))
print(ultimo(nome = "Kirigaya", Lastname = "Kazuto"))

