def func(*args):
    x = []
    x += args #solução cabulosa!!!
    qnt = len(x)
    print("A soma: {}\nA quantidade de argumentos informados: {}".format(sum(x), qnt))
    
'''
    qnt = len(args)
    print("A soma: {}\nA quantidade de argumentos informados: {}".format(sum(args), qnt))
'''

func(1, 2, 3, 3.5)