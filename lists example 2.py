
#These are my original tuples
characters = ["Dog", "Cat", "Hamster"]

dog_in = ("ball", "crate", "bone")
dog_in = list(dog_in)

cat_in = ["yarn", "catnip", "nails"]

hamster_in = ["wheel", "bowl", "grass"]


#I concatenate an element from the characters list to one of the other lists
dog = [characters[0],] + dog_in   #I need (,) for a tuple with only 1 element

cat = [characters[1],] + cat_in


hamster = [characters[2],] + hamster_in

#make a tuple with the 3 tuples
all_tuples = [dog, cat, hamster]

#what characters are holding
dog_hold = [dog_in[0], dog_in[2]] #Method 1
cat_hold = [all_tuples[1][1], all_tuples[1][3]] #Method 2 (takes from all_tuples)
hamster_hold = [all_tuples[2][1], all_tuples[2][2]] #Method 2 (all_tuples has 3 tuples in it)

#it would be helpful to create a big tuples/list of what all characters are holding
all_holding = [dog_hold, cat_hold, hamster_hold]

def modify_holding(charIndex, item1, item2):
    """Enter the index of the character (0, 1, or 2) and the seconddary index of the item in all tuples (0, 1, 2)"""
    all_holding[charIndex][0] = all_tuples[charIndex][item1]
    #this changes one of the first item in the all_holding lists
    all_holding[charIndex][1] = all_tuples[charIndex][item2]
    #this changes one of the second items in the all_holding list
    print(str(all_tuples[charIndex][0]) + " is holding the " + str(all_holding[charIndex][0]) + " and the " + str(all_holding[charIndex][1])) 

    
    


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
