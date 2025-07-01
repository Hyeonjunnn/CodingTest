much = int(input())
num_lis = list(map(int, input().split()))

num_lis.sort()

print(num_lis[0]*num_lis[-1])