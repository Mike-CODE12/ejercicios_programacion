# 2. Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
# y arroje una excepción de no ser así.


def parameter_checker(function):
    def modified_function(*args, **kwargs):
        for index in args:  
            try:             
                if type(index) != int:    
                    if type(index) != float:
                        raise ValueError("This parameter is not a number")
            except ValueError as ex:
                print(ex)
                exit()
        for value in kwargs.values():                 
            try:             
                if type(value) != int:
                    if type(value) != float:
                        raise ValueError("This parameter is not a number")
            except ValueError as error:
                print(error)
                exit()
        return function (*args, **kwargs)
    return modified_function