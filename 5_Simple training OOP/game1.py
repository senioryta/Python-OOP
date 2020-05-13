# game  
class Tinny_troopers:
	# class attribute
	total = 0

	# constructor __init__()
	def __init__(self,name,gun,health,armor):
		self.name = name
		self.gun = gun
		self.health = health
		self.armor = armor
		self.attack_power = (len(self.name) + len(self.gun) + len(str(self.health)) + len(str(self.armor))) * 4

	# method
	def showinfo(self):
		print("{} \n\t gun : {} \n\t health : {} \n\t armor : {} \n\t attack power : {}\n".format(self.name,self.gun,self.health,self.armor,self.attack_power))

	def attack(self,enemy):
		print(self.name + ' attack ' + enemy.name + ' with ' + self.gun)
		enemy.getattack(self)

	def getattack(self,enemy):
		print(self.name + ' get attack enemy with ' + enemy.gun)
		feel = enemy.attack_power // self.armor
		print("feel attack : " + str(feel))
		self.health -= feel
		print(self.name + ' health : ' + str(self.health) + '\n')
		if self.health < 0:
			print(self.name + ' is dead!')
			exit()
		if self.health == 0:
			print(self.name + ' is dead!')
			exit()

	def gethealth(self):
		self.health += 20
		print(self.name + " health +20!")


# object 
michael = Tinny_troopers(gun="smg",name="michael",health=90,armor=12)
samuel = Tinny_troopers("samuel","m416",93,8)

michael.showinfo()
samuel.showinfo()

michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)

samuel.gethealth()
michael.gethealth()

print('\n')

samuel.showinfo()
michael.showinfo()

michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)
samuel.attack(michael)
michael.attack(samuel)

samuel.attack(michael)
samuel.attack(michael)
samuel.attack(michael)
samuel.attack(michael)
samuel.attack(michael)

michael.attack(samuel)

# not run, because if terminate
michael.attack(samuel)
michael.attack(samuel)