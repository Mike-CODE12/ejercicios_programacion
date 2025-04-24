#Instrucción: Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
#Por lo que observé diría que los usos que se le pueda dar a la herencia multiple depende del programa que estés creando, de lo que estés necesitando para el código
#debido a que la herencia múltiple siempre te permitirá combinar y reutilizar métodos de otras clases.
#En el siguiente ejemplo intento usar la herencia múltiple para emular una pequeña interacción en un entorno específico. 

class Teacher:

    def __init__(self, teacher):
        self.teacher = teacher


    def greeting(self):
        print(f"Teacher: Good morning class, my name is {self.teacher} and I'm the new teacher")


    def answer_concerned_students(self):
        print(f"Teacher {self.teacher}: Don't worry, she's fine, but she was transferred to another school.")


class Students:

    def __init__(self, student_1_name, student_2_name, student_3_name):
        self.student_1 = student_1_name
        self.student_2 = student_2_name
        self.student_3 = student_3_name


    def greeting_student(self):
        print("Students: Good morning teacher")


    def questions_concerned_students(self, student_1_name, student_2_name, student_3_name): 
        questions_dictionary={f"{student_1_name}": "What happened to teacher Karla?", f"{student_2_name}": "Is she okay?", f"{student_3_name}": "Will she come tomorrow?"}
        for key in questions_dictionary:
            print(f"{key}: {questions_dictionary[key]}")


class Classroom(Teacher, Students):
    
    def __init__(self, teacher, student_1_name, student_2_name, student_3_name): 
        Teacher.__init__(self, teacher) 
        Students.__init__(self, student_1_name, student_2_name, student_3_name)    


    def interaction(self):
        self.greeting()  
        self.greeting_student() 
        self.questions_concerned_students(self.student_1, self.student_2, self.student_3)
        self.answer_concerned_students()


new_class = Classroom("Jhon", "Juana", "Pedro", "Ana")
new_class.interaction()