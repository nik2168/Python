# import time

# t = tuple(range(1000000))
# l = list(range(1000000))

# start = time.time()
# for _ in t:
#     pass
# print("Tuple:", time.time() - start)

# start = time.time()
# for _ in l:
#     pass
# print("List:", time.time() - start)


t = (1, 2, 3,4,5);
l = []
for i in reversed(t):
    l.append(i)

print(l)