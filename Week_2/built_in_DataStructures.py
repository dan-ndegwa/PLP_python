# Create an empty list
my_list = []

# Appending elements to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert the value 15 at the second position in the list.
my_list[1] = 15
print(my_list)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50,60,70])
print(my_list)

# Remove the last element from my_list
# Formula 1
my_list.pop()
print(my_list)

# Sort my_list in ascending order.
my_list.sort()
print(my_list)

# Find and print the index of the value 30 in my_list

index_30 = my_list.index(30)
print(index_30)
