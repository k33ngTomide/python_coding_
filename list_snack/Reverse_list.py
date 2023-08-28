
def main():
    print(reverse(["Akintomide", "Tomide", 1, 3, 8.9, "Muiliyu"]))

def reverse(array: list) -> list:
    new_array = []

    for counter in array[::-1]:
        temp = counter
        new_array.append(temp)

    return new_array

if __name__ == '__main__':
    main()


