print("funcao para concatenar")
def conca(*strings):
    x = ''
    for str in strings:
        x += str
    return x


print(conca())