# superclass
class Math_subject:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,estudentName,estudentId,estudentClss):
		self.__name = estudentName
		self.__id = estudentId
		self.__clss = estudentClss

		# set math score
		self.exercise = 0
		self.homework = 0
		self.exame = 0

	@property
	def showinfo(self):
		return "{} \n\t id : {} \n\t class : {} \nMath Score___________ \n\t exercise : {} \n\t homework : {} \n\t exame : {} \n\t total : {} \n".format(self.__name,self.__id,self.__clss,self.__exercise,self.__homework,self.__exame,self.math)

	@property
	def exercise(self):
		pass

	@exercise.setter
	def exercise(self,input):
		self.__exercise = input
	
	@property
	def homework(self):
		pass

	@homework.setter
	def homework(self,input):
		self.__homework = input

	@property
	def exame(self):
		pass

	@exame.setter
	def exame(self,input):
		self.__exame = input

	@property
	def math(self):
		pass

	@math.getter
	def math(self):
		self.__math = (self.__exercise + self.__homework + self.__exame) // 3
		return self.__math

	@property
	def checkpoint1(self):
		pass

	@checkpoint1.getter
	def checkpoint1(self):
		if self.__math <= 100 and self.__math > 90:
			return 'you got score "A+"'
		elif self.__math <= 90 and self.__math > 80:
			return 'you got score "A"'
		elif self.__math <= 80 and self.__math > 70:
			return 'you got score "B"'
		elif self.__math <= 70 and self.__math >= 60:
			return 'you got score "C"'
		else:
			return 'you got bad score (' + str(self.__math) + ')'

	@property
	def checkpoint2(self):
		pass

	@checkpoint2.getter
	def checkpoint2(self):
		if self.__math <= 100 and self.__math > 90:
			return self.__name + ' is passed!'
		elif self.__math <= 90 and self.__math > 80:
			return self.__name + ' is passed!'
		elif self.__math <= 80 and self.__math > 70:
			return self.__name + ' is passed!'		
		elif self.__math <= 70 and self.__math >= 60:
			return self.__name + ' is passed!'
		else:
			return self.__name + ' is not passed!'

# subclass
class Estudent_a(Math_subject):
	
	# constructor __init__()
	def __init__(self,estudentName,estudentId):
		super().__init__(estudentName,estudentId,"a")

# subclass
class Estudent_b(Math_subject):
	
	# constructor __init__()
	def __init__(self,estudentName,estudentId):
		super().__init__(estudentName,estudentId,"b")