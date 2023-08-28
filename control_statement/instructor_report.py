
student_class = "SS3"
counter = 0
total = 0

while True:
    score = int(input("Enter score of another student or -25 to quit:   "))

    if score == -25:
        break

    if score >= 0:
        counter += 1
        total += score
    else:
        print("invalid score")


average = total / counter
print('''***************************************************************************
                Aso Rock Secondary School Abuja, Nigeria.                
***************************************************************************''')
print("Class: ", student_class)
print("Number of Student in class: ", counter)
print("Total: ", total)
print("Average Score: ", average)
print("***************************************************************************")
