import random

# position of 1. player
#			2. monster
#			3. door 
#			are represented with tuples

CELLS=[
	(0,0),(0,1),(0,2),
	(1,0), (1,1), (1,2),
	(2,0), (2,1), (2,2)
	]

def get_locations():
	#get player's location
	while True:
		player = random.choice(CELLS)
		#get monster's location
		monster = random.choice(CELLS)
		#get door's location
		door = random.choice(CELLS)

		#if player, monster and door are the same start over
		# return get_locations():
		if not player== monster and not player == door and not monster==door:
			break

	return player, door, monster

# returns player
def move_player(player, move):
	# get player's current locaition
	x,y = player

	# if move is Right: x +1
	if move=='RIGHT':
		x+=1
	# if move Left: x-1
	if move == 'LEFT':
		x-=1
	# if player move Up: y-1
	if move =='LEFT':
		y-=1
	# if player move down: y+1
	if move=='DOWN':
		y+=1
	player=x,y

	return player

def get_moves(player):
	moves=['LEFT', 'RIGHT', 'UP', 'DOWN']
	x,y=player
	#if players y is 0 , remove left
	if y ==0:
		moves.remove('LEFT')
	# if players x is 0 remove up
	if x==0:
		moves.remove('UP')
	# if players y is 2, remove right
	if y==2:
		moves.remove('RIGHT')
	# if players x is 2 , remove dowm
	elif x==2:
		moves.remove('DOWN')
	return moves

while True:
	
	position=get_locations()

	player=position[0]
	door = position[1]
	monster = position[2]

	possible_moves = get_moves(player)

	print("Dungeon Game Started\n")
	print("Your currentely at position {}\n".format(position[0]))  			# format position
	print("You can move to {}\n".format(possible_moves))					# available moves
	print("Enter QUIT to exit,\n Enter HELP for help \n")
	
	print("CELLS[0] CELLS[1] CELLS[2]")
	print("CELLS[3] CELLS[4] CELLS[5]")
	print("CELLS[6] CELLS[7] CELLS[8]")

	



	moves = input("> ")
	moves = moves.upper()

	if moves=='QUIT':
		break
	
	if moves in possible_moves:
		play = move_player(player, moves)

	# if play position is door: win
	if play==position[1]:
		print("You Won !!")
		break

	# if player's position is monster: lost
	if play==position[2]:
		print("You got eaten by the monster. You Lost !!")
		break

		# if player's position in unvalid do nothing
		#if position[0]==invalid:
			#continue
