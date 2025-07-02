from collections import deque

def solution(priorities, location):
    
    dq = deque(priorities)
    
    order_dq = deque()
    for i in range(len(priorities)):
        order_dq.append(0)
    order_dq[location] = 1
    
    cnt = 1
    for i in range(9, 0, -1):
        while i in dq:
            value = dq.popleft()
            order_value = order_dq.popleft()
            
            if (value != i):
                dq.append(value)
                order_dq.append(order_value)
            elif (value == i and order_value == 1):
                return cnt
            else:
                cnt += 1