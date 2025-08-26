def solution(s, skip, index):
    result = []
    
    for i in s:
        chr_i = i
        cnt = index
        
        while(cnt != 0):
            if (chr_i == 'z'):
                chr_i = 'a'
            else:
                chr_i = chr(ord(chr_i) + 1)
        
            if (chr_i not in skip):
                cnt -= 1
                
        result.append(chr_i)
    
    answer = ''
    for i in result:
        answer += i
    
    return answer