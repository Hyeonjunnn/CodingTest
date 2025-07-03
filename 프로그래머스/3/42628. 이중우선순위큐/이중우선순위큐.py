import heapq

def solution(operations):
    
    heap = []
    
    for operation in operations:
        spl = operation.split(" ")

        if (spl[0] == "I"):
            heapq.heappush(heap, int(spl[1]))
        elif (len(heap) > 0):
            if (spl[1] == "1") :
                heap.remove(max(heap))
            elif (spl[1] == "-1") :
                heapq.heappop(heap)
            
    print(heap)
    answer = [0, 0]
    if (len(heap) > 0):
        answer[0] = max(heap)
        answer[1] = min(heap)
    
    return answer