from termcolor import colored 
# from colorama import init
# init()

#add double jumps

#check the input to make sure its passable

class Game_Piece (object):
	def __init__(self,color,king):
		self.color=color
		self.king=king

		

class CheckerBoard(object):
	def __init__(self):
		
		#is it ok to instantantiate objects of a class in another class and not ever in the actual program?
		#refactor this to be in a loop
		#take out the king attribute
		# self.board = [(Game_Piece("r", False, [0,0])), (Game_Piece("r", False, [0,2])), (Game_Piece("r", False, [0,4])), (Game_Piece("r", False, [0,6])),(Game_Piece("r", False, [1,1])),(Game_Piece("r", False, [1,3])),(Game_Piece("r", False, [1,5])),(Game_Piece("r", False, [1,7])),(Game_Piece("b", False, (6,0))),(Game_Piece("b", False, (6,2))),(Game_Piece("b", False, (6,4))),(Game_Piece("b", False, (6,6))),(Game_Piece("b", False, (7,1))),(Game_Piece("b", False, (7,3))),(Game_Piece("b", False, (7,5))),(Game_Piece("r", False, (7,7)))]
		self.board = {}
		for i in range (0,8,2): 
			self.board[(0,i)]=Game_Piece("r",False)
			self.board[(1,i+1)]=Game_Piece("r",False)
			self.board[(6,i)]=Game_Piece("b",False)
			self.board[(7,i+1)]=Game_Piece("b",False)


		# why is this self.current_player where as in the rest of code is my_game.current_player?
		self.current_player = 'r'

	def is_there_a_piece(self, start_position):
		if (start_position[0],start_position[1]) in self.board and self.current_player == self.board[tuple(start_position)].color.lower():
			return start_position
		else: 
			start_position[0] = int(raw_input("You don't have a piece there.  What row do you want to move from "+ player_color_dictionary[self.current_player]+"?"))
			print "here 5"
			start_position[1] = int(raw_input("What column do you want to move from "+ player_color_dictionary[self.current_player]+"?"))
			return self.is_there_a_piece(start_position)
		#output should tell you which piece you're using

	def is_king(self,end_position):
		# if self.board[end_position].color="r" and end_position[1]=
		pass



	def double_jump(self,move,jumped_piece_zero, jumped_piece_one):

		if self.board[(jumped_piece_zero,jumped_piece_one)].color.lower()!=self.current_player and (jumped_piece_zero+move,jumped_piece_one+move) not in self.board or (jumped_piece_zero+move,jumped_piece_one-move) not in self.board:
			end_position[0]=int(raw_input("Wahoo!  You can do another jump.  What row do you want to move to "+ player_color_dictionary[self.current_player]+"?"))
			end_position[1]=int(raw_input("What column do you want to move to "+ player_color_dictionary[self.current_player]+"?"))
			end_position= [end_position[0],end_position[1]]
			return end_position
		# else:
		# 	print "how do you break out of this"

	def single_jump(self, move,start_position,start_position_zero, start_position_one,end_position):
		if self.board[(start_position_zero,start_position_one)].color.lower()!=self.current_player and (start_position_zero+move)==end_position[0] and ((start_position_one+move)==end_position[1] or (start_position_one-move)==end_position[1]):
					
					del self.board[tuple(start_position)]	
					
					del self.board[(start_position_zero,start_position_one)]
					self.board[tuple(end_position)]=Game_Piece(self.current_player,False)
		
					if (end_position[0]+move,end_position[1]+move) in self.board:
						self.double_jump(move,end_position[0]+move,end_position[1]+move)
					if (end_position[0]+move, end_position[1]-move) in self.board: 
						self.double_jump(move,end_position[0]+move,end_position[1]-move)

	def move(self, start_position, end_position):
		#move from top bottom, 
		if self.current_player == 'r':
			move = 1
		elif self.current_player == 'b':
			move = -1
		# else:
		# 	move = 1 or move = -1

		#why does this have to be self. something instead of just the function?

			#is the type a string or 
		while True:
			start_position = self.is_there_a_piece(start_position)
			if (end_position[0],end_position[1]) in self.board:
				end_position[0]=int(raw_input("You can't move there.  Try again.  What row do you want to move to "+ player_color_dictionary[self.current_player]+"?"))
				print "here1"
				end_position[1]=int(raw_input("What column do you want to move to "+ player_color_dictionary[self.current_player]+"?"))
			
		#moving one diagonally
			
			elif (start_position[0]+move)==end_position[0] and (start_position[1]+1)==end_position[1] or (start_position[1]-1)==end_position[1]:
				print "moving one diagonally"  
				del self.board[tuple(start_position)]	
				self.board[tuple(end_position)]=Game_Piece(self.current_player,False)
				break

		#why do my pieces have to be ojbects?  why can't they just be strings

		#jumping
		#checks that there is a string type that is not equal to the current player and that the end move is really a jump away
		#is it a tuple? should i be working with brackets or parenthesis?

		# should be in a function, what has changed should be parameters
			elif (start_position[0]+move,start_position[1]+move) in self.board:
				self.single_jump(move,start_position,start_position[0]+move,start_position[1]+move,end_position)
				break

			elif (start_position[0]+move,start_position[1]-move) in self.board:
				self.single_jump(move,start_position,start_position[0]+move,start_position[1]-move,end_position)
				break

			#figure out the proper if statements for how to get the parameters to be right to pass through the double_jump function
			
			else:
				end_position[0]=int(raw_input("You can't move there.  Try again.  What row do you want to move to "+ player_color_dictionary[self.current_player]+"?"))
				end_position[1]=int(raw_input("What column do you want to move to "+ player_color_dictionary[self.current_player]+"?"))

		#checks for the next possible jump
		



		# self.board[].location=

		#moving for a king

		#becoming a king
		#


		
		pass

	def haswinner(self):
		# search self.board to see if there are both types of pieces
		#use keys method to turn dictionary keys into a list
		#iterate through the list 
		count_red=0
		count_black=0
		for key in self.board.keys():
			if self.board[key].color=="r" or self.board[key].color=="R":
				count_red+=1
			if self.board[key].color=="b" or self.board[key].color=="B":
				count_black+=1

		if count_red==0:
			return True
		elif count_black==0:
			return True
		else:
			return False



	def print_board(self):
		#if something is a king or not
		board_coordinates= [range(8) for x in range(8)]
		
		for i in range(8):
			for j in range(8):
				if (i,j) in self.board:
					board_coordinates[i][j]=self.board[(i,j)].color

		for line in board_coordinates:
			for space in line:
				if space == 'r':
					print colored(space, 'red'),
				elif space == 'b':
					print colored(space, 'blue'),
				else:
					print space,

			print	






		#lots of formatting stuff and searching for 
		pass

