
#These are my original tuples
characters = ("Dog", "Cat", "Hamster")

dog_in = ("ball", "crate", "bone")

cat_in = ("yarn", "catnip", "nails")

hamster_in = ("wheel", "bowl", "grass")


#I concatenate an element from the characters list to one of the other lists
dog = (characters[0],) + dog_in   #I need (,) for a tuple with only 1 element

cat = (characters[1],) + cat_in


hamster = (characters[2],) + hamster_in

#make a tuple with the 3 tuples
all_tuples = (dog, cat, hamster)

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

