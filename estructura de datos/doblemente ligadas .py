class NodoDoble:
    def _init_(self, valor=None):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
def llenar_lista_doble(valores):
    if not valores:
        return None
    head = NodoDoble(valores[0])
    curr = head
    for valor in valores[1:]:
        nuevo_nodo = NodoDoble(valor)
        nuevo_nodo.anterior = curr
        curr.siguiente = nuevo_nodo
        curr = nuevo_nodo
    return head
# Lista de entrada
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Crear la lista doblemente ligada a partir de la lista de entrada
head = llenar_lista_doble(valores)
# Imprimir la lista doblemente ligada hacia adelante
curr = head
while curr:
    print(curr.valor, end=" <-> ")
    curr = curr.siguiente
print("None")
# Imprimir la lista doblemente ligada hacia atrás
curr = head
while curr.siguiente:
    curr = curr.siguiente
while curr:
    print(curr.valor, end=" <-> ")
    curr = curr.anterior
print("None")