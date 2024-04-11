#program to print 4 letter word in string in uppercase

#decorator
def outer(func):
	def inner(*args,**kwargs):
		return[word.upper() for word in func(args[0])]
	return inner


@outer
def words_length(s):
	new_l = []
	for word in s.split():
		if len(word) == 4:
			new_l.append(word)
	return new_l



def word_length(s):
	new_l = []
	for word in s.split():
		if len(word) == 4:
			new_l.append(word)
	return new_l




print(word_length('we need to learn this'))  #['need', 'this']

print(words_length('we need to learn this'))  #['NEED', 'THIS']

