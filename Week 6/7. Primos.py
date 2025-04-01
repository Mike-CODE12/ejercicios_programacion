#7. Cree una función que acepte una list_1 de números y retorne una list_1 con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matematica para averiguar si un number es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la list_1, revisar si cada number es primo, y agregarlo a otra list_1). Así que lo mejor es agregar **otra función** para revisar si el number es primo o no.*


def is_prime(number):
    if number <= 1:             #Los números primos son mayores que 1, así que si el número es 1 o menor, se retorna False
        return False
    if number == 2:             #El número 2 es el único número primo par, por lo que si el número es 2, se retorna True
        return True     
    if number % 2 == 0:         #Si el número es divisible por 2 (es decir, es par y mayor que 2), no puede ser primo, por lo que se retorna False
        return False
    for index in range(3, int(number**0.5) + 1, 2):   # Si number tiene un divisor mayor que su raíz cuadrada, entonces también tendrá un divisor menor
        if number % index == 0:                       # Número elevado a 0.5 es equivalente a la raíz cuadrada de número
            return False
    return True


def list_of_primes(parameter_1):
    primes = []
    for number in parameter_1:
        if (is_prime(number)==True):
            primes.append(number)
    print(primes)


list_of_primes([1, 4, 6, 7, 13, 9, 67, 41, 47, 72, 17, 74])


numb=12+3.5
print(int(numb**0.5))