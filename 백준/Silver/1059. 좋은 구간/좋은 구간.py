import sys

l = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
n = int(input())

if nums[0] > n:
    max = nums[0]
    min = 0
else:
    for i in nums:
        if n < i:
            min = nums[nums.index(i)-1]
            max = i
            break

count = 0
for i in range(min+1, max-1, 1):
    if i <= n:
        for j in range(n, max, 1):
            if i < j:
                count += 1
    else:
        break

print(count)