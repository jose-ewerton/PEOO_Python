def soma(*ls):
  s = 0
  for n in ls:
    s += n
  print(f"A soma dos {ls} temos {s}")


soma(1, 1, 1)
soma(69, 34, 24, 4)
