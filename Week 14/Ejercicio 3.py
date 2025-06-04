# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    data: str

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root


    def print_structure(self):
        if self.root is None:
            print("Cannot print from empty BinaryTree")
            return
        self.print_node(self.root, 0)

    def print_node(self, node, level):
        if node is None:
            return
        print('  ' * level + node.data)
        self.print_node(node.left, level + 1)
        self.print_node(node.right, level + 1)
