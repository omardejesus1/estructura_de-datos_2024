nombre_de_la_variable =[]
metodo2 = list('ABCDE')

print(metodo2)

for i in 'CADENA DE CARACTERES':
    print(i)

    lista = range(100) #range(a,b)[a,b)
    print(list(lista))

    for i in lista: # for i in range(100)
        print(i)

        x = list(range(1,11,2))
        
        for i in range(len(x)):
            print(i, x[i])

            for i, elemento in enumerate(x):
                print(i, elemento)

                import random

                desordenada= [random.randint(1,100)for _ in range(10)]
print(desordenada)
desordenada.sort()
print(desordenada)

otralista = list('omar cardenas')
otralista.reverse()
#elemento=otralista[0]+ otralista[1]+ otralista[3]
#elemento= otralista[0:4]
#elemento= otralista[:4]
#elemento= otralista[4:]
#elemento= otralista[0:-4:3]
#elemento =otralista[::-1]
#print(elemento)
holder =''
for i in range (len(otralista)):
    holder= otralista[i]+ holder
    print(holder)

