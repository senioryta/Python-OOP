# template
class Estudent:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id,age):
		# private object attribute
		self.__name = name
		self.__id = id 
		self.__age = age
		Estudent.__total += 1



# object 
ifania = Estudent("ifania",124,20)
ilda = Estudent("ilda",125,20)
januario = Estudent("januario",126,22)