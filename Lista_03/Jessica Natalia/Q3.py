def conv(h):
    a = h-12
    return a

def sai():
    while True:
        x = int(input("insira a hora: "))
        m = input("insira os minutos: ")
        if x<12:
            print("{}:{} AM".format(x,m)) 
        else:
            print("{}:{} PM".format(conv(x),m)) 


sai()