print("===========================================================")
N = []
IM = []
P = []
i = 0

while i < 10:
    num = (int(input("INFORME UM NUMERO: ")))
    N.append(num)
    if num%2 > 0:
        IM.append(num)
    i += 1

O = 0
s = 0
t = 0
for i in range(10):
    for c in range(1, N[O]+1):
        if N[O] % c == 0:
            t += 1
        if t == 2:
            s += nums[O]
        O += 1
        t = 0
print(s)
print(N)
print(IM)
print(P)
