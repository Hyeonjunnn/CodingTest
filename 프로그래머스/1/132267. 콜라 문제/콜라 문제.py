def solution(a, b, n):
    
    answer = 0
    while n >= a:
        answer += int(n / a) * b
        n = int(n / a) * b + (n % a)
    
    return answer