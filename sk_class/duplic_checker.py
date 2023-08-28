

def check_duplicate(word):

    for element in word:
        return element if word.count(element) > 1 else "No duplicate."

if __name__ == '__main__':

    fruits = ["Apple","Orange", "Apple","Banana"]
    print(check_duplicate(fruits))
    print()

    names = ['Yoda', 'Moses', 'Joshua', 'Mark']
    print(check_duplicate(names))
