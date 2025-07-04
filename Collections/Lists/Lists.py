# list is a collection of elements which are ordered and can be of any data type. \
# it is denoted by [] and elements are separated by comma.



fruits = ["apple", "banana", "cherry", "mango"];

# print(fruits) # print a list ...

# print(type(fruits)) # type of list

# print("length : ", len(fruits)) # length of list

# print(fruits.__contains__("mango"))

# if "mango" in fruits:
#     print("mango is there !")
# else: print("mango is not there !")

# print(fruits[-1]) # reverse access of list

# print(fruits[1:3]) # slice access of list

# fruits.append(5); # append at end
# print(fruits)

# fruits.insert(1, "kiwi") # insert at index
# print(fruits)

# fruits.extend([1, 2, 3]) # extend list
# print(fruits)

# fruits.remove("kiwi") # remove element
# print(fruits)

# fruits.pop() # remove last element
# print(fruits)

fruits[1] = "blue"
print(fruits)
      
fruits[1:4] = ["kiwi", "mango", "guava"]
fruits.sort() # sort ascending order
fruits.sort(reverse=True) # sort reverse
print(fruits)

temp = fruits;
print(temp)