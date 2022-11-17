a = [int(input("->")) for i in range(6)]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i], end=" ")