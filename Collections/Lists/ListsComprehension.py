# list = [1,2,3,4];

# print(list)

# newList = [i for i in list if i > 2]  # derived list from another list in one line with conditions

# print(newList)

# list = [1,2,[4,5]];

# for i in range(0,4):
#     if(i == 1):
#         t = list[i];
#         list[i] = list[i + 1]
#         list[i + 1] = t

# the following code will take a number n from user and then n elements
# then it will store all the elements in a list and print it

list = [] # empty list
n = int(input("enter a number : ")) # take a number from user
for _ in range(n): # loop will run n times
    t = int(input()) # take an element from user
    list.append(t) # add the element in the list

print(list) # print the list

