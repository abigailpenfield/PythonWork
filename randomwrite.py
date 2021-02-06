import random

def main():
    random_write = True
    while(random_write):
        while(True):
            try:
                num_of_ran_nums = int(input("How many random numbers do you want? "))
                if (num_of_ran_nums <= 0):
                    print("Negative values and zero are not allowed.")
                    continue
            except ValueError:
                print("The value you entered is invalid. Try again.")
            else:
                break
            
        while(True):
            try:
                lower_bound = int(input("What is the lowest the random number should be? "))
                if (lower_bound <= 0):
                    print("Negative values and zero are not allowed.")
                    continue
            except ValueError:
                print("The value you entered is invalid. Try again.")
            else:
                break
            
        while(True):
            try:
                upper_bound = int(input("What is the highest the random number should be? "))
                if (upper_bound <= 0):
                    print("Negative values and zero are not allowed.")
                    continue
            except ValueError:
                print("The value you entered is invalid. Try again.")
            else:
                break

        randomnum = open('randomnum.txt', 'w')
        for count in range(num_of_ran_nums):
            number = random.randint(lower_bound, upper_bound)
            randomnum.write(str(number) + '\n')
            
        randomnum.close()
        print("The random numbers were written to randomnum.txt")
        break

main()
