# template
class Estudent:
	# private class attribute
	__total = 0

	# constructor __init__()
	def __init__(self,name,id,age):
		self.__name = name
		self.__id = id 
		self.__age = age

		# set math score
		self.__exercise = 0
		self.__homework = 0
		self.__exame = 0
		self.math

	@property
	def showdetail(self):
		return "{} \n\t id : {} \n\t age : {} \n\t math : ___\n\t\ta. exercise : {}\n\t\tb. homework : {}\n\t\tc. exame : {}\n\t\td. total score : {}".format(self.__name,self.__id,self.__age,self.__exercise,self.__homework,self.__exame,self.math)

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
	def checkpoint(self):
		pass

	@checkpoint.getter
	def checkpoint(self):
		# set math score
		self.__math = (self.__exercise + self.__homework + self.__exame) // 3

		if (self.__math >= 10 and self.__math > 9):
			return "you got score 'A+'"
		elif (self.__math >= 8 and self.__math > 7):
			return "you got score 'A'"
		elif (self.__math >= 7 and self.__math > 6):
			return "you got score 'B'"
		elif (self.__math >= 6 and self.__math > 5):
			return "you got score 'C'"
		else:
			return "you got bad score (" + str(self.__math) + ")"

# object
marciana = Estudent("marciana",134,20)
maria = Estudent("maria",135,20)

print(maria.showdetail)

maria.exercise = 9
maria.homework = 10
maria.exame = 4

print(maria.showdetail)

print(maria.checkpoint)