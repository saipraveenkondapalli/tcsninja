n = int(input())
arr = []
count = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count += 1
    else:
        arr.append(x)

for y in range(count):
    arr.append(0)

for z in arr:
    print(z, end=' ')


