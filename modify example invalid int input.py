
#These are my original tuples
characters = ["Dog", "Cat", "Hamster"] #this is one of the most important lists

dog_in = ("ball", "crate", "bone")
dog_in = list(dog_in)

cat_in = ["yarn", "catnip", "nails"]

hamster_in = ["wheel", "bowl", "grass"]


#I concatenate an element from the characters list to one of the other lists
dog = [characters[0],] + dog_in   #I need (,) for a tuple with only 1 element

cat = [characters[1],] + cat_in


hamster = [characters[2],] + hamster_in

#make a tuple with the 3 tuples
all_tuples = [dog, cat, hamster]  #This is another really important list

#what characters are holding
dog_hold = [dog_in[0], dog_in[2]] #Method 1
cat_hold = [all_tuples[1][1], all_tuples[1][3]] #Method 2 (takes from all_tuples)
hamster_hold = [all_tuples[2][1], all_tuples[2][2]] #Method 2 (all_tuples has 3 tuples in it)

#it would be helpful to create a big tuples/list of what all characters are holding
all_holding = [dog_hold, cat_hold, hamster_hold]    #This is another important list

def modify_holding(charIndex, item1, item2):
    """Enter the index of the character (0, 1, or 2) and the secondary index of the item in all tuples (0, 1, 2)"""
    all_holding[charIndex][0] = all_tuples[charIndex][item1]
    #this changes one of the first item in the all_holding lists
    all_holding[charIndex][1] = all_tuples[charIndex][item2]
    #this changes one of the second items in the all_holding list
    print(str(all_tuples[charIndex][0]) + " is holding the " + str(all_holding[charIndex][0]) + " and the " + str(all_holding[charIndex][1])) 


def printInv(i):
    """This is a function that prints each item in the inventory"""
    for index, item in enumerate(all_tuples[i]):
        if index == 0:      #if it is the first item (character's name)
            print(item)
            line = ""       #create a blank string for the line
            for i in range(len(item)):
                #add a - for each character in the character's name
                line+="-"
            print(line)     #print the line that is same length as name
        else:
            print(item)

    print("")           #print a blank line

def choose_char():
    ind = -1
    while ind < 0:
        print("These are the characters in the game: ")
        print(characters)   #This is the name of the list with all the characters
        char = input("Which character inventory would you like?: ")
        char = char.capitalize()                #Capitalizes the first letter automatically
        if (char in characters):
            ind = characters.index(char)            #finds the index of the character in characters list
        else:
            print("Invalid input")
        print("")
    return(ind)                             #returns the index value of the character

    

choice = 0      #This is the starting value of the choice

while (choice != 5):
    #loops will run repeatedly until the user enters a 5
    print("These are your options")
    print("")
    print("1: Print a character's inventory")
    print("2: Add to a character's inventory")
    print("3: Add a new character")
    print("4: Remove from inventory")
    print("5: Quit")
    print("")
    choice = input("What would you like to do? Enter a 1 or a 2 or a 3 or a 4 or a 5: ")
    while True:
        try:
            choice = int(choice)
            if (choice <= 5 and choice >= 1):
                break
            else:
                choice = input("Invalid input. Enter a 1 or a 2 or a 3 or a 4 or a 5: ")
        except:
            choice = input("Invalid input. Enter a 1 or a 2 or a 3 or a 4 or a 5: ")
        
    #asks for a new user choice
    if(choice == 1):
        #first choice
        index = choose_char()                   #ask user to choose a character
        printInv(index)                         #print the characters inventory
    elif(choice == 2):
        #second choice
        index = choose_char()                   #ask user to choose a character
        item_to_add = input("What would you like to add to " + characters[index] + "'s inventory?: ")
                                                #ask what to add
        item_to_add = item_to_add.lower()       #make sure item is lowercase                                  
        all_tuples[index].append(item_to_add)   #add the item to all_tuples list
        printInv(index)                         #print the new inventory
    elif(choice == 3):
        #third choice
        """Adds a character to the game"""
        to_add = input("What is the name of your character?: ")     #ask character name
        to_add = to_add.capitalize()                                #capitalize the character name
        characters.append(to_add)                                   #adds to the character list
        all_tuples.append([to_add])                                 #adds to the all_tuples list
        all_holding.append([to_add])                                #adds to the all_holding list
        num_items = input("How many items are in the character's inventory?: ")    #ask how many items character has
        while type(num_items) != int:
            try:
                num_items = int(num_items)
            except:
                num_items = input("Invalid input. Enter an integer. How many items are in the character's inventory?: ")
        for i in range(num_items):                                  #run a loop to ask for each item
            item = input("Item: ")
            item = item.lower()                                     #make sure each item is lowercase
            all_tuples[-1].append(item)                          #add the item to the all_tuples list
        print("")
        printInv(-1)                                             #prints new character and its inventory
                              #use the add_char function to add a character
    elif(choice == 4):
        #fourth choice
        """Removes an item from a character's inventory"""
        index = choose_char()                   #ask user to choose a character
        print("")                               #creates a blank line
        printInv(index)                         #prints current inventory
        print("")
        remove_item = input("What item would you like to be removed?: ")
        remove_item = remove_item.lower()       #makes sure input is lowercase
        while remove_item not in all_tuples[index]:
            print("That is not in the character's inventory. Choose something in their inventory")
            print("")
            printInv(index)
            remove_item = input("What item would you like to be removed?: ")
            remove_item = remove_item.lower()       #makes sure input is lowercase
        all_tuples[index].remove(remove_item)   #removes the item specified from the list
        print("")
        printInv(index)                         #prints the inventory again
        
    print("")








#prints each characters inventory
#printInv(0)
#printInv(1)
#printInv(2)

"""    
#This is the easier way
print(characters[0])        #prints the first character in characters list
print("------------")       #prints a line of dashes
for item in dog_in:         #prints each item in the list on its own line
    print(item)

print("")       #add a blank line between the characters

#This way is more difficult, but more efficient (Use all_tuples)

for index, item in enumerate(all_tuples[1]):
    if index == 0:      #if it is the first item (character's name)
        print(item)
        print("------")     #if it is the first item, print a line
    else:
        print(item)


print("")           #print a blank line


for index, item in enumerate(all_tuples[2]):
    if index == 0:
        print(item)
        print("------")
    else:
        print(item)
"""























"""

#print all the original tuples
print("Characters: " + str(characters))
print("Dog: " + str(dog_in))
print("Cat: " + str(cat_in))
print("Hamster: " + str(hamster))


#print the new tuples with the character names
print(dog)
print(cat)
print(hamster)

#print all the tuples combined
print(all_tuples)

#use the print statement to say what each character is holding
print(str(all_tuples[0][0]) + " is holding the " + str(dog_hold[0]) + " and the " + str(dog_hold[1]))
print(str(all_tuples[1][0]) + " is holding the " + str(cat_hold[0]) + " and the " + str(cat_hold[1])) 
print(str(all_tuples[2][0]) + " is holding the " + str(hamster_hold[0]) + " and the " + str(hamster_hold[1])) 

print(all_holding)

modify_holding(0, 2, 3)
modify_holding(1, 2, 1)
modify_holding(2, 1, 3)

"""

