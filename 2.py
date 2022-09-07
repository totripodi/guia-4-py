aux=0
numero=int(input("ingrese un numero: ")) 
while numero!=-1:
    numero=int(input("ingrese un numero: "))
    aux+=1
print("cant. de elementos: ",aux)

if aux%2==0:
    print("es par")
else:
    print("es impar")