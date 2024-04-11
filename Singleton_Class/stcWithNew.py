class a:
	_instance =None #class variable
	def __new__(cls, *args,**kwargs):

		if (cls._instance is None):
			cls._instance = super().__new__(cls,*args,**kwargs) 
			'''__new__ method is overridden. This method 
			is called when an object is created. In this method:'''
		
		return cls._instance
a1 =a()
a2= a()
a3 =a()

print(a1) #<__main__.a object at 0x00000248ECC9B4A0>
print(a2) #<__main__.a object at 0x00000248ECC9B4A0>


'''
super().__new__(cls, *args, **kwargs) is a way to delegate the creation 
of the instance to the default __new__ method of the superclass. It is a
 common practice when overriding __new__ to call the superclass method to 
 ensure correct initialization of the object.'''
