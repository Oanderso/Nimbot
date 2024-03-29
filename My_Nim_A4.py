
'''
#Assignment 4: Nim Player

References:
- https://www.youtube.com/watch?v=NqsZ8DD6WHU 
- https://github.com/tkl5/Nim-Game - On how to check number of stones to remove

'''
import random
import time

def main(): 
    
    #Select Mode
    print("   ____________________________________________")
    print(" / \                                           \,")
    print("|   |                                          |")
    print(" \_ |               WELCOME TO NIM             |")
    print("    |      - A text based battle of wits! -    |")
    print("    |                                          |")
    print("    |           Choose your opponent:          |")
    print("    |       1. Cerebral Thunder (Computer)     |")
    print("    |       2. A Fellow Human Player (PvP)     |")
    print("    |                                          |")
    print("    |         Enter your numerical choice:     |")
    print("    |                                          |")
    print("    |   __________________________________________")
    print("    |  /                                          /")
    print("    \_/__________________________________________/")
 
 
    gameMode = input()
    while 1:
        if gameMode == "1":
            print("You have chosen a worthy opponent! We shall see who is the sharper Nim-wit")
            break
        elif gameMode == "2":
            print("You have come to test your mettle against a fellow human? We shall see who has the Nim-bler mind!")
            break
        else:
            print("You signed up for this. There's no backing out now. You have to choose either option 1 or 2!")
            gameMode = input()
    
    
    if gameMode == "1":
        
        p1 = input("State your name, brave contestant: ")
        p2 = "Cerebral Thunder"
        
        firstOrSecond = int(input("Would you like to play first or second? Enter 1 for first or 2 for second. Your choice: "))
        if (firstOrSecond == 1):
            currentPlayer = p2
        elif (firstOrSecond == 2):
            currentPlayer = p1
        else:
            print("That is not a valid position. By default, you will be first to play then.")
            currentPlayer = p2
        
        #ask if user wants to choose piles
        choosePiles = input("Do you want to choose the maximum number of piles? Enter y for yes or n for no. Your choice: ")
        choosePiles = choosePiles.upper()
        numPiles = 2
        maxPiles = 0
        if (choosePiles == "N"):
            numPiles = random.randint(2, 6) #Set random number of piles of stones
        elif (choosePiles == "Y"):
            maxPiles = int(input("How many piles would you like to play with? Your choice: "))
            numPiles = maxPiles
        
        #set up board
        pilesList = []  
        make_board(pilesList, numPiles) # initial board
        
        #switch player after each turn
        gameState = 1
        while gameState == 1:
            
            #switch player
            if currentPlayer == p1:
                if pilesList == [0] * len(pilesList): #if there are no stones left on this player's turn, the other player has won.
                    print(currentPlayer + " is the winner!")
                    gameState == 0
                    break         
                elif pilesList != [0] * len(pilesList):
                    computer_move(pilesList, numPiles)
                    currentPlayer = p2
           
            else:
                if pilesList == [0] * len(pilesList): #if there are no stones left on this player's turn, the other player has won.
                    print(currentPlayer + " is the winner!")
                    gameState == 0
                    break    
                elif pilesList != [0] * len(pilesList):
                    player_input(pilesList, numPiles, currentPlayer) #Start the game
                    currentPlayer = p1  
                
            
    

            
    

    if gameMode == "2":
        
        #players
        p1 = input("Name of player 1: ")
        p2 = input("Name of player 2: ")
    
        currentPlayer = p1 #initialize starting player
        
        #ask if user wants to choose piles
        choosePiles = input("Do you want to choose the maximum number of piles? Enter y for yes or n for no. Your choice: ")
        numPiles = 2
        maxPiles = 0
        if (choosePiles == "n"):
            numPiles = random.randint(2, 6) #Set random number of piles of stones
        elif (choosePiles == "y"):
            maxPiles = int(input("How many piles would you like to play with? Your choice: "))
            numPiles = maxPiles
        
        #set up board
        pilesList = []  
        make_board(pilesList, numPiles) # initial board        
        
        #switch player after each turn
        gameState = 1
        while gameState == 1:
                
            #switch player
            if currentPlayer == p1:
                print("\n" + p1 + "'s turn:")
                player_input(pilesList, numPiles, currentPlayer) 
                
                if pilesList == [0] * len(pilesList): #if there are no stones left on this player's turn, the other player has won.
                    print(currentPlayer + " is the winner!")
                    gameState == 0
                    break                
                currentPlayer = p2
                
            else:
                print("\n" + p2 + "'s turn:")
                player_input(pilesList, numPiles, currentPlayer) 
                
                if pilesList == [0] * len(pilesList): #if there are no stones left on this player's turn, the other player has won.
                    print(currentPlayer + " is the winner!")
                    gameState == 0
                    break
                
                currentPlayer = p1  
                


    
    
