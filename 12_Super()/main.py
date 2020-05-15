# superclass
class Estudent:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id,classroom):
		self.__name = name
		self.__id = id
		self.__class = classroom
		Estudent.__total += 1

	# method
	def showinfo(self):
		print("{} \n\t id : {} \n\t class : {} \n".format(self.__name,self.__id,self.__class))


# subclass
class Estudent_a(Estudent):
	
	# constructor __init__()
	def __init__(self,name,id):
		# call superclass and __init__()
		super().__init__(name,id,"a")
		super().showinfo()


# subclass 
class Estudent_b(Estudent):
	
	# constructor __init__()
	def __init__(self,name,id):
		# call superclass and __init__()
		super().__init__(name,id,"b")
		super().showinfo()


# object 
serafina = Estudent("serafina",138,"b")
angelia = Estudent_a("angelia",107)
suzana = Estudent_b("suzana",139)
