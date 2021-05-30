import random
from datetime import datetime
import time
from generate import generate, firstDeck, riffleShuffle, secondDeck, splitDeck

# fetches the array from generate then puts its contents into array "z"
z = generate()

# sets deviation to a random number from 0 to 3 inclusive, this will represent the 
# difference between the two decks that are made
random.seed(time.time())
deviation = random.randint(0, 3)

# sets length to the length of the array "z", value from 1 to 52
length = len(z)  # value: 52, index from 0 to 51

# length is 52, loops runs from 2 to 51
#for x in range(0, length):
#    print(f"{x} {z[x]}")

# creates a temporary variable to store a random boolean value for use later on
temp_choice = random.randint(1, 2)

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

for v in range(0, 4):

    deck_three = riffleShuffle(deck_one, deck_two)

    deviation = random.randint(0, 3)
    temp_choice = random.randint(1, 2)

    if temp_choice == 1:
        temp_choice = True
    else:
        temp_choice = False 

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

print(deck_three)        

