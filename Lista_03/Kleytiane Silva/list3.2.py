def interios(n):
  return len((str(n)))

n = str(input("Digite um número:")).strip()
print(f'Esse número tem {interios(n)} dígitos.')