from collections import deque

def solution(prices):
    answer = []
    prices_dq = deque(prices)
    
    while (len(prices_dq) > 0):
        val = prices_dq.popleft()
        
        cnt = 0
        for i in prices_dq:
            cnt += 1
            if (val > i):
                break
            
        answer.append(cnt)
    
    return answer