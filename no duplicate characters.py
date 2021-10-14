
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

def modify_holding(charIndex):
    """Enter the index of the character (0, 1, or 2) and the secondary index of the item in all tuples (0, 1, 2)"""
    opt = 0
    if opt != 3:
        print("Your character can hold up to 2 items. Please select one of the following options: ")
        print("1: Add an item to what the character is holding.")
        print("2: Remove an item from what the character is holding.")
        print("3: Make no changes")
        opt = input("What would you like to do? Enter a 1 or a 2 or a 3 or a 4: ")
        while True:
            try:
                opt = int(opt)
                if (opt >= 1 and opt <= 3):
                    break
                else:
                    opt = input("Invalid input. What would you like to do? Enter a 1 or a 2 or a 3: ")
            except:
                opt = input("Invalid input. What would you like to do? Enter a 1 or a 2 or a 3: ")
        print("")
        if opt == 1:
            yn = "Yes"
            while yn == "Yes":
                printHolding(charIndex)
                print("This is the characters inventory: ")
                printInv(charIndex)
                item1 = input("What would you like the character to hold? ")
                item1 = item1.lower()
                while True:
                    if item1 in all_tuples[charIndex]:
                        if item1 not in all_holding[charIndex]:
                            break
                        else:
                            item1 = input(characters[charIndex] + " is already holding that item. Choose another item: ")
                    else:
                        print("Invalid input. Choose an item from the character's inventory:")
                        printInv(charIndex)
                        print("")
                        item1 = input("What would you like the character to hold? ")
                        item1 = item1.lower()
                item_ind = all_tuples[charIndex].index(item1)
                if len(all_holding[charIndex])<2:
                    all_holding[charIndex].append(item1)
                else:
                    print(str(all_tuples[charIndex][0]) + " is currently holding the " + str(all_holding[charIndex][0]) + " and the " + str(all_holding[charIndex][1])+".")
                    rep_item = input("Which item would you like to replace?: ")
                    rep_item = rep_item.lower()
                    while rep_item not in all_holding[charIndex]:
                        rep_item = input("Invalid input. Which item would you like to replace?: ")
                        rep_item = rep_item.lower()
                    ind = all_holding[charIndex].index(rep_item)
                    all_holding[charIndex][ind] = all_tuples[charIndex][item_ind]
                yn = input("Do you want to add another item? Enter Yes or No: ")
                yn = yn.capitalize()
                #this changes one of the second items in the all_holding list
        if opt == 2:
            yn = "Yes"
            while yn == "Yes":
                printHolding(charIndex)
                item1 = input("What item would you like the character to stop holding?: ")
                item1 = item1.lower()
                while item1 not in all_holding[charIndex]:
                    print("Invalid input. Choose an item the character is holding.")
                    printHolding(charIndex)
                    item1 = input("What item would you like the character to stop holding?: ")
                    item1 = item1.lower()
                all_holding[charIndex].remove(item1)
                yn = input("Do you want to add another item? Enter Yes or No: ")
                yn = yn.capitalize()
        print("")
        printHolding(charIndex)


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

def printHolding(i):
    """This is a function that prints each item the character is holding"""
    char = characters[i]
    if len(all_holding[i])<2:
        if len(all_holding[i])<1:
            print(char + " is not currently holding any items.")
        else:
            print(char + " is holding the " + all_holding[i][0] + ".")
    else:
        print(characters[i] + " is holding the " + all_holding[i][0] + " and the " + all_holding[i][1] + ".")
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

while (choice != 7):
    #loops will run repeatedly until the user enters a 5
    print("These are your options")
    print("")
    print("1: Print a character's inventory")
    print("2: Add to a character's inventory")
    print("3: Add a new character")
    print("4: Remove from inventory")
    print("5: Print what a character is holding")
    print("6: Change character holding")
    print("7: Quit")
    print("")
    choice = input("What would you like to do? Enter a 1 or a 2 or a 3 or a 4 or a 5 or 6 or a 7: ")
    while True:
        try:
            choice = int(choice)
            if (choice <= 7 and choice >= 1):
                break
            else:
                choice = input("Invalid input. Enter a 1 or a 2 or a 3 or a 4 or a 5 or a 6 or a 7: ")
        except:
            choice = input("Invalid input. Enter a 1 or a 2 or a 3 or a 4 or a 5 or a 6 or a 7: ")
        
    #asks for a new user choice
    if(choice != 3 and choice != 7):
        #first choice
        index = choose_char()                   #ask user to choose a character
        if choice == 2:
            """Adds to a character's inventory"""
            #second choice
            item_to_add = input("What would you like to add to " + characters[index] + "'s inventory?: ")
                                                    #ask what to add
            item_to_add = item_to_add.lower()       #make sure item is lowercase
            while item_to_add in all_tuples[index]:
                item_to_add = input("That item is already in " + characters[index] +"'s inventory. Choose a new item: ")
                item_to_add = item_to_add.lower()
            all_tuples[index].append(item_to_add)   #add the item to all_tuples list
        elif choice == 4:
            """Removes an item from a character's inventory"""
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
            if remove_item in all_holding[index]:
                all_holding[index].remove(remove_item)
        elif choice == 5:
            printHolding(index)
        elif choice == 6:
            modify_holding(index)
            
    elif(choice == 3):
        #third choice
        """Adds a character to the game"""
        to_add = input("What is the name of your character?: ")     #ask character name
        to_add = to_add.capitalize()                                #capitalize the character name
        while to_add in characters:
            to_add = input("That is already a character. Choose a new character: ")     #ask character name
            to_add = to_add.capitalize()                                #capitalize the character name
        characters.append(to_add)                                   #adds to the character list
        all_tuples.append([to_add])                                 #adds to the all_tuples list
        all_holding.append([])                                #adds to the all_holding list
        num_items = input("How many items are in the character's inventory?: ")    #ask how many items character has
        index = -1
        while type(num_items) != int:
            try:
                num_items = int(num_items)
            except:
                num_items = input("Invalid input. Enter an integer. How many items are in the character's inventory?: ")
        for i in range(num_items):                                  #run a loop to ask for each item
            item = input("Item: ")
            item = item.lower()                                     #make sure each item is lowercase
            while item in all_tuples[index]:
                item = input("That item is already in the inventory. Choose a new item: ")
                item = item.lower()
            all_tuples[index].append(item)                          #add the item to the all_tuples list

    print("")
    if choice != 7 and choice != 5 and choice != 6:
        printInv(index)                                             #prints new character and its inventory
                                                                    #use the add_char function to add a character

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

