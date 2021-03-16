def func(*args):
    x = []
    x += args #solução cabulosa!!!
    qnt = len(x)
    print("A soma: {}\nA quantidade de argumentos informados: {}".format(sum(x), qnt))
'''
    qnt = len(args)
    print("A soma: {}\nA quantidade de argumentos informados: {}".format(sum(args), qnt))
'''

<<<<<<< HEAD

func(1, 2, 3, 3.5)
=======
func(1, 2, 3)
>>>>>>> 692e22ea2340ba349368fae9b74aaf070c93cf4a