my_game = CheckerBoard()

#where would i put the following into a class?
player_color_dictionary = { "r": "Red", "b": "Black"}


while True:
	
	my_game.print_board()
	#start position is a tuble
	start_position=[0,0]
	end_position=[0,0]
	start_position[0] = int(raw_input("What row would you like to move from "+ player_color_dictionary[my_game.current_player]+"?")) # shorthand for current move and end move

	start_position[1] = int(raw_input ("what column would you like to move from "+ player_color_dictionary[my_game.current_player]+"?"))
	end_position[0] = int(raw_input("What row would you like to move to "+ player_color_dictionary[my_game.current_player]+"?")) # shorthand for current move and end move
	end_position[1] = int(raw_input ("what column would you like to move to "+ player_color_dictionary[my_game.current_player]+"?"))
	
	my_game.move(start_position,end_position)
	if my_game.haswinner():
		print player_color_dictionary[my_game.current_player], 'is the winner'
		break
	my_game.current_player = 'b' if my_game.current_player == 'r' else 'r'



#####################################################################

# def create_board(array):
# 		print "cell#: 0 1 2 3 4 5 6 7"
# 		print "row 0:","\033[0;47;37m"+str(array[0][0])+"\033[0m",array[0][1],"\033[0;47;37m"+str(array[0][2])+"\033[0m",array[0][3],"\033[0;47;37m"+str(array[0][4])+"\033[0m",array[0][5],"\033[0;47;37m"+str(array[0][6])+"\033[0m",array[0][7]
# 		print "row 1:",array[1][0],"\033[0;47;37m"+str(array[1][1])+"\033[0m",array[1][2],"\033[0;47;37m"+str(array[1][3])+"\033[0m",array[1][4],"\033[0;47;37m"+str(array[1][5])+"\033[0m",array[1][6],"\033[0;47;37m"+str(array[1][7])+"\033[0m"
# 		print "row 2:","\033[0;47;37m"+str(array[2][0])+"\033[0m",array[2][1],"\033[0;47;37m"+str(array[2][2])+"\033[0m",array[2][3],"\033[0;47;37m"+str(array[0][4])+"\033[0m",array[2][5],array[2][6],array[2][7]
# 		print "row 3:",array[3][0],array[3][1],array[3][2],array[3][3],array[3][4],array[3][5],array[3][6],array[3][7]		
# 		print "row 4:",array[4][0],array[4][1],array[4][2],array[4][3],array[4][4],array[4][5],array[4][6],array[4][7]
# 		print "row 5:",array[5][0],array[5][1],array[5][2],array[5][3],array[5][4],array[5][5],array[5][6],array[5][7]
# 		print "row 6:",array[6][0],array[6][1],array[6][2],array[6][3],array[6][4],array[6][5],array[6][6],array[6][7]
# 		print "row 7:",array[7][0],array[7][1],array[7][2],array[7][3],array[7][4],array[7][5],array[7][6],array[7][7]


