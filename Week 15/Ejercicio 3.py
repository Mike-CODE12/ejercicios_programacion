#1. Implemente un `bubble_sort` que funcione para Linked Lists.
#    1. La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def print_structure(self):
        if not self.head:
            print("Cannot print an empty LinkedList")
            return
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next

    def append(self, new_node):
        if not self.head:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        current_node.next=new_node

    def remove(self):
        if not self.head:
            print("Cannot print an empty LinkedList")
            return
        if not self.head.next:
            print(f"Cannot bubble_sort a LinkedList with only an element")
            return 
        current_node=self.head
        while current_node.next.next is not None:
            current_node=current_node.next
        removed=current_node.next
        current_node.next = None
        return removed.data


    def convert_to_list(self):
        new_list = []
        current_node= self.head
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next
        return new_list

    def bubble_sort(self):
        if not self.head:
            print(f"Cannot bubble_sort an empty LinkedList")
        if not self.head.next:
            print(f"Cannot bubble_sort a LinkedList with only an element")
            return  
        swapped=True 
        first_counter=0
        while swapped:
            swapped = False
            current = self.head
            second_counter=0
            while current.next is not None:
                print(f"Iteration {first_counter+1}.{second_counter+1}. Current element: {current.data}, Next element: {current.next.data:}")
                if current.data > current.next.data:
                    print("Current element is greater than the next. Swapping them")
                    current.data, current.next.data = current.next.data, current.data
                    swapped=True
                current = current.next
                second_counter=second_counter+1
            first_counter=first_counter+1




n1 = Node(80)
n2 = Node(35)
n3 = Node(30)
n4 = Node(48)
n5 = Node(90)
n6 = Node(75)


first = LinkedList(n1)
first.append(n2)
first.append(n3)
first.append(n4)
first.append(n5)
first.append(n6)


first.print_structure()
print(first.convert_to_list())
first.bubble_sort()
first.print_structure()
print(first.convert_to_list())
