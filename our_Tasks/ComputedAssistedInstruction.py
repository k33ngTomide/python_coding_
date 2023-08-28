import random

first_number = 0
second_number = 0
def quiz_question() -> tuple:
    global first_number
    first_number =  random.randint(0, 10)
    global second_number
    second_number= random.randint(0, 10)
    return first_number, second_number


def saved_question() -> None:
    user_answer = int(input(f"How much is {first_number} times {second_number}: "))
    answer = first_number * second_number

    if user_answer == answer:
        print("Very Good!")
        main()
    else:
        print("No, Please try again!")
        saved_question()

def main() -> None:
    quiz_question()
    saved_question()

if __name__ == '__main__':
    main()
