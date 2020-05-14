# template
class Estudent:
	# class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id):
		# object attribute
		self.name = name
		self.id = id

		'''
		# public attribute
		self.departament = '"departament"'

		# _protected attribute
		self._departament = '"departament"'
		'''

		# __private attribute 
		self.__departament = '"departament"'
		Estudent.__total += 1


# object
hermengildo = Estudent("hermengildo",123)

'''
# access public
print(hermengildo.departament)
hermengildo.departament = 'IT'
print(hermengildo.departament)

# access _protected like public
print(hermengildo._departament)
hermengildo._departament = 'IT'
print(hermengildo._departament)

# can't access __private & change 
#print(hermengildo.__departament)
#print(hermengildo.departament)
hermengildo.__departament = "IT"
print(hermengildo.__departament)
print(hermengildo.__dict__)
'''