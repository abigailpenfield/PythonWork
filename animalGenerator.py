from Animal import Animal

print("Welcome to the animal generator!")
print("This program creates animal objects.")

animal_list = []

while (True):
    animal_type = input("What type of animal would you like to create? ")
    name = input("What is the animal's name? ")
    created_animal = Animal(animal_type, name)
    animal_list.append(created_animal)
    more_animals = input("Would you like to add more animals? (y/n) ")
    if (more_animals != "y"):
        break
 
print("Animal List:")
for created_animal in animal_list:
    print("{} the {} is {}.".format(created_animal.get_animal_type(), \
                                    created_animal.get_name(), \
                                    created_animal.check_mood()))

#OR
#for created_animal in animal_list:
    #animal_name = created_animal.get_name()
    #animal_type = created_animal.get_animal_type()
    #animal_mood = created_animal.check_mood()

    #print(animal_name, "the", animal_type, "is", animal_mood)
