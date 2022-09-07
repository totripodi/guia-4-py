acu=0
mayor=0
i=int
for i in range(0,10,1):
    n=int(input("ingrese numero:"))
    acu+= n
    if(n>mayor):
        mayor=n
        posicion=i

promedio=acu/i 
print("promedio: ",promedio,"\nmayor: ",mayor,"posicion: ",posicion)