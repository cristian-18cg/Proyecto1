print("Por favor digite 10 valores")
lista=[]
x=0
for i in range(10):
 num=int(input(f"Digite el valor[{i+1}]:"))
 lista.append(num)
print("Lista 1:",lista)
for i in range(1,len(lista)):
  for j in range(0,len(lista)-i):
    if(lista[j+1] > lista[j]):
      lista[j],lista[j+1]=lista[j+1],lista[j]      
print("Lista ordenada de mayor a menor",lista)
for i in range(1,len(lista)):
  for j in range(0,len(lista)-i):
    if(lista[j+1] < lista[j]):
      lista[j],lista[j+1]=lista[j+1],lista[j]      
print("Lista ordenada de menor a mayor",lista)