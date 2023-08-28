if __name__ == "__main__":
    student_class = "SS3"
    counter = 0
    total = 0

    # while counter < 20:
    for x in range(2):
        score = int(input("Enter score of another student:  "))

        if score >= 0:
            counter += 1
            total = total + score
        else:
            print("Invalid Score")

    average = total / counter

    for x  in range(0, 60):
        print("*", end='')
    print("\n\t\tAso Rock Secondary School Abuja, Nigeria.")
    for x  in range(0, 60):
        print('*', end='')

    print("\nClass: ", student_class, "\nNumber of Student in class: ", counter, "\nTotal: ", total,
          "\nAverage Score: ", average)

    for x  in range(0, 60):
        print("*",end='')
