# template
class Estudent:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id,age):
		self.__name = name
		self.__id = id
		self.__age = age
		#self.info = "{} \n\t id : {} \n\t age : {} \n".format(self.name,self.__id,self.__age)

	@property
	def info(self):
		return "{} \n\t id : {} \n\t age : {} \n".format(self.__name,self.__id,self.__age)

	@property
	def name(self):
		pass

	@name.getter
	def name(self):
		return self.__name

	@name.setter
	def name(self,newname):
		self.__name = newname

	@property
	def id(self):
		pass

	@id.setter
	def id(self,newid):
		self.__id = newid

# object
lourdes = Estudent("lourdes",132,20)
luduvina = Estudent("luduvina",133,19)

print(lourdes.info)
print(lourdes.name)
lourdes.name = "luly"
print(lourdes.name)
print(lourdes.info)

print(luduvina.info)
luduvina.id = 111
print(luduvina.info)