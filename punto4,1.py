import random
from tkinter import N 
x=int(input("Digite la cantidad de celdas: "))
lista=[]
for i in range(0,x):
    n=random.randint(0,100)
    lista.append(n)
    if i == x-1:
        print("Lista creada:",lista)
for i in range(1,x):
    for j in range(0,x-i):
        if(lista[j+1] < lista[j]):
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
print("lista ordenada:",lista)    