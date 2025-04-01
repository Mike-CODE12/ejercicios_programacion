#2. Cree una clase de `Bus` con:
#    1. Un atributo de `max_passengers`.
#    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#    3. Un método para bajar pasajeros uno por uno (en cualquier orden).

import random


class Person():
	def __init__(self, name):
		self.name = name


class Bus():
	

	def __init__(self, max_passengers):
		self.max_passengers=max_passengers
		self.passengers=[]                   
		print(f"The maximum capacity of this bus is {max_passengers} passengers")
		

	def adding_passengers(self, parameter_1):
		if len(self.passengers)<self.max_passengers:             
			self.passengers.append(parameter_1.name)     
			print(self.passengers)
			return
		print("This bus is full")
		

	def getting_passengers_off(self):
		if len(self.passengers)>=1: 
			self.random_passenger = random.randint(0, (len(self.passengers)-1))      
			self.passenger_got_off=self.passengers.pop(self.random_passenger)
			print(f"{self.passenger_got_off} got off the bus")
		else:
			print("This bus is already empty")



passenger=Person("John")
passenger_1=Person("Daniel")
passenger_2=Person("Marco")
passenger_3=Person("Maria")

bus_1=Bus(3)
bus_1.adding_passengers(passenger)
bus_1.adding_passengers(passenger_1)
bus_1.adding_passengers(passenger_2)
bus_1.adding_passengers(passenger_3)
bus_1.getting_passengers_off()
bus_1.getting_passengers_off()
bus_1.getting_passengers_off()
bus_1.getting_passengers_off()