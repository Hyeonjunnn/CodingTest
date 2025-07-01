n = int(input())

nums = list(map(int, input().split()))

table = []
table = nums.copy()

j = 0
while j < n:
    if j == min(table):
        table[nums.index(j)] = 1001
        j += 1
        continue
    else:
        coordinate = table.index(min(table))
        nums[coordinate] = j
        table[coordinate] = 1001
        j += 1

for i in nums:
    print(i, end = ' ')