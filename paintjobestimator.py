#format this better
print("A painting company has determined that for every 350 square feet of wall space,\
 one gallon of paint and six hours of labor are required.  The company charges\
 $62.25 per hour for labor.")
print("This program is a paint job estimator.")
#should set constants for knowns

import math

do_estimation = True
while(do_estimation):
    while (True):
        try:
            wall_space = float(input("Enter the square feet of wall space: "))
            if (wall_space <= 0):
                print("Only positive values are allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
    while (True):
        try:
            price_of_paint = float(input("Enter the price of paint per gallon: "))
            if (price_of_paint <= 0):
                print("Only positive values are allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    gallons_of_paint = wall_space / 350
    gallons_of_paint = math.ceil(gallons_of_paint)
    
    hours_of_labor = (wall_space / 350) * 6
    
    cost_of_paint = price_of_paint * gallons_of_paint

    labor_charges = hours_of_labor * 62.25
    
    total_cost = cost_of_paint + labor_charges

#should use comma, not plus sign
    print("Gallons of paint needed: ", gallons_of_paint)
    print("Hours of labor needed: ", format(hours_of_labor, '.1f'))
    print("Cost of paint: $", cost_of_paint)
    print("Labor charges: $", format(labor_charges, ',.2f'))
    print("Total cost of paint job: $", format(total_cost, ',.2f'))

    another_estimation = input("Do you want to perform another estimation? (y/n): ")
    if (another_estimation != "y"):
        do_estimation = False

