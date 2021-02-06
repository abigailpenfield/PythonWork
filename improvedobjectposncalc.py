def produce_float_input(prompt):
    while(True):   
        try:
            variable = float(input(prompt))
        except ValueError:
            print("Only numerical values are allowed.")
            continue
        else:
            return variable

def calculate_final_position():
    initial_x = produce_float_input("Enter the initial position: ")
    initial_v = produce_float_input("Enter the initial velocity: ")
    while(True):
        time = produce_float_input("Enter the time: ")
        if (time < 0):
            print("Negative times are not allowed.")
            continue
        else:
            break
    acceleration = produce_float_input("Enter the acceleration: ")
    final_x = initial_x + initial_v * time + 0.5 * acceleration * time ** 2
    return final_x

def main():
    new_calculation = True
    while(new_calculation):
        final_x = calculate_final_position()
        print("The final position is", final_x)
        again = input("Would you like to calculate another final position (y/n)? ")
        if (again != "y"):
            new_calculation = False


if __name__ == "__main__":
    main()
