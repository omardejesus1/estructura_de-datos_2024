Lista_desordenada=[3,2,4,1,3,9]

for i in range(len(Lista_desordenada)):
    for j in range(len(Lista_desordenada)-i-1):
        if(Lista_desordenada[j]> Lista_desordenada[j+1]):
            Lista_desordenada[j], Lista_desordenada[j+1], Lista_desordenada[j]
print(Lista_desordenada)