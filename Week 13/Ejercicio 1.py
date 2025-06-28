#1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.


def parameter_printer_returning_function(function):
    def modified_function(*args, **kwargs):
        for index in args:               
            print(index)
        for index_2 in kwargs:                  
            print(kwargs[index_2])
        return function (*args, **kwargs)
    return modified_function