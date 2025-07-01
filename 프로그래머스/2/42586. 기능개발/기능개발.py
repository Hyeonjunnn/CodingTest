from collections import deque
from math import ceil

def solution(progresses, speeds):
    
    dq = deque()
    
    idx = 0
    for progress in progresses:
        cal = (100 - progress)
        
        val = ceil(cal / speeds[idx])
        if ((cal % speeds[idx]) != 0):
            val += 1
        
        dq.append(val)
        
        idx += 1
    
    answer = []
        
    cnt = 0
    max_val = dq[0]
    while(len(dq) != 0):
        val = dq.popleft()
        
        if (val <= max_val):
            cnt += 1
        else:
            max_val = val
            answer.append(cnt)
            cnt = 1
    
    answer.append(cnt)
    
    return answer