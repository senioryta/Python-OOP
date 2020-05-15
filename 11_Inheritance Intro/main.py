# superclass
class Estudent:
	# class atributte
	total = 0

	# constructor __init__()
	def __init__(self,name,id):
		self.name = name
		self.id = id
		Estudent.total += 1

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

print(carmelinda.__dict__)
print(natalia.__dict__)
print(sandra.__dict__)