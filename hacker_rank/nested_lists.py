
def main():

    number_of_student = int(input())

    names_ = []
    scores_ = []

    for _ in range(number_of_student):
        name = input()
        score = float(input())

        names_.append(name)
        scores_.append(score)

    new_score = [score for score in scores_]

    new_score.sort()

    second_lowest_score = 0.0
    for score in new_score:
        if score > new_score[0]:
            second_lowest_score = score
            break

    students = []

    for counter in range(len(scores_)):
        if second_lowest_score == scores_[counter]:
            students.append(names_[counter])

    students.sort()

    for student in students:
        print(student)
