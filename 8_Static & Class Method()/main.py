# template
class Estudent:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id):
		self.__name = name
		self.__id = id
		# self.chekin()
		Estudent.__total += 1

	'''
	def chekin(self):
		print(self.__total, ':', self.__name)
	'''

	@staticmethod
	def total():
		print(Estudent.__total)

	@classmethod
	def toTal(cls):
		print(cls.__total)


# object 
joaquim = Estudent("joaquim",127)
Estudent.total()
leonardo = Estudent("leonardo",128)
leonardo.total()
licenia = Estudent("licenia",129)
licenia.toTal()
lizania = Estudent("lizania",130)
Estudent.toTal()
lijenia = Estudent("lijenia",131)
lijenia.toTal()
Estudent.toTal()