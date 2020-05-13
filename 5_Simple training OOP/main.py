# template
class Estudent:
	# class attribute
	total = 0

	# constructor __init__()
	def __init__(self,name,id,age):
		# object attribute
		self.name = name
		self.id = id
		self.age = age
		# set math score | object	
		self.math = 0

	# method
	def showinfo(self):
		print("{} \n\t id : {} \n\t age : {} \n\t math : {}\n".format(self.name,self.id,self.age,self.math))

	def get_mathscore(self,score):
		self.math = score
		self.get_info()

	def get_info(self):
		if self.math <= 100 and self.math > 90:
			print("you get score 'A+'")
		elif self.math <= 90 and self.math > 80:
			print("you get score 'A'")
		elif self.math <= 80 and self.math > 70:
			print("you get score 'B'")
		elif self.math <= 70 and self.math > 60:
			print("you get score 'C'")
		else:
			print("you get score 'D'! (BAD SCORE)")

	def get_report(self):
		return "\nlist math score \n================\nid \t|\t name\t\t\t score\n{id} \t|\t {name}\t\t\t{score}\n".format(id=self.id,name=self.name,score=self.math)



# object
genilda = Estudent("genilda",121,18)
goransia = Estudent("goransia",122,18)

genilda.showinfo()
print(genilda.get_report())

genilda.get_mathscore(80)

genilda.showinfo()
print(genilda.get_report())

print(30*"+=")
