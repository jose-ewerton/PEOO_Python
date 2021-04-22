def soma(*args):
    print("a soma dos argumentos é {}".format(sum(args)))
    print("foram fornecidos {} argumentos".format(len(args)))

soma(1,2,3)    