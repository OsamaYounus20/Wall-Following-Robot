import string

# choices = ["w", "a", "s", "d"]
import random
# a = random.randint(0,3)
#print("hello world") 
#direction = choices[a]
#print(direction)

grid = [[9, 9, 9, 9, 9, 9, 9, 9],
	[9, 1, 1, 1, 1, 1, 1, 9],
	[9, 1, 0, 0, 0, 0, 1, 9],
	[9, 1, 0, 0, 0, 1, 9, 9],
	[9, 1, 0, 0, 0, 1, 9, 9],
	[9, 1, 0, 0, 0, 0, 1, 9],
	[9, 1, 1, 1, 1, 1, 1, 9], 
	[9, 9, 9, 9, 9, 9, 9, 9]]
for row in grid:
	print(row)
# 00 nothing
# 11 forward
# 10 left
# 01 right 
r = 1
c = 1
fitness = 1
list_len = 56
pop = 20
matching_list = "wwwwwdwdwawwwawdwdwwwwwdwwww"
pop_lists = [] 
# def gen(list_len):
# 	ex =""
# 	for count in range (list_len):
# 		x = random.randint(0,3)
# 		ex = ex + choices[x]
# 	print(ex)
# 	return ex 


class robo:

	def __init__(self):
		self.robodir = "00"
		self.robolist = ''.join(str(random.randint(0,1)) for count in range(56))
		self.area = grid 
		self.robofit = 1
		self.x = 1
		self.y = 1
		self.face = "E"
		self.visitlist = [(1, 1)]

def copies(list_len, pop):
	for count in range (pop):
		a = robo()
		pop_lists.append(a)
	return pop_lists	

def pick(pop_lists): 
	pop_lists = sorted(pop_lists, key = lambda robo:robo.robofit, reverse = True)
	pop_lists = pop_lists[:12]
	return pop_lists

def roboeval(pop_lists):
	for robo in pop_lists:
		for k in range(0, 56, 2):
			move = robo.robolist[k:k+2]
			if move == "11":
				if robo.face == "E":
					if not grid[robo.x][robo.y+1] == 9:
						robo.y = robo.y + 1
						if (robo.x, robo.y) not in robo.visitlist:
							robo.visitlist.append((robo.x, robo.y))
							if grid[robo.x][robo.y] == 1:
								robo.robofit = robo.robofit + 1
				elif robo.face == "W":
					if not grid[robo.x][robo.y-1] == 9:
						robo.y = robo.y - 1
						if (robo.x, robo.y) not in robo.visitlist:
							robo.visitlist.append((robo.x, robo.y))
							if grid[robo.x][robo.y] == 1:
								robo.robofit = robo.robofit + 1
				elif robo.face == "N":
					if not grid[robo.x-1][robo.y] == 9:
						robo.x = robo.x - 1
						if (robo.x, robo.y) not in robo.visitlist:
							robo.visitlist.append((robo.x, robo.y))
							if grid[robo.x][robo.y] == 1:
								robo.robofit = robo.robofit + 1
				elif robo.face == "S":
					if not grid[robo.x+1][robo.y] == 9:
						robo.x = robo.x + 1
						if (robo.x, robo.y) not in robo.visitlist:
							robo.visitlist.append((robo.x, robo.y))	
							if grid[robo.x][robo.y] == 1:
								robo.robofit = robo.robofit + 1
					
			elif move == "10":
				if robo.face == "E":	
					robo.face = "N"	
				elif robo.face =="W":
					robo.face = "S"
				elif robo.face == "N":
					robo.face = "W"
				elif robo.face == "S":
					robo.face = "E"	
			
			elif move == "01":
				if robo.face == "E":	
					robo.face = "S"	
				elif robo.face =="W":
					robo.face = "N"
				elif robo.face == "N":
					robo.face = "E"
				elif robo.face == "S":
					robo.face = "W"	
			
	return pop_lists	

def crossover(pop_lists):
	offspring = list()
	for count in range(4):
		breaker = random.randint(0, 56)
		p1 = random.choice(pop_lists)
		p2 =  random.choice(pop_lists)
		o1 = robo()
		o1.robolist =  p1.robolist[0:breaker] + p2.robolist[breaker:56]
		o2 = robo()
		o2.robolist =  p2.robolist[0:breaker] + p1.robolist[breaker:56]
		offspring.append(o1)
		offspring.append(o2)
	pop_lists.extend(offspring)
	return pop_lists	

def mutate(pop_lists):
	for robot in pop_lists:
		for count in range(56):
			temp = random.randint(0, 180)
			if (temp < 5):-
				if robot.robolist[count] == "1":
					new = "0"
				elif robot.robolist[count] == "0":
					new = "1"
				robo.robolist = robot.robolist[0:count] + str(new) + robot.robolist[count+1:56]
	return pop_lists			

# main starts here 
pop_lists = copies(list_len, pop)	
pop_lists = roboeval(pop_lists)
maximumfitness = pop_lists[0].robofit
print ("starting now")
ind = 1
while maximumfitness < 18:
	pop_lists = pick(pop_lists)
	pop_lists = crossover(pop_lists)
	pop_lists = mutate(pop_lists)

	for robot in pop_lists:
		robot.face = "E"
		robot.x = 1
		robot.y = 1
		robot.visitlist = [(1, 1)]
		robot.fitness = 1
	print("Generation " + str(ind))
	pop_lists = roboeval(pop_lists)
	maximumfitness = pop_lists[0].robofit
	ind = ind + 1

print("maximum fitness " + str(maximumfitness) + " found in generation " + str(ind))
