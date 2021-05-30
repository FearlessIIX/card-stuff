import random
import time
from datetime import datetime

# a function that creates an array with numbers from 1 to 52 inclusive, then returns the array
def generate():

    y = []  # the array to be returned

    # for loop runs through every value from 1 to 53(excluded) with a step of one
    for x in range(1, 53, 1):
        y.append(str(x)) # .append adds the current value of x to the end of the array

    return y # returns the array "y"


def splitDeck(z):
    temp_choice = random.randint(1, 2)
    # sets deviation to a random number from 0 to 3 inclusive, this will represent the 
    # difference between the two decks that are made
    deviation = random.randint(0, 3)

    if temp_choice == 1:
        temp_choice = True
    else:
        temp_choice = False     

    # somehow these functions work, but i don't really know how >_<

    # if temp_choice is true, then it will put more cards in deck one
    # otherwise more cards will be put into deck two
    if temp_choice:
        del(temp_choice) # gets rid of temp_choice
    
        index_of_start = 0
        index_of_end = 26 + deviation


        # sends the following paramaters to the function "firstDeck", then uses them to
        # fill and return the deck that was instructed, is set equal to "deck_one"
        deck_one = firstDeck(index_of_start, index_of_end, z)

   
        # sends the following paramaters to the function "secondDeck", then uses them to
        # fill and return the deck that was instructed, is set equal to "deck_two"
        deck_two = secondDeck(index_of_end, z) 

    else:
        del(temp_choice) # gets rid of temp_choice

        index_of_start = 0
        index_of_end = 26 - deviation


        # sends the following paramaters to the function "firstDeck", then uses them to
        # fill and return the deck that was instructed, is set equal to "deck_one"
        deck_one = firstDeck(index_of_start, index_of_end, z)


        # sends the following paramaters to the function "secondDeck", then uses them to
        # fill and return the deck that was instructed, is set equal to "deck_two"
        deck_two = secondDeck(index_of_end, z)


# passed index_of_start, index_of_end, and the card array from main
def firstDeck(index_o_s, index_o_e, z):

    y = [] # creates the deck that is to be filled and returned

    # loops from the card at index: 0 to the card at index_of_end
    for x in range(index_o_s, index_o_e):
        y.append(z[x])

    return y  # returns the array that was filled    


# passed index_of_start, and the card array from main
def secondDeck(index_o_e, z):

    y = [] # creates the deck that is to be filled and returned

    # loops from the card after index_of_end to the card at index: 51
    for x in range(index_o_e, 52):
        y.append(z[x])

    return y  # returns the array that was filled   


def riffleShuffle(deck_one, deck_two):

    # finds the length of both decks
    length_d1 = len(deck_one)
    length_d2 = len(deck_two)

    deck_three = []  # creates the deck that is to be filled and returned

    done_check = False  # a varible that is made to control the while structure
    deck_choice = 1  # a variable that is made to pick the decks in alternating order

    # while loop runs until there are no cards left in a deck
    while not done_check:
        random.seed(time.time())
        cards_to_take = random.randint(1, 3)

        # runs the following if structure when the current deck choice is "deck_one"
        if deck_choice == 1:
            
            # exits the while structure if "deck_one" is empty
            if len(deck_one) == 0:
                done_check = True
            # empties "deck_one" if there are less cards then are wanted from "cards_to_take"    
            elif len(deck_one) < cards_to_take:
                
                deck_choice = 2  # ensures that the next cycle will take "deck_two"
                done_check = True # ensures that the structure is exited after "deck_one" is emptied
                x = 0

                # for loop runs from index 0 until the last index of "deck_one"
                for x in range(0, len(deck_one)):

                    # adds every card indexed by the loop to "deck_three"
                    deck_three.append(deck_one[x])

                x = 0

                # for loop pops every value indexed by the above for loop
                for x in range(0, len(deck_one)):
                    deck_one.pop(0)    
            else:

                deck_choice = 2  # ensures that the next cycle will take "deck_two"

                x = 0

                # for loop runs from index 0 until the index "cards_to_take" specifies out
                for x in range(0, cards_to_take):
                    
                    # adds every card indexed by the loop to "deck_three"
                    deck_three.append(deck_one[x])

                x = 0

                # for loop pops every value indexed by the above for loop
                for x in range(0, cards_to_take):
                    deck_one.pop(0)    
        else:
                       
            # exits the while structure if "deck_two" is empty
            if len(deck_two) == 0:
                done_check = True
            # empties "deck_two" if there are less cards then are wanted from "cards_to_take"    
            elif len(deck_two) < cards_to_take:
                
                deck_choice = 1  # ensures that the next cycle will take "deck_one"
                done_check = True  # ensures that the structure is exited when "deck_two" is emptied
                x = 0

                # for loop runs from index 0 until the last index of "deck_two"
                for x in range(0, len(deck_two)):

                    # adds every card indexed by the loop to "deck_three"
                    deck_three.append(deck_two[x])

                x = 0

                # for loop pops every value indexed by the above for loop
                for x in range(0, len(deck_two)):
                    deck_two.pop(0)    
            else:

                deck_choice = 1  # ensures that the next cycle will take "deck_one"

                x = 0

                # for loop runs from index 0 until the index "cards_to_take" specifies out
                for x in range(0, cards_to_take):
                    
                    # adds every card indexed by the loop to "deck_three"
                    deck_three.append(deck_two[x])

                x = 0

                # for loop pops every value indexed by the above for loop
                for x in range(0, cards_to_take):
                    deck_two.pop(0)  

    leng = len(deck_three) - 1

    if deck_choice == 1:
        
        # retuns "deck_three" if the largest deck contains no cards
        if len(deck_one) == 0:
            return deck_three

        else:

            x = 0
            
            # for loop inserts the remaining cards into a random index of "deck_three"
            for x in range(0, len(deck_one)):
                random.seed(time.time())
                ran = random.randint(0, leng)
                deck_three.insert(ran, deck_one[x])

            x = 0

            # for loop pops every value indexed by the above for loop
            for x in range(0, len(deck_one)):
                deck_one.pop(0)
    else:
        
        # returns "deck_three" if the largest deck contains no cards
        if len(deck_two) == 0:
            return deck_three

        else:

            x = 0

            # for loop inserts the remaining cards into a random index of "deck_three"
            for x in range(0, len(deck_one)):
                random.seed(time.time())
                ran = random.randint(0, leng)
                deck_three.insert(ran, deck_one[x])

            x = 0

            # for loop pops every value indexed by the above for loop
            for x in range(0, len(deck_two)):
                deck_two.pop(0)                                                                     

    return deck_three  # returns "deck_three"
