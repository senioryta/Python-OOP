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

	# getter
	def showname(self):
		print(self.__name)

	def showid(self):
		return self.__id

	def showinfo(self):
		print("{} \n\t id : {} \n\t age : {} \n".format(self.__name,self.__id,self.__age))

	# setter
	def changename(self,newname):
		self.__name = newname 

	def changeid(self,newid):
		self.__id = newid

# object 
ifania = Estudent("ifania",124,20)
ilda = Estudent("ilda",125,20)
januario = Estudent("januario",126,22)

# ifania.showname()
# print(ifania.showid())

ifania.showinfo()

ifania.changename('fania')
ifania.changeid('100')

ifania.showinfo()

ilda.showname()
print(januario.showid())