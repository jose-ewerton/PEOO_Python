print("="*50)
print("                                  DESAFIO 1 " )
print("="*50)

count = 0

resp = str(input("Telefonou para a vítima? "))
resp = resp.lower()
if resp == "sim" or resp == "s":
  count += 1

resp = str(input("Esteve no local do crime? "))
resp = resp.lower()
if resp == "sim" or resp == "s":
  count += 1

resp = str(input("Mora próxomo a vítima? "))
resp = resp.lower()
if resp == "sim" or resp == "s":
  count += 1

resp = str(input("Devia para a vítima? "))
resp = resp.lower()
if resp == "sim" or resp == "s":
  count += 1
resp = str(input("Já trabalhou com a vítima? "))
resp = resp.lower()
if resp == "sim" or resp == "s":
  count += 1

if count == 2:
  print ("Você é suapeito!")
  print('=' * 50)
elif count == 3 or count == 4:
  print ("Você é cúmplice!")
  print('=' * 50)
elif count == 5:
  print('=' * 50)
  print("Assassino!")
else:
  print('=' * 50)
  print("Inocente")


    
    

