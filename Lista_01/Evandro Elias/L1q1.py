print(" forneça o sexo das pessoas M = masculino e F = feminino")
F= []
M =[]
AM = []
AF = []
PM = []
PF = []
p = 0

while p < 15:
  
  i = str(input("Informe o sexo: "))
  if i == 'M':
    M.append(i)
    AM.append(float(input("lnforme a altura: ")))
    PM.append(int(input("Informe o peso: ")))
    a = []
    for altura in AM:
        if altura >=1.70:
          a.append(altura)    
        
    p += 1

  elif i == 'F':
    F.append(i)
    AF.append(float(input("informe a altura:")))
    PF.append(int(input("informe o peso:")))
   
    p += 1


x = sum(AM) + sum(AF)
y = len(AM) + len(AF)
mest= x / y
print(f"altura media do grupo: {mest}m")
maior = max(AF)
menor = min(AM)
print(f"a mulher mais alta{maior}m homem mais baixo {menor}m")
print(f" {len(a)} homens maiores q 1.70m")
po= (len(M) / 15) * 100
pr = (len(F) / 15) * 100
print(f"{po}% de homens e {pr}% de mulheres")
