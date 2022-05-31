x=int(input("Digite el tamaño del arreglo: "))
lista=[]
posicion=[]
posicion2=[]
for i in range (x):
 num=int(input(f"Digite numero[{i+1}]:"))
 lista.append(num)
mayor=lista[0]
menor=lista[0]
for i in range(1,len(lista)):
 if mayor<lista[i]:
     mayor=lista[i]
     posicion=lista.index(mayor)
 if menor>lista[i]:
     menor=lista[i]
     posicion2=list[lista.index(menor)]
print(lista)
print(f"El numero mayor es: {mayor}, en la posicion [{posicion+1}]")    
print(f"El numero menor es: {menor}, en la posicion [{posicion2+1}]") 