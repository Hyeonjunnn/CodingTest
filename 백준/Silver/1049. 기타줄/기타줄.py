import sys

n, m = map(int, sys.stdin.readline().split())

pac_price = []
each_price = []
ans = []
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    pac_price.append(x)
    each_price.append(y)

ans.append(min(pac_price)*(n // 6) + min(each_price)*(n % 6))
ans.append(min(pac_price)*(n // 6 + 1))
ans.append(min(each_price)*n)

print(min(ans))