#initialize board
def make_board(pilesList, numPiles):
    print("\n---------------------------------")
    
    print("Starting Board Configuration:")
    
    for i in range(0, numPiles):
        numRocks = random.randint(1, 10) #set randomly each iteration. Sets random number of stones in each pile.
        
        print("Pile " + str(i+1) + " --- "+ str(numRocks) + " stones") #Prin1ts piles
        pilesList.append(numRocks)
    
    
def player_input(pilesList, numPiles, currentPlayer):
    
    print("---------------------------------\n")
    goodCondition = False #initialize condition
    while goodCondition == False: 
        
        #print(currentPlayer + print("Cerebral Thunder has made its move")n.")
        pile = input('Which pile are you taking from? (Enter a number) \n')
        stone = input("How many stones are you taking? (Enter a number) \n")

        goodCondition1 = False
        if (pile.isdigit() or stone.isdigit()):
            goodCondition1 = True
        else: #arbitrary code indicating it's not an int
            pile = 9999282
            stone = 9999282

        if (pile != 9999282 or stone != 9999282): #check it's an int
            stone = int(stone)
            pile = int(pile)
            if (stone > 0 ): #check positive number of stones
                if (pile <= len(pilesList)) and (pile > 0): #check valid pile number
                    if (stone <= pilesList[pile - 1]): #check valid number of stones
                        if (int(stone) != 0) and (int(pile) != 0):
                            break
                        
                    else:
                        print("The number of stones you have chosen is invalid.")    
                else:
                    print("The pile choice is invalid. You can only pick from the listed piles.")
            else:
                print("You can only pick a positive number!")
        else:
            print("You need to enter a positive integer!")
            
        
        
    pilesList[pile - 1] -= stone #remove a stone from the pile

    # prints the piles after update
    print("   ____________________________________________")
    print(" / \                                           \,")
    print("|   |                                          |")
    print(" \_ |          --- STONES AND PILES ---        |")    
    for i in range(0, numPiles):
        print("    |   Pile " + str(i+1) + " --- "+ pilesList[i]*"✪" + ((28-2*pilesList[i])*" ") + "|") #Prints piles
        #print("    |             Pile " + str(i+1) + " --- "+ str(pilesList[i]) + " stones          |") #Prints piles
    print("    |                                          |")      
    print("    |   __________________________________________")
    print("    |  /                                          /")
    print("    \_/__________________________________________/")


    #print(pilesList)

#uses nim sum to find optimal move.
def computer_move(pilesList, numPiles):
    print("\n\nCerebral Thunder is thinking...")
    time.sleep(2)
    #https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
    #https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
    #https://github.com/tkl5/Nim-Game
    #Uses bitwise XOR operator to check the nim sum of the piles

    nimSum = 0    
    for i in pilesList:
        nimSum = nimSum^i #nimsum XOR the number of stones in the current pile    

    takeNum = abs(max(pilesList) - nimSum) #how many stones to remove
    takeFromPile = pilesList.index(max(pilesList)) #which pile to remove it from. Take from the largest pile.

    #check how many stones to remove from a pile, and which pile.
    if (nimSum > 0) and (len(pilesList) > 2) and (nimSum != max(pilesList)) and (nimSum !=1):
        pilesList[takeFromPile] -= takeNum #remove a stone from the pile

    if (nimSum > 0) and (len(pilesList) > 2) and (nimSum == max(pilesList)) and (nimSum !=1):
        pilesList[takeFromPile] -= nimSum #remove a stone from the pile

    if nimSum > 0 and len(pilesList) <= 2 and (takeNum != 0):
        pilesList[takeFromPile] -= takeNum #remove a stone from the pile        

    if nimSum > 0 and len(pilesList) <= 2 and (takeNum == 0):
        pilesList[takeFromPile] -= nimSum #remove a stone from the pile          

    if (nimSum == 1) and (len(pilesList) <= 2):
        pilesList[takeFromPile] -= nimSum #remove a stone from the pile   
        
    if (nimSum == 1) and (nimSum == max(pilesList)) and (nimSum != 0) and (len(pilesList) > 2):
        pilesList[takeFromPile] -= nimSum #remove a stone from the pile           
        
    if nimSum == 0:
        pilesList[takeFromPile] -= pilesList[takeFromPile]  #remove a stone from the pile            
        
    
    
    # prints the piles after update
    print("   ____________________________________________")
    print(" / \                                           \,")
    print("|   |                                          |")
    print(" \_ |          --- STONES AND PILES ---        |")    
    for i in range(0, numPiles):
        print("    |   Pile " + str(i+1) + " --- "+ pilesList[i]*"✪" + ((28-2*pilesList[i])*" ") + "|") #Prints piles
        #print("    |             Pile " + str(i+1) + " --- "+ str(pilesList[i]) + " stones          |") #Prints piles
    print("    |   __________________________________________")
    print("    |  /                                          /")
    print("    \_/__________________________________________/")
        
    
    #print(pilesList[takeFromPile])
    #print(pilesList)
   
    print("Cerebral Thunder has made its move.\n\n")
   
   
   
   
   
   
#run program     
main()