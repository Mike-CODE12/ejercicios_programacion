# 4. Cree las siguientes clases:
#     1. `Head`
#     2. `Torso`
#     3. `Arm`
#     4. `Hand`
#     5. `Leg`
#     6. `Feet`
#     7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.

class Hand:            
	def __init__(self):
		pass
		
right_hand= Hand()       
left_hand= Hand()


class Arm:
	def __init__(self, hand):
		self.hand = hand


right_arm=Arm(right_hand)
left_arm=Arm(left_hand)


class Feet:
	def __init__(self):
		pass

right_foot = Feet()
left_foot = Feet()


class Leg: 
	def __init__(self, foot):
		self.foot = foot

right_leg=Leg(right_foot)
left_leg=Leg(left_foot)


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