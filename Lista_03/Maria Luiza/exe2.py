"""Faça uma função que informe a quantidade de dígitos
 de um determinado número inteiro informado."""


def contador_inteiros(n):
    return len((str(n)))


n = str(input('Digite um número: ')).strip()
print(f'Esse número tem {contador_inteiros(n)} dígitos!')