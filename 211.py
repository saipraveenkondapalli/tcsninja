n = int(input())
arr = []
sum = 0


for x in range(n):
    arr.append(int(input()))


for x in range(n):
    if arr[x] == 0:
        c = x
        while c<=n-1:
            if arr[c] ==1:
                sum +=1
            c += 1

print(sum)
