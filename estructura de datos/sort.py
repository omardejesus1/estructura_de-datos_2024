Lista_desordenada=[3,2,4,1,3,9]
lista_ordenada=[]
for i in range(len(Lista_desordenada)):
    maximo= max(Lista_desordenada)

    maximo= min(Lista_desordenada)
    lista_ordenada.append(maximo)
    Lista_desordenada.remove(maximo)
    print(lista_ordenada)
