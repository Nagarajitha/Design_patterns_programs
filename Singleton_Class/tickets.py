
def single_ton(cls):
	l=[]
	def inner(*args , ** kwargs):
		if len(l)==0:
			l.append(cls())
		return l[0]
	return inner

@single_ton
class guntur_karam:
	def __init__(self):
		self.tickets =60

	def booking(self):
		tickets = int(input('enter no on tickets : '))

		if(self.tickets >= tickets):
			self.tickets = tickets
			print("tickets booked Successfully")
		else:
			print("tickets not available")
@single_ton
class hanuman:
	def __init__(self):
		self.tickets =60

	def booking(self):
		tickets = int(input('enter no on tickets : '))

		if(self.tickets >= tickets):
			self.tickets = tickets
			print("tickets booked Successfully")
		else:
			print("tickets not available")
@single_ton
class leo:
	def __init__(self):
		self.tickets =60

	def booking(self):
		tickets = int(input('enter no on tickets : '))

		if(self.tickets >= tickets):
			self.tickets = tickets
			print("tickets booked Successfully")
		else:
			print("tickets not available")
@single_ton
class fighter:
	def __init__(self):
		self.tickets =60

	def booking(self):
		tickets = int(input('enter no on tickets : '))

		if(self.tickets >= tickets):
			self.tickets = tickets
			print("tickets booked Successfully")
		else:
			print("tickets not available")


class PVR:
	print('1)GunturKaram\n2)Hanuman\n3)Leo\n4)Fighter')
	print("Choose the option")
	option =int(input())

	if (option ==1):
		g1 = guntur_karam()
		g1.booking()

	elif (option == 2):
		h1 = hanuman()
		h1.booking()

	elif (option ==3):
		l1 = leo()
		l1.booking()

	elif (option ==4):
		f1 = fighter()
		f1.booking()

	else:
		print('Invalid option')

while True:
	PVR()