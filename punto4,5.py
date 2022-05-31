lista=[]
lista2=[]
for i in range (10):
 num=int(input(f"Digite poscion [{i+1}]:"))
 lista.append(num)
for i in range(10):
 r=str("")
 x=lista[i]
 for j in range(x):
  r+=("*")
 print(f"{lista[i]}->{r}")