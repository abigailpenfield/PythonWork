gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]

students_avgs = [ sum(x) / 15 for x in gradebook ]
print("Student Averages:")
print("Student 1: ", format(students_avgs[0], '.2f'))
print("Student 2: ", format(students_avgs[1], '.2f'))
print("Student 3: ", format(students_avgs[2], '.2f'))
print("Student 4: ", format(students_avgs[3], '.2f'))
print("Student 5: ", format(students_avgs[4], '.2f'))
print("Student 6: ", format(students_avgs[5], '.2f'))
print("Student 7: ", format(students_avgs[6], '.2f'))
print("Student 8: ", format(students_avgs[7], '.2f'))
print("Student 9: ", format(students_avgs[8], '.2f'))
print("Student 10: ", format(students_avgs[9], '.2f'))


assignments_avgs = [ sum(y) / 10 for y in zip(*gradebook) ]
print("\nAssignment Averages:")
print("Assignment 1: ", format(assignments_avgs[0],'.2f'))
print("Assignment 2: ", format(assignments_avgs[1],'.2f'))
print("Assignment 3: ", format(assignments_avgs[2],'.2f'))
print("Assignment 4: ", format(assignments_avgs[3],'.2f'))
print("Assignment 5: ", format(assignments_avgs[4],'.2f'))
print("Assignment 6: ", format(assignments_avgs[5],'.2f'))
print("Assignment 7: ", format(assignments_avgs[6],'.2f'))
print("Assignment 8: ", format(assignments_avgs[7],'.2f'))
print("Assignment 9: ", format(assignments_avgs[8],'.2f'))
print("Assignment 10: ", format(assignments_avgs[9],'.2f'))
print("Assignment 11: ", format(assignments_avgs[10],'.2f'))
print("Assignment 12: ", format(assignments_avgs[11],'.2f'))
print("Assignment 13: ", format(assignments_avgs[12],'.2f'))
print("Assignment 14: ", format(assignments_avgs[13],'.2f'))
print("Assignment 15: ", format(assignments_avgs[14],'.2f'))
