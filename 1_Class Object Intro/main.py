# template
class Estudent:
	pass


# object 
angelina = Estudent()
angelina.name = "angelina"
angelina.id = 111

aprilia = Estudent()
aprilia.name = "aprilia"
aprilia.id = 112

print(angelina.name)
print(aprilia.id)

print(angelina.__dict__)
print(aprilia.__dict__)

print(20*'-')
print(Estudent.__dict__)