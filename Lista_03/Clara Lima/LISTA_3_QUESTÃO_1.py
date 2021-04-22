
print('='*50)
print("             LISTA 3 QUESTÃO 1")
print('='*50)
print("\n")

def soma(*num):
  n = []
  n += num
  q = len(n)

  print("A soma dos números informados são:", sum(n))
  print("A quantidade de números informados são: ", q)

soma(2,2,2)