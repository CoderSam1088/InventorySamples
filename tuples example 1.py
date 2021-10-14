"""Part 1"""
characters = ("Dog", "Cat", "Hamster") #This is a tuple with my characters

dog_in = ("ball", "crate", "bone") #This is the inventory for the dog

cat_in = ("yarn", "catnip", "nails") #This is the inventory for the cat

hamster_in = ("wheel", "bowl", "grass") #This is the inventory for the hamster

"""Part 2"""
#Concatenate the character name to the inventory
dog = (characters[0],) + dog_in  #I convert to a tuple by typing (,)
cat = (characters[1],) + cat_in
hamster = (characters[2],) + hamster_in

"""Part 3"""
#create a tuple with the three tuples in it
all_tuples = (dog, cat, hamster)

"""Part 4"""
#create tuples for what each character is holding
#Method 1 - using the list from the beginning
dog_holding = (characters[0], dog_in[0], dog_in[2])

#Method 2 - using the new tuple all_tuples
cat_holding = (all_tuples[1][0],) + all_tuples[1][2:]
hamster_holding = (all_tuples[2][0], all_tuples[2][1], all_tuples[2][2])

#I am printing the character names and inventories
"""Print part 1"""
print("Characters: " + str(characters))

print("Dog: " + str(dog_in))

"""Print part 2"""
#printing the characters + inventories
print(dog)
print(cat)
print(hamster)

"""Print part 3"""
#print the big tuple
print(all_tuples)

#print the last 2 tuples
print(dog_holding)
print(cat_holding)
print(hamster_holding)

"""Print part 4"""
print(dog_holding[0] + " is holding the " +dog_holding[1]+ " and the " +dog_holding[2])


