class ArrayList:
    count = 0
    new_list = [int]

    def __init__(self, initial_capacity):
        self.a = initial_capacity

    def append(self, element):
        global new_list, count

        new_list += [element]
        count += 1

    def extend(self, iterable_data):
        pass

    def remove(self, index, element):
        pass

    def pop(self, index):
        pass

    def clear(self):
        pass

    def index(self, element, start, stop):
        pass

    def count(self, x):
        pass

    def sort(self):
        pass

    def reverse(self):
        pass

    def copy(self):
        pass
