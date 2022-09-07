
acumulador=0
resul=0
n=42
while n>=42 and  n<=176: ##Con WHILE
    
    if n%2!=0:
        resul+=n
        print("n:",n)
    n+=1                    ##CORRECION: 2 para ahorrarnos el if aplica para for tambien
print("resultado:",resul) 
"""
acu=0
for i in range(42,176+1,1):   ##con FOR
    if i%2!=0:
        print(i)
        acu+=i 

print("acu",acu) """
