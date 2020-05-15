# superclass
class Estudent:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id,clss):
		self.name = name
		self.id = id
		self.clss = clss
		Estudent.__total += 1

	# method 
	def showinfo(self):
		print("type Estudent \n {} \n\t id : {} \n\t class : {} \n".format(self.name,self.id,self.clss))

# subclass
class Estudent_a(Estudent):

	# constructor __init__()
	def __init__(self,name,id):
		super().__init__(name,id,"a")

	# override method
	def showinfo(self):
		print("type Estudent_a \n {} \n\t id : {} \n\t class : {} \n".format(self.name,self.id,self.clss))

# subclass
class Estudent_b(Estudent):
	
	# constructor __init__()
	def __init__(self,name,id):
		super().__init__(name,id,"b")

	# override method
	def showinfo(self):
		print("type Estudent_b \n {} \n\t id : {} \n\t class : {} \n".format(self.name,self.id,self.clss))

# object
juliao = Estudent_b("juliao",140)
rivaldo = Estudent_a("rivaldo",102)
teresinha = Estudent_b("teresinha",141)

rivaldo.showinfo()
juliao.showinfo()
teresinha.showinfo()