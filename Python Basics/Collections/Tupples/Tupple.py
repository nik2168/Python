# whats are tupple in python and difference between tupple and lists ?

# Tupple in python is a collection of elements which are ordered and can be of any data type. \
# it is denoted by () and elements are separated by comma. \
# Tupple is imutable means once created its elements can not be changed.

# main difference between tupple and lists is that tupple is imutable and list is mutable. \
# also tupple is more memory efficient than lists. \
# another difference is that tupple can be used as key in dictionary but list can not.

# properties of tupple :

# 1. ordered
# 2. imutable
# 3. can be of any data type
# 4. can be used as key in dictionary
# 5. more memory efficient than lists


# first = ("first", 1, 2, 1, 3)
# count = first.count(1)

# stg = ("hello",); # , is necessary at the end to make it a tupple
# print(type(stg))
# print(first[-4:])
# a = list([1,2,3]);
# print(a)

# for i in a: 
#     print(i)


#unpacking a tupple
data = (1, 2, 3)
a, b, c = data
print(a, b, c)