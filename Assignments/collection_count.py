
def count_collection(data) -> int:
    count = 0
    for item in data: count += 1
    return count

if __name__ == '__main__':

    counted_ = count_collection([49, 23, 35, 36, 27, 28, 29, 38, 39, 27, 25, 75, 95, 36, 36])
    print("The size of the collection is: ", counted_)


