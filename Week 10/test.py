class Person():
    name = "Juan"

    def __init__(self, name):
        self.name=name
        print(f"h{name}")

objeto_1=Person("Mike")
print(objeto_1.name)