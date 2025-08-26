from collections import deque

def solution(k, m, score):
    score.sort(reverse = True)
    dq = deque(score)
    
    arr = []
    answer = 0
    while dq:
        num = dq.popleft()
        arr.append(num)
        
        if (len(arr) == m):
            answer += (min(arr) * m)
            arr = []
    
    return answer