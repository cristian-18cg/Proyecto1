lista=[]
aux=0
print("Por favor digite 10 numeros")
for i in range(10):
 num=int(input(f"Digite poscion [{i+1}]:"))
 lista.append(num)
igual=int(input("Por favor digite el numero a comparar: "))
for i in range(10):
 if lista[i]==igual:
  aux=aux+1
print(f"El numero {igual} se repite {aux} veces")