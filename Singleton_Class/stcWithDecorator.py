
def single_ton(cls):
	l=[]
	def inner(*args , ** kwargs):
		if len(l)==0:
			l.append(cls())
		return l[0]
	return inner

@single_ton
class sample:
	def __init__(self):
		print('Object Created')

s1 =sample()
s2 =sample()
s3 =sample()

#output :-  Object Created

