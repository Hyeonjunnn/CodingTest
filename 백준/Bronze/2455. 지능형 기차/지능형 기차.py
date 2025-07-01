import sys

maxi = 0
now = 0
b=1
while b != 0:
    a, b = map(int, sys.stdin.readline().split())
    now += b
    now -= a
    if maxi < now:
        maxi = now

print(maxi)