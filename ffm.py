
#########################################
#										#
# Jaime Manuel Trillos Ujueta			#
# Luis Daniel Fernandes Rotger			#
#										#
# Programming Assignment B 				#
# 2D Celular Automata 					#
# Forest Fire Model 					#
#										#
#########################################

from random import randint
import os 
import sys

# Counters Initialization
global ashesC
global treesC
global firesC

# Counters Initialization
ashesC = 82*101
treesC = 0
firesC = 0


# Procedure to print the cell depending of its state.
# Receives a value 0 for ground, 1 for tree and 2 for fire.
# Returns nothing
def print_cell(value):
	if (value == 0):
		sys.stdout.write(' ')
	elif (value == 1):
		sys.stdout.write('T')
	elif (value == 2):
		sys.stdout.write('*')

# Function to check if the cell with position i,j has neighbour
# 1 (tree) or 2 (fire)
# Receives the position i,j of the cell and a value treeOrFire (1 or 2)  
def checkNeighbours(grid, i, j, treeOrFire):
	# Border validation for Torus Topology
	# Rows
	if(i == 0):
		prevRow = 81
		nextRow = 1
	elif(i == 81):
		nextRow = 0
		prevRow = 80
	else:
		prevRow = i - 1
		nextRow = i + 1
	# Columns
	if(j == 0):
		prevCol = 100
		nextCol = 1
	elif(j == 100):
		prevCol = 99
		nextCol = 0
	else:
		prevCol = j - 1
		nextCol = j + 1

	# Northern neighbour
	if(grid[prevRow][j] == treeOrFire):
		return True
	# Eastern neighbour
	elif(grid[i][nextCol] == treeOrFire):
		return True
	# Southern neighbour
	elif(grid[nextRow][j] == treeOrFire):
		return True
	# Western neighbour
	elif(grid[i][prevCol] == treeOrFire):
		return True

	return False


# Function to determine the new state of the cell
# receives the position of a grid.
# Returns the new state of the cell
def defNewCellState(grid, i, j):
	
	# Counters Initialization
	global ashesC
	global treesC
	global firesC

	# Neighbour Columns and rows
	prevCol = -1 
	nextCol = -1 
	prevRow = -1 
	nextRow = -1

	# Check fire case, if so returns ground.
	if(grid[i][j] == 2):
		firesC -= 1
		ashesC += 1
		return 0

	# Check ground case
	if(grid[i][j] == 0):
		# Take random value for spontaneous growth if its lesser than p grow a tree
		sponGrowth = randint(1, 100)
		if (sponGrowth <= p):
			ashesC -= 1
			treesC += 1
			return 1

		# Check if it has a Tree neighbour
		if(checkNeighbours(grid, i, j, 1)):
			print checkNeighbours(grid, i, j, 1)
			
			# Take random value for induced growth if its lesser than q grow a tree
			indGrowth = randint(1, 100)
			if (indGrowth <= q):
				ashesC -= 1
				treesC += 1
				return 1
			else:
				return 0

		# If no Tree Neighbour found keep it ground
		else:
			return 0

	# Check tree case
	if(grid[i][j] == 1):

		# If it has a Fire neighbour, burn it!
		if(checkNeighbours(grid, i, j, 2)):
			firesC += 1
			treesC -=1
			return 2
		
		# If not
		# Take random value for spontaneous growth if its lesser than p grow a tree
		goingToBurn = randint(1, 100)
		if (goingToBurn <= f):
			firesC += 1
			treesC -= 1
			return 2
		else:
			return 1
		



os.system('clear')
print "                           FOREST FIRE MODEL"
print "                           ====== ==== ====="
print ""
print ""
print ""

# Enter input
p = raw_input('Enter the probability of spontaneous growth (p) (0-100): ')
f = raw_input('Enter the probability of spontaneous fire (f) (0-100): ')
q = raw_input('Enter the probability of induced growth (q) (0-100): ')

# Cast the input
p = int(p)
f = int(f)
q = int(q)

#Grid initialization
grid = []
for i in range(82):
	grid.append([])
	for j in range(101):
		grid[i].append(0)


#Initial print
os.system('clear')
for i in range(82):
	for j in range(101):
		print_cell(grid[i][j])
	print ''


while (True):
	print '| Ashes: ' + str(ashesC) + ' | Trees: ' + str(treesC) + ' | Fires: ' + str(firesC) + ' |'
	raw_input('Press enter everytime you want to see the new state of the grid. Ctrl + C to Exit.')
	#New Grid Construction
	newGrid = []
	for i in range(82):
		newGrid.append([])
		for j in range(101):
			newGrid[i].append(0)

	for i in range(82):
		for j in range(101):
			newGrid[i][j] = defNewCellState(grid, i, j)

	# Grid Copy
	for i in range(82):
		for j in range(101):
			grid[i][j] = newGrid[i][j]

	# Print new Grid
	os.system('clear')
	for i in range(82):
		for j in range(101):
			print_cell(newGrid[i][j])
		print ''
