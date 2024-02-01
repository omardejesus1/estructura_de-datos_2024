rang= int(input(" cuantos nuemros quieres que se muestre")) # este es de tipo entero, lo utilizo para preguntar cuantos numeros
fib=[0,1] # lista 
for i in range(rang-2): # por que el -2, por si escribo un numero al azar se restan los dos nueros que tengo en la lista
    fib.append(fib[-1]+ fib[-2]) # el append se utiliza para añadir, en este caso añade mas numeros
    print(fib) # el print se utliza para imprimir las operaciones realizadas
    