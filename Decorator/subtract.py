# program to subtact a from b and converting result to positive

#decorator
def outer(func):
	def inner(*args,**kwargs):
		x,y = args

		if x>y:
			return func(x,y)
		else:
			return func(y,x)
	return inner


@outer
def subtract(a,b):
	return a-b


def sub(a,b):
	return a-b

print(sub(2,10)) #-8
print(sub(10,4)) #6
print(sub(3,7))	 #-4


print(subtract(2,10))  #8
print(subtract(10,4))	#6
print(subtract(3,7))	#4