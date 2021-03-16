def func(*args):
    x = []
    x += args
    qnt = len(x)
    print("A soma: {}\nA quantidade de argumentos informados: {}".format(sum(x), qnt))


func(1, 2, 3)