# positions=([[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]])

# def playing():
# 	#return true when all the R and r or B and b are removed from the board
# 	#black wins
# 	count_red=0
# 	count_black=0
# 	winner=0
# 	for i in xrange(len(positions)):
# 		for j in xrange(len(positions)):
# 			if positions[i][j] == "R":
# 				count_red+=1
# 			if positions[i][j] == "r":
# 				count_red+=1
# 			if positions[i][j] == "B":
# 				count_black+=1
# 			if positions[i][j] == "b":
# 				count_black+=1
# 			if count_black==0:
# 				return "Red"
				
# 			if count_red==0:
# 				return "Black"
# 			else:
# 				return True

# def moving():
# 	if type(positions[k][l])!=str and k==(i+2*move) and (l==j+2) and type(positions[i+move][j+move])==str:


# #put red on the board
# for i in range(0,8,2):
# 	positions[0][i]=colored("R","red")	
# for i in range(1,8,2):
# 	positions[1][i]=colored("R","red")		

# #put black on the board
# for i in range(0,8,2):
# 	positions[6][i]=colored("B","blue")
# for i in range(1,8,2):
# 	positions[7][i]=colored("B","blue")

# create_board(positions)
# count=0

# while playing():
# 	if count%2==0:
# 		player=colored("R","red")
# 		player_king=colored("r","red")
# 		player_name="Red"
# 		move=1
# 	else:
# 		player=colored("B","blue")
# 		player_king=colored("b","blue")
# 		player_name="Black"
# 		move=-1
		
	
# 	while True:
# 		i=int(raw_input(("What row would you like to move from, %s? ")%(player_name)))
		
# 		j=int(raw_input(("What cell would you like to move from, %s? ")%(player_name)))
# 		if positions[i][j]==player or positions[i][j]==player_king:
# 			positions[i][j]=j
# 			move*=-1
# 			break
# 		else:
# 			print "You don't have a piece there.  Try again"
	
	

# 	while True:
		
# 		k=int(raw_input(("What row would you like to move to, %s? ")%(player_name)))
# 		l=int(raw_input(("What cell would you like to move to, %s? ")%(player_name)))	
# 			if type(positions[k][l])!=str and k==i+move and (l==j+1 or l==j-1):
# 			positions[k][l]=player
# 			break
# 		if type(positions[k][l])!=str and k==(i+2*move) and (l==j-2)and type(positions[i+move][j-move])==str:
# 			positions[k][l]=player
# 			positions[i+move][j-move]=j-move
# 			break
# 		#for black, move is -1
# 		#if we're at i=5 j=1 againd want to get to k=3 l=3
# 		#so, jumping 4 and 2
# 		#for red move is 1
# 		#if were at i=3 j=3 and go to i=5 j=1
# 		#so, jumping 4  and 2


# 		if type(positions[k][l])!=str and k==(i+2*move) and (l==j+2) and type(positions[i+move][j+move])==str:
# 			positions[k][l]=player
# 			positions[i+move][j+move]=j+move
# 			break
# 		else:
# 			print "You can't move there.  Try again"

# 	if positions[k][l]=="R" and k==7:
# 		positions[k][l]="r"
# 	if positions[k][l]=="B" and k==0:
# 		positions[k][l]="b"  		

# 	create_board(positions)
# 	count+=1

# winner =playing()
# print "The winner is:",winner
