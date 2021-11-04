n = int(input())
binary = bin(n)
binary = binary[::-1]
binary = binary.split('b')[0]


print(int(binary, 2))