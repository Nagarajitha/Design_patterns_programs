#decorator function
def outer(func):
	def inner():
		print('*' * 15)
		func()
		print('*' * 15)
	return inner


#decorated function
@outer
def wish_1():
	print('Good Morning')


#user defined function
def wish_2():
	print('Good Noon')



wish_1()
print('------------------')
wish_2()

'''
***************
Good Morning
***************
------------------
Good Noon
'''