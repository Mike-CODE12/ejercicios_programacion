# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Deque:
    head: Node
    tail: Node


    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


    def print_structure(self):
        if not self.head:
            if not self.tail:
                print("Cannot print from empty deque")
                return
        current_node = self.head
        while (current_node is not None):
            if current_node.next is not None:
                end_str = " <-> "
            else:
                end_str = " <-> None"
            print(current_node.data, end=end_str)   
            current_node = current_node.next
        print()                                     


    def push_left(self, new_node_left):   
        if self.head is None:
            self.head = new_node_left
            self.tail = new_node_left 
            return 
        new_node_left.next = self.head
        self.head = new_node_left


    def push_right(self, new_node_right): 
        if self.head is None:
            self.head = new_node_right
            self.tail = new_node_right   
            return                 
        last_node = self.tail
        last_node.next = new_node_right 
        self.tail = new_node_right


    def pop_left(self):    
        if not self.head:
            print("Cannot pop_left from empty Deque")
            return  
        if self.head == self.tail:                
            removed_left=self.head.data
            self.head = None
            self.tail = None
            return removed_left
        removed_left = self.head.data                  
        self.head = self.head.next
        return removed_left


    def pop_right(self):                          
        if self.head is None:
            print("Cannot pop_right from empty Deque")
            return  
        if self.head == self.tail:
            removed_right=self.head.data
            self.head = None
            self.tail = None
            return removed_right
        current_node=self.head                    
        while current_node.next != self.tail:          
            current_node=current_node.next
        removed_right=current_node.next
        current_node.next = None                      
        self.tail = current_node                       
        return removed_right.data