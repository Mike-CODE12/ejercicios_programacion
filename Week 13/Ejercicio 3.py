# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
# Luego cree un decorador para funciones que acepten un `User` como parámetro 
# que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date


class User:

    def __init__(self, date_of_birth):
        self.date_of_birth=date_of_birth


    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    

def adults_only(function):
    def modified_function(user, *args, **kwargs):
        try:
            if user.age < 18:
                raise ValueError("This user is not an adult.")
        except ValueError as ex:
            print(ex)
            exit() 
        return function(user, *args, **kwargs)
    return modified_function