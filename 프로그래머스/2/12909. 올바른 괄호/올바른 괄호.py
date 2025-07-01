from collections import deque

def solution(s):
    
    dq = deque()
    
    for _ in s:
        if (len(dq) != 0 and _ == ")"):
            dq.popleft()
        else:
            dq.append(_)
        
    if (len(dq) == 0):
        answer = True
    else:
        answer = False
        
    return answer