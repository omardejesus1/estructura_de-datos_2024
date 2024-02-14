class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

def lista_a_lista_ligada_circular(e):
    if not e:  
        return None
    
    head = Nodo(e[0])  
    curr = head  
    i = 1  
    while i < len(e):
        curr.siguiente = Nodo(e[i])  
        curr = curr.siguiente  
        i += 1  
    curr.siguiente = head  # Hacer que el último nodo apunte de nuevo al primer nodo
    return head  

e = [1, 2, 3, 4, 5]
head = lista_a_lista_ligada_circular(e)
curr = head
while True:
    print(curr.valor, end=" -> ")
    curr = curr.siguiente
    if curr == head:  # Si el siguiente nodo es el inicio, entonces hemos completado un ciclo
        break
print("el nodo no tiene valor")