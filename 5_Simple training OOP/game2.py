# template 
class Tekken:
	# class attribute
	total = 0

	# constructor __init__()
	def __init__(self,name,health,damagekick,damagehit,armor):
		self.name = name
		self.health = health
		self.damage_kick = damagekick
		self.damage_hit = damagehit
		self.armor = armor

	# method
	def set_vs(self1,self2):
		print(self1.name + ' vs ' + self2.name + '\n {} \t\t {}'.format(self1.health,self2.health))

	def kick(self1,self2):
		print(self1.name + ' kick ' + self2.name)
		feel_attack = self1.damage_kick // self2.armor
		self2.getkick(self1,feel_attack)
		# chek lose!
		if self1.health < 0:
			print(self1.name + '\nyou lose!')
			exit()
		elif self1.health == 0:
			print(self1.name + '\nyou lose!')
			exit()

	def getkick(self1,self2,fattack):
		print(self1.name + ' get kick by ' + self2.name)
		print("feel attack " + str(fattack))
		self1.health -= fattack
		print(self1.name + ' health ' + str(self1.health) + '\n')
		# chek lose!
		if self1.health < 0:
			print(self1.name + '\nyou lose!')
			exit()
		elif self1.health == 0:
			print(self1.name + '\nyou lose!')
			exit()

	def hit(self1,self2):
		print(self1.name + ' hit ' + self2.name)
		feel_attack = self1.damage_hit // self2.armor
		self2.gethit(self1,feel_attack)
		# chek lose!
		if self1.health < 0:
			print(self1.name + '\nyou lose!')
			exit()
		elif self1.health == 0:
			print(self1.name + '\nyou lose!')
			exit()

	def gethit(self1,self2,fattack):
		print(self1.name + ' get hit by ' + self2.name)
		print("feel attack " + str(fattack))
		self1.health -= fattack
		print(self1.name + ' health ' + str(self1.health) + '\n')
		# chek lose!
		if self1.health < 0:
			print(self1.name + '\nyou lose!')
			exit()
		elif self1.health == 0:
			print(self1.name + '\nyou lose!')
			exit()

# object
zinkazama = Tekken("zin kazama",100,93,58,10)
steve = Tekken("steve",100,44,90,15)

zinkazama.set_vs(steve)

zinkazama.kick(steve)
zinkazama.hit(steve)
zinkazama.kick(steve)

steve.hit(zinkazama)
steve.hit(zinkazama)
steve.hit(zinkazama)
steve.kick(zinkazama)

zinkazama.hit(steve)
zinkazama.kick(steve)
zinkazama.hit(steve)
zinkazama.kick(steve)
zinkazama.kick(steve)
zinkazama.hit(steve)

steve.kick(zinkazama)
steve.hit(zinkazama)
steve.hit(zinkazama)
steve.hit(zinkazama)

zinkazama.kick(steve)
steve.hit(zinkazama)
zinkazama.hit(steve)
zinkazama.kick(steve)
steve.kick(zinkazama)

steve.set_vs(zinkazama)