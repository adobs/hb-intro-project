from termcolor import colored 
from colorama import init
init()

def create_board(array):
		print "cell#: 0 1 2 3 4 5 6 7"
		print "row 0:",Back.WHITE+str(array[0][0]),array[0][1],array[0][2],array[0][3],array[0][4],array[0][5],array[0][6],array[0][7]
		print "row 1:",array[1][0],array[1][1],array[1][2],array[1][3],array[1][4],array[1][5],array[1][6],array[1][7]
		print "row 2:",array[2][0],array[2][1],array[2][2],array[2][3],array[2][4],array[2][5],array[2][6],array[2][7]
		print "row 3:",array[3][0],array[3][1],array[3][2],array[3][3],array[3][4],array[3][5],array[3][6],array[3][7]		
		print "row 4:",array[4][0],array[4][1],array[4][2],array[4][3],array[4][4],array[4][5],array[4][6],array[4][7]
		print "row 5:",array[5][0],array[5][1],array[5][2],array[5][3],array[5][4],array[5][5],array[5][6],array[5][7]
		print "row 6:",array[6][0],array[6][1],array[6][2],array[6][3],array[6][4],array[6][5],array[6][6],array[6][7]
		print "row 7:",array[7][0],array[7][1],array[7][2],array[7][3],array[7][4],array[7][5],array[7][6],array[7][7]


positions=([[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]])

def playing():
	#return true when all the R and r or B and b are removed from the board
	#black wins
	count_red=0
	count_black=0
	winner=0
	for i in xrange(len(positions)):
		for j in xrange(len(positions)):
			if positions[i][j] == "R":
				count_red+=1
			if positions[i][j] == "r":
				count_red+=1
			if positions[i][j] == "B":
				count_black+=1
			if positions[i][j] == "b":
				count_black+=1
			if count_black==0:
				return "Red"
				
			if count_red==0:
				return "Black"
			else:
				return True

#put red on the board
for i in range(0,8,2):
	positions[0][i]=colored("R","red")
for i in range(1,8,2):
	positions[1][i]=colored("R","red")		

#put black on the board
for i in range(0,8,2):
	positions[6][i]=colored("B","blue")
for i in range(1,8,2):
	positions[7][i]=colored("B","blue")

create_board(positions)
count=0

while playing():
	if count%2==0:
		player=colored("R","red")
		player_king=colored("r","red")
		player_name="Red"
		move=1
	else:
		player=colored("B","blue")
		player_king=colored("b","blue")
		player_name="Black"
		move=-1
		
	
	while True:
		i=int(raw_input(("What row would you like to move from, %s? ")%(player_name)))
		
		j=int(raw_input(("What cell would you like to move from, %s? ")%(player_name)))
		if positions[i][j]==player_king:
			move*=-1
		if positions[i][j]==player or positions[i][j]==player_king:
			positions[i][j]=j
			break
		else:
			print "You don't have a piece there.  Try again"
	
	

	while True:
		
		k=int(raw_input(("What row would you like to move to, %s? ")%(player_name)))
		l=int(raw_input(("What cell would you like to move to, %s? ")%(player_name)))	
		if type(positions[k][l])!=str and k==i+move and (l==j+1 or l==j-1):
			positions[k][l]=player
			break
		if type(positions[k][l])!=str and k==(i+2*move) and (l==j-2)and type(positions[i+move][j-move])==str:
			positions[k][l]=player
			positions[i+move][j-move]=j-move
			break
		#for black, move is -1
		#if we're at i=5 j=1 againd want to get to k=3 l=3
		#so, jumping 4 and 2
		#for red move is 1
		#if were at i=3 j=3 and go to i=5 j=1
		#so, jumping 4  and 2

		if type(positions[k][l])!=str and k==(i+2*move) and (l==j+2) and type(positions[i+move][j+move])==str:
			positions[k][l]=player
			positions[i+move][j+move]=j+move
			break
		else:
			print "You can't move there.  Try again"

	if positions[k][l]=="R" and k==7:
		positions[k][l]="r"
	if positions[k][l]=="B" and k==0:
		positions[k][l]="b"  		

	create_board(positions)
	count+=1

winner =playing()
print "The winner is:",winner
