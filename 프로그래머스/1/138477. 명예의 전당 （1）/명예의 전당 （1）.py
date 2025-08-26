def solution(k, score):
    arr = []
    answer = []
    for i in score:
        if (len(arr) < k):
            arr.append(i)
        else:
            if (i >= arr[0]):
                arr[0] = i
        arr.sort()
        answer.append(min(arr))
        
    return answer