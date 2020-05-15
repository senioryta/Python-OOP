# superclass
class Estudent:
	# class atributte
	total = 0

	# constructor __init__()
	def __init__(self,name,id):
		self.name = name
		self.id = id
		Estudent.total += 1

	# method
	def showinfo(self):
		print("{} \n\t id : {}".format(self.name,self.id))

# subclass
class Estudent_a(Estudent):
	pass

# subclass
class Estudent_b(Estudent):
	pass


# object
carmelinda = Estudent("carmelinda",136)
natalia = Estudent_a("natalia",137)
sandra = Estudent_b("xandra",138)

carmelinda.showinfo()
natalia.showinfo()
sandra.showinfo()