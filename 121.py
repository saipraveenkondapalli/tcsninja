n = int(input())
arr = []
for x in range(n):
    arr.append(int(input()))

zero = arr.count(0)
one = arr.count(1)
two = arr.count(2)
count = 0
for x in range(zero):
    arr[count] = 0
    count += 1
for x in range(one):
    arr[count] = 1
    count += 1
for x in range(two):
    arr[count] = 2
    count += 1

for x in arr:
    print(x, end=" ")

