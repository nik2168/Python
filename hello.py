n = int(input("take input n : "))

for i in range (1, n + 1):
    for k in range (1, int(((n+1) - i))):
        print(" ", end=" ")
    for j in range (1, 2 * (i + 1) - 2):
        print(j, end=" ")
    print()    