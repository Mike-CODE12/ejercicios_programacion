import random
secret_number = random.randint(1, 10)
name = int(input("Guess the secret number from 1 to 10 "))
while (name != secret_number) :
    name = int(input("Try again "))
print("Congratulations, you have founded out the secret number")