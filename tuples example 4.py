
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

#what characters are holding
dog_hold = (dog_in[0], dog_in[2]) #Method 1
cat_hold = (all_tuples[1][1], all_tuples[1][3]) #Method 2 (takes from all_tuples)
hamster_in = (all_tuples[2][1], all_tuples[2][2]) #Method 2 (all_tuples has 3 tuples in it)

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