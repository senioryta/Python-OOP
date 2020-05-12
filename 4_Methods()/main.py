# template
class Estudent:
	# class attribute
	total = 0

	# constructor __init__()
	def __init__(self,name,id):
		self.name = name
		self.id = id

	# method | with print()
	def showname(self):
		print("estudent \n\t name : {}".format(self.name))

	# with return
	def showid(self):
		return "\t id : {}".format(self.id)

	# with agrument
	def changeid(self,newid):
		self.id = newid

# object 
eusebio = Estudent("eusebio",120)

"""
print(eusebio.name)
print(eusebio.id)
print(eusebio.__dict__)
"""

eusebio.showname()
print(eusebio.showid())
eusebio.changeid(223)
print(10*"-")
print(eusebio.showid())
print(eusebio.__dict__)