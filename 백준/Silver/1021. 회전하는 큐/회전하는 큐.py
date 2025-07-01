import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
queue = deque(range(1, n+1))

count = 0
for i in nums:
    while i in queue:
        if queue[0] == i:
            queue.popleft()
        elif len(queue) - queue.index(i) < queue.index(i):
            queue.rotate(1)
            count += 1
        elif len(queue) - queue.index(i) >= queue.index(i):
            queue.rotate(-1)
            count+=1

print(count)