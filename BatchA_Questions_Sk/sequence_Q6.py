

sequence = input("Enter a list of numbers separating them with a comma:  ")
list_generated = sequence.split(",")
tuple_generated = tuple(list_generated)

print(f'List: {list_generated}\nTuple: {tuple_generated}')
