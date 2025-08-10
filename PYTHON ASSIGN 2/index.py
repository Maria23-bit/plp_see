my_list = []
print(f"Initial list: {my_list}")

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"List after appending elements: {my_list}")

my_list.insert(1, 15)
print(f"List after inserting 15 at index 1: {my_list}")

my_list.extend([50, 60, 70])
print(f"List after extending with [50, 60, 70]: {my_list}")

my_list.pop()
print(f"List after removing the last element: {my_list}")

my_list.sort()
print(f"List after sorting in ascending order: {my_list}")

try:
    index_of_30 = my_list.index(30)
    print(f"The index of the value 30 is: {index_of_30}")
except ValueError:
    print("The value 30 was not found in the list.")
