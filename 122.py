n = int(input())
arr = []
answer = 0
for x in range(n):
    arr.append(int(input()))



def SmallestTwo(ans):
    lenght = len(ans)
    check =[]
    for x in range(lenght-1):
        c = ans[x]+ans[x+1]
        check.append(c)
    return [check.index(min(check)), min(check)]


def ReplaceValue(ind):
    arr[ind[0]] = ind[1]
    arr.pop(ind[0]+1)
    return int(ind[1])


for i in range(n-1):
    small = SmallestTwo(arr)
    answer += ReplaceValue(small)



print(answer)