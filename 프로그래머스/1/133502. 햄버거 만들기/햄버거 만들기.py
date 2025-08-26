from collections import deque
def solution(ingredient):
    answer = 0
    
    dq = []
    for i in ingredient:
        dq.append(i)
        
        if (len(dq) >= 4 and dq[-4:] == [1,2,3,1]):
            dq.pop()
            dq.pop()
            dq.pop()
            dq.pop()
            
            answer += 1
    
    return answer