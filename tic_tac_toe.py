#tic-tac-toe logic
#2014 Livio Conzett

import time
import random
""" 
7 8 9
4 5 6
1 2 3
"""

#the plaxer field that will be shown on screen
field =[""," "," "," "," "," "," "," "," "," "]

#field that is used for calculating next move
num = [0,0,0,0,0,0,0,0,0,0]


def main():
    show()
    while Finish() == False:
        PlayerMove()
        if Win():
            break
        CompMove()
        show()
        if Win():
            break
            

#get the players move	
def PlayerMove():
    global field
	#get a number from the player
    while True:
        while True:
            try:
                num = int(raw_input("Place an X:  "))
                break
            except KeyboardInterrupt: #still make ctrl c possible
                raise
            except:
                print "That's not a number!"
		
		#check if num is in range
        if num <1 or num >9:
            print "Number not in range (1-9)"
		#check if field is still free
        elif field[num] != " ":
            print "Can't place an X there." 
        else:
            field[num] = "X"
            break

#Shows the field on the screen
def show(): 
    global field
	
    print ""
    print " " + field[7] + " I " + field[8] + " I " + field[9]
    print "---I---I---"
    print " " + field[4] + " I " + field[5] + " I " + field[6]
    print "---I---I---"
    print " " + field[1] + " I " + field[2] + " I " + field[3]
    print ""
	
#check if the field is full	
def Finish():
    if " " in field:
        return False
    else:
        show()
        print ""
        print ""
        print ""
        print "It's a draw."
        return True

# Check if someone won		
def Win():
    Convert()
	
    if CheckRow(3) == False and CheckCol(3) == False and CheckDia(3) == False:
        if CheckRow(15) == False and CheckCol(15) == False and CheckDia(15) == False:
            return 0
        else:
            print ""
            print ""
            print "I Win!"
            return True	
    else:
        show()
        print ""
        print ""
        print "you Win!"
        return True
	
#Computers move	O	
def CompMove():
    global field
    global num
    Convert()
	
	#check if comp can win
    if CheckRow(10) != False:
        field[CheckRow(10)] = "O"
        return 0
    elif CheckCol(10) != False: 
        field[CheckCol(10)] = "O"
        return 0
    elif CheckDia(10) != False:
        field[CheckDia(10)] = "O"
        return 0
	
	#check if user can 
    if CheckRow(2) != False:
        field[CheckRow(2)] = "O"
        return 0
    elif CheckCol(2) != False:
        field[CheckCol(2)] = "O"
        return 0
    elif CheckDia(2) != False:
        field[CheckDia(2)] = "O"
        return 0
	
	# if nothing fill a random space
    elif field[5] == " ":
        field[5] = "O"
    elif FindRandCorn() != 0:
        field[FindRandCorn()] = "O"
        return 0
    else:
        field[FindRand()] = "O"

#find random corner for beginning
def FindRandCorn():
    y = []
    
    if field[1] == " ":
        y.append(1)
    if field[3] == " ":
        y.append(3)
    if field[7] == " ":
        y.append(7)
    if field[9] == " ":
        y.append(9)
    if len(y) != 0:
        while True:
            
            return random.choice(y)
    else:
        return 0
		
#find random empty field
def FindRand():
    y = []
    c = 1
    
    while c < 9:
        if field[c] == " ":
            y.append(c)
        c += 1
    if len(y) > 0:
        return random.choice(y)
    else:
        return 0
        
#check for rows with two X's and an empty space 
def CheckRow(y):
    x = 1
    while x <= 7:
        if CalcRow(x) == y:
            return EmptySpaceRow(x)
        x += 3
    return False
	
#check for coloms with two X's and an empty space
def CheckCol(y):
    x = 1
    while x <= 3:
        if CalcCol(x) == y:
            return EmptySpaceCol(x)
        x += 1
    return False
	
#check for diagonals with two X's and an empty space
def CheckDia(y):
    x = 1
    while x <= 3:
        if CalcDia(x) == y:
            return EmptySpaceDia(x)
        x += 2
    return False
		
#Calculates the row starting with x
def CalcRow(x):
    return num[x] + num[x+1] + num[x+2]

#Check which space in the row is still empty
def EmptySpaceRow(x):
    if num[x] == 0:
        return x
    if num[x+1] == 0:
        return x+1
    if num[x+2] == 0:
        return x+2
	
#Calculates the colum starting with x
def CalcCol(x):
    return num[x] + num[x+3] + num[x+6]

#Check which space in the colum is still empty
def EmptySpaceCol(x):
    if num[x] == 0:
        return x
    if num[x+3] == 0:
        return x+3
    if num[x+6] == 0:
        return x+6
	
#Calculates the diagnal starting with x
def CalcDia(x):
    if x == 1:
        return num[1] + num[5] + num[9]
    if x == 3:
        return num[3] + num[5] + num[7]

#Check which space in the colum is still empty
def EmptySpaceDia(x):
    if x == 1:
        if num[1] == 0:
            return 1
        if num[5] == 0:
            return 5
        if num[9] == 0:
            return 9
    if x == 3:
        if num[3] == 0:
            return 3
        if num[5] == 0:
            return 5
        if num[7] == 0:
            return 7

#converts the field list into the num list 
def Convert():
    global field
    global num
    y = 1
    while y < len(field):
        if field[y] == "X":
            num[y] = 1
        elif field[y] == "O":
            num[y] = 5
        else:
            num[y] = 0
		# X is 1 and O is 5. That way when calculating you can't mix up an O with two X's
		# opposed to X being 1 and O being 2   x I x I   = 2     o I  I   = 2
        y +=1
	
if __name__ == "__main__":
    main()
