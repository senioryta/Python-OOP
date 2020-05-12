# template
class Estudent:
	
	# constructor __init__() | magic method
	def __init__(self,InputName,InputID=None):
		# object attribute
		self.name = InputName
		self.id = InputID

# object 
auxilia = Estudent("auxilia",113)
aurito = Estudent("aurito",114)
alexandra = Estudent(InputID=115,InputName="alexandra")
beatriz = Estudent(InputName="beatriz")

print(auxilia.__dict__)
print(aurito.__dict__)
print(alexandra.__dict__)