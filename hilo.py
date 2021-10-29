from random import randint
'''
Author: Ronald Coello
Course: CSE 210
Purpose: Build an game game in which the player guesses if the next 
card drawn by the dealer will be higher or lower than the previous one. 
Points are won or lost based on whether or not the player guessed correctly.
'''
#Generate the card using randit

def cardGenerator():
    card = randint(1, 13)
    return card

#Get the input (Guess) from the user and validate it

def getInput():   
    done = False
    while not done:
        userGuess = (input('Higher or lower?[h/l]: '))
        if userGuess.lower() == "h" or userGuess.lower() == "l":
            done =  True
        else:
            print('Sorry, that is not a correct input')
            done = False
    return userGuess

 #Compare the UserGess to the card generated
def compareCards(userGuess, card1, card2):
    secondValue = 0
    if userGuess == 'l':
        if card1 > card2:
            secondValue = 100
        else:
            secondValue = -75
    elif userGuess == 'h':
        if card1 < card2:
            secondValue = 100
        else:
            secondValue = -75

    return secondValue

#do the math add or reduce points
def computePoints(points, pointsToAddOrReduce):
    points = points + pointsToAddOrReduce
    return points


    
#function to check if the user wants and can keep playing
def canPlay(points):
    done = False
    if points <= 0:
        done = True
    elif points > 0:
        userChoice = input('Keep playing?: [y/n]')           
        if userChoice.lower() == 'y':
            done = False
        elif userChoice.lower() == 'n':
            done = True

    return done

def main():    
    done = False
    points = 300
    while not done:        
        card1 = cardGenerator() #generates first card with function cardGenerator()
        card2 = cardGenerator() #generates second card with function cardGenerator()
        print(f'The card is {card1}') #Show the first card
        userGuess = getInput() #call the function getInput(), get the user guess, and store it in a variable
        print(f'The next card is {card2}') #show the second card
        pointsToAddOrReduce = compareCards(userGuess, card1, card2) #compare the cards, return a positive or negative value to add or reduce the points, and store it in a variable
        points = computePoints(points, pointsToAddOrReduce) #do the math and reasign the variable points with the new points
        #check if point is a negative number and set points to 0
        if points <= 0:
            points = 0 
        print(f'Your score is: {points}') #show new score
        done = canPlay(points) #check if points are greater than 0 and user wants to keep playing
             
    print('Game Over')
            

main()
