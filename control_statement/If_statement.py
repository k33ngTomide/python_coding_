
if __name__ == '__main__':
    print('Hi, welcome to a score calculator')

score = int(input("Enter your Score: "))

if 55 <= score < 65:
    print("your score is ", score, "your grade is D")
elif 65 >= score < 80:
    print("your score is ", score, "your grade is C")
elif 80 >= score < 90:
    print("your score is ", score, "your grade is B")
elif 90 >= score <= 100:
    print("your score is ", score, "your grade is A")
else:
    print("you failed, you need to retake this course")