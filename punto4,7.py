print("Por favor digite 8 valores")
lista=[]
cont=0
for i in range(8):
 lista.append(input(f"Digite poscion [{i+1}]:"))
print(lista)
for i in range(8):
 aux=int(lista[i])
 for j in range(2,aux):
  resto=aux%j
  if resto==0:
    cont+=1
 if cont==0:
  lista[i]=1
 else:
  lista[i]=0
print(lista)