cont=0
t=input("telefonou para a vitima(SIM ou NAO)? ").upper()
while t!="SIM" and t!="NAO":
    t=input("telefonou para a vitima(SIM ou NAO): ").upper()
if t=="SIM":
    cont=cont+1
l=input("esteve no local do crime(SIM ou NAO)? ").upper()
while l!="SIM" and l!="NAO":
    l=input("esteve no local do crime(SIM ou NAO)? ").upper()
if l=="SIM":
    cont=cont+1
m=input("mora perto da vitima(SIM ou NAO)? ").upper()
while m!="SIM" and m!="NAO":
    m=input("mora perto da vitima(SIM ou NAO)? ").upper()
if m=="SIM":
    cont=cont+1
d=input("devia para a vitima(SIM ou NAO)? ").upper()
while d!="SIM" and d!="NAO":
    d=input("devia para a vitima(SIM ou NAO)? ").upper()
if d=="SIM":
    cont=cont+1
j=input("trabalhou alguma vez para a vitima(SIM ou NAO)? ").upper()
while j!="SIM" and j!="NAO":
    j=input("trabalhou alguma vez para a vitima(SIM ou NAO)? ").upper()
if j=="SIM":
    cont=cont+1
print("resultado: ")
if cont==2:
    print("suspeita")
elif cont==3 or cont==4:
    print("cumplice")
elif cont==5:
    print("assassino")
else:
    print("inocente")  
