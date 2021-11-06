n = int(input())
c = int(input())
v = []
w = []

for x in range(n):
    v.append(int(input()))

for y in range(n):
    w.append(int(input()))

def solution(cap, weights, profits, n):
    if(n==0 or cap == 0):
        return 0
    if(weights[n-1]>cap):
        return solution(cap,weights,profits,n-1)
    else:return max(profits[n-1]+solution(cap-weights[n-1],weights,profits,n-1),solution(cap,weights,profits,n-1))


print(solution(c,w,v,n))
