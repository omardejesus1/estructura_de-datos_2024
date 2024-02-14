''' Implementación de lista ligada '''
from node import Node

class LinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        nuevo_nodo= Node(val)
        nuevo_nodo.next =self.head
        self.head= nuevo_nodo
        self.counter +=1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
    if self .tail== none :
     self.headInsert(val)
     self.tail= self.head 
     return
    self.tail.next =Node(val)
    self.tail= self.tail.next
    self.counter +=1  

    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
    if self.head is None:
        raise ValueError("la lista esta vacia")
    self.head = self.head.next
    if self.head is nene:
        self.tail= None
        self.counter -=1

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
if not self.head:
    print("la lista esta vecia")
    return
if __name__ == '__main__':
    lista_ligada = LinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

   