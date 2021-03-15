nums = []
imp = []
i = 0
sumimp = 0
while i < 10:
    num = (int(input("digite um numero: ")))
    nums.append(num)
    if num % 2 != 0:
        imp.append(num)
    sumimp = sum(imp)
    i += 1
oe = 0
somap = 0
tat = 0
for i in range(10):
    for c in range(1, nums[oe]+1):
        if nums[oe] % c == 0:
            tat += 1
        
    if tat == 2:
        somap += nums[oe]
    oe += 1
    tat = 0
    
print("a soma dos primos é igual a: ",somap)
print("a soma dos impares é igual a: ",sumimp)

