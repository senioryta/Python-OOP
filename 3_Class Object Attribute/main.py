# template
class Estudent:
	# class attribute
	# departament = "\"departament\""
	total = 0

	# constructor __init__()
	def __init__(self,InputName,InputID):
		# object attribute
		self.name = InputName
		self.id = InputID
		Estudent.total += 1
		print(str(Estudent.total) + ' : ' + self.name)

# object 
dircia = Estudent("dircia",116)
donacio = Estudent("donacio",117)
elia = Estudent("elia",118)
basilio = Estudent("basilio",119)

"""

print(dircia.__dict__)
print(donacio.__dict__)

print(dircia.departament)
dircia.departament = "IT"

print(donacio.departament)

donacio.hobby = "dance"
print(donacio.hobby)

print(dircia.__dict__)
print(donacio.__dict__)

"""

print("total estudent " + str(Estudent.total))