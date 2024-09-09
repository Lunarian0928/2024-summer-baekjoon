import heapq # min heap
import sys
input = sys.stdin.read

def main():
    data = input().strip().split('\n')
    T = int(data[0]) # 테스트 케이스의 개수
    
    index = 1
    results = [] 
    
    for _ in range(T):
        max_heap = [] # 최대 힙
        min_heap = [] # 최소 힙
        count = {}
        
        for i in range(int(data[index])):
            index += 1 
            command = data[index].split() # 연산 입력
            op = command[0] # 명령
            X = int(command[1]) # 명령에 사용할 정수
            
            # 삽입 명령
            if op == 'I':
                heapq.heappush(max_heap, -X)
                heapq.heappush(min_heap, X)
                if X in count: # X가 카운트에 있다면
                    count[X] += 1 # 카운트를 증가
                else:
                    count[X] = 1 # 카운트를 1로 초기화
            
            # 삭제 명령
            elif op == 'D':
                if X == 1: # 최댓값 제거
                    # count가 0일 때 heap에서 원소를 완전히 제거
                    while max_heap and count.get(-max_heap[0], 0) == 0:
                        heapq.heappop(max_heap)
                    # 최대 힙이 비어있지 않을 경우
                    if max_heap:
                        # 최댓값을 삭제 후
                        max_value = -heapq.heappop(max_heap)
                        # 카운트를 업데이트
                        count[max_value] -= 1
                        
                        if count[max_value] == 0:
                            del count[max_value]
                
                elif X == -1: # 최솟값 제거
                    # count가 0일 때 heap에서 원소를 완전히 제거
                    while min_heap and count.get(min_heap[0], 0) == 0:
                        heapq.heappop(min_heap)
                    # 최소 힙이 비어있지 않을 경우
                    if min_heap:
                        # 최솟값을 삭제 후
                        min_value = heapq.heappop(min_heap)
                        # 카운트를 업데이트
                        count[min_value] -= 1
                        if count[min_value] == 0:
                            del count[min_value]
        
        while max_heap and count.get(-max_heap[0], 0) == 0:
            heapq.heappop(max_heap)
        while min_heap and count.get(min_heap[0], 0) == 0:
            heapq.heappop(min_heap)
        
        if max_heap and min_heap:
            max_val = -max_heap[0]
            min_val = min_heap[0]
            results.append(f"{max_val} {min_val}")
        else:
            results.append("EMPTY")
        
        index += 1
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
