"""
bem vindo, forneca os dados de 15 pessoas
"""
ome = []#sexo maxo
cuie =[]#sexo femea
estm = []# altura dos maxo
estf = []#altura das femeas
pm = []#peso dos maxo
pf = []#peso das femeas
p = 0

while p < 15:
  """
  forneca o sexo da pessoa como M = masculino e F = feminino
  a altura como float, ex: 1.87, 1.65
  o peso como int, ex: 78, 90
  """
  gen = str(input("qual o sexo?:"))
  if gen == 'M':
    ome.append(gen)
    estm.append(float(input("qual a altura?")))
    pm.append(int(input("qual o peso?:?")))
    alt = []#lista usada pra encontrar a questao c
    for alturas in estm:
        if alturas >=1.70:
          alt.append(alturas)    
        
    p += 1

  elif gen == 'F':
    cuie.append(gen)
    estf.append(float(input("qual a altura?")))
    pf.append(int(input("qual o peso?:?")))
   
    p += 1


estt = sum(estm) + sum(estf)#estatura total
nest = len(estm) + len(estf)#quantidade de estaturas 
mest= estt / nest#media da estatura
print(f"a altura media do grupo eh {mest}m")
maior = max(estf)#maior estatura feminina
menor = min(estm)#menor estatura masculina
print(f"a mulher mais alta possui {maior}m e o menor homem possui {menor}m")
print(f"existem {len(alt)} homens maiores q 1.70m")
pome= (len(ome) / 15) * 100#porcentagem de maxo
pcuie = (len(cuie) / 15) * 100#porcentagem de cuie
print(f"no total ha {pome}% de homens e {pcuie}% de mulheres")