#Construye un cuerpo humano de lo mas pequeño a lo mas grande
#Que partes conforman un cuerpo humano?
#Voy a utilizar los atributos como objetos para poderlos usar de parametros para crear cada parte extensa del cuerpo humano

class Hand:             #Empiezo con una parte que no necesitará de parámetros
	def __init__(self):
		pass
		
right_hand=Hand()       #Creo los objetos necesarios con esta clase para los parámetros de la siguiente parte más grande
left_hand=Hand()


class Arm:
	def __init__(self, right_hand, left_hand):
		self.right_hand = right_hand
		self.left_hand = left_hand

right_arm=Arm(right_hand, left_hand)
left_arm=Arm(right_hand, left_hand)


class Feet:
	def __init__(self):
		pass

right_foot = Feet()
left_foot = Feet()

feet=Feet()


class Leg: 
	def __init__(self, right_foot, left_foot):
		self.right_foot = right_foot
		self.left_foot = left_foot

right_leg=Leg(right_foot, left_foot)
left_leg=Leg(right_foot, left_foot)


class Head:
	def __init__(self):
		pass

head=Head()


class Torso:
	def __init__(self, head, right_arm, left_arm):
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm
		
torso=Torso(head, right_arm, left_arm)


class Human:
	def __init__(self, torso, right_leg, left_leg):
		self.torso = torso
		self.right_leg = right_leg
		self.left_leg = left_leg
		
body_human=Human(torso, right_leg, left_leg)



# class Leg: 
# 	def __init__(self, right_foot, left_foot, right_knee, left_knee):
# 		self.right_foot = right_foot
# 		self.left_foot = left_foot
# 		self.right_knee = right_knee
# 		self.left_knee = left_knee
#No puedo hacerlo de esta manera porque necesito colocar los parametros y por eso debo irlos creando con partes que no necesiten de otras		
# right_foot=Leg()
# left_foot=Leg()
# right_knee=Leg()
# left_knee=Leg()

# right_leg=Leg()
# left_leg=Leg()










#class Person:
#	def __init__(self, name):
#		self.name=name


#name=Person()
#eyes=head()                    #Juan=Person()
#right_hand = Hand()                          #Estoy creando atributos en objetos
#right_arm = Arm(right_hand)
#torso = (head, right_arm)