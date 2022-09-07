numero=int(input("ingrese un numero: ")) 
menor= numero
mayor= numero
while numero!=-1:
    
    if numero>mayor: #consultar en clase
        mayor=numero
    elif numero<menor:#signos '<' alreves segun mi logica
        menor=numero
    numero=int(input("ingrese otro numero: "))
print("mayor: ",mayor)
print("menor: ",menor)