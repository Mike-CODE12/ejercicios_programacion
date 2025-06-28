#1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self, top):
        self.top = top


    def print_structure(self):
        if not self.top:
            print("Cannot print from empty stack")
            return
        current_node = self.top
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):                        
        new_node.next = self.top            
        self.top = new_node                


    def pop(self):
        if not self.top:
            print("Cannot pop from empty stack")
            return
        if self.top:
            removed = self.top.data
            self.top = self.top.next
            return removed