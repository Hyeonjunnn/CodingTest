import heapq
# [2,3], 7, => 1
def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    cnt = 0
    while True:
        val1 = heapq.heappop(scoville)
        if (len(scoville) == 0 and K > val1):
            return -1
        if (K <= val1):
            return cnt
        val2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, val1 + (val2 * 2))
        cnt += 1