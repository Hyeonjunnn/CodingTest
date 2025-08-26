def solution(s):
    answer = []
    dic = {}
    idx = 0
    for i in s:
        if (i not in dic):
            answer.append(-1)
        else:
            answer.append(idx - dic[i])
            
        dic[i] = idx
        idx += 1

    return answer