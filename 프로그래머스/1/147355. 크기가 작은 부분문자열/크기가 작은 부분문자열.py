def solution(t, p):
    answer = 0
    for i in range(0, len(t) + 1 - len(p)):
        num = t[i: i + len(p)]
        if (num <= p):
            answer += 1
    
    return answer