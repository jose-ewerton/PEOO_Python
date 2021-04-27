def soma_total(*num):
    """Uma função que recebe uma sequência
    de argumentos variáveis e retorna a soma total."""
    soma = sum(num)  # soma os valores que estão em 'num'
    print(f"A soma dos valores digitados é: {soma}")


def acrescenta50(a):
    """Uma função que recebe um
    valor real e acrescenta 50%."""
    porc = a * 50 / 100  # faz a conta dos 50% de 'a'
    total = a + porc  # soma 'a' com os 50% de 'a'
    print(f"{a} + 50% do seu valor é {total}")  # mostra o valor com o acréscimo


def concatenar(*valores):
    """Uma função que recebe parâmetros
    String variáveis e retorna à concatenação."""
    r = ""
    for c in valores:
        r += c
    return r


def ultimo_valor_chave(**valor):
    """Uma função que recebe uma sequência variável de parâmetros
nomeados e retorna o último elemento enviado (chave e valor)."""
    lista = 0
    for c, v in valor.items():
        lista = c, v
    return lista
