s = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(s):
    sum += a.pop(a.index(max(a))) * b.pop(b.index(min(b)))

print(sum)