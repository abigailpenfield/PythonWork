import random

class Animal:
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        generate_ran_num = random.randint(1, 3)
        if (generate_ran_num == 1):
            self.__mood = "happy"
        elif (generate_ran_num == 2):
            self.__mood = "hungry"
        elif (generate_ran_num == 3):
            self.__mood = "sleepy"

    def get_animal_type(self):
        return self.__animal_type
    
    def get_name(self):
        return self.__name
    
    def check_mood(self):
        return self.__mood
        

    
