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
    card = randint(1, 14)
    return card

#Get the input (Guess) from the user and validate it

def getInput():   
    done = False
    while not done:
        userGuess = (input('Higher or lower?[h/l]: '))
        if userGuess == "h" or userGuess == "l":
            done =  True
        else:
            print('Sorry, that is not a correct input')
            done = False
    return userGuess

 #Compare the UserGess to the card generated
def compare(userGuess, card):
    pass



def main():

    pass
