'''A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array arrt of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

For Example:

N=7 and arr = [4,5,0,1.9,0,5,0].
There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array
Example 1:

Input:

7  – Value of N
[4,5,0,1,0,0,5] – Element of arr[O] to arr[N-1],While input each element is separated by newline
Output:

4 5 1 9 5 0 0
Example 2:

Input:

6
— Value of N.
[6,0,1,8,0,2] – Element of arr[0] to arr[N-1], While input each element is separated by newline
Output:

6 1 8 2 0 0 '''
#******************************************************************************Answer**********************************************************************************************

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


