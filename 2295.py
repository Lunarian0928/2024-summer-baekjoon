def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    # 모든 가능한 두 수의 합을 저장
    two_sum = set()
    for i in range(n):
        for j in range(i, n):
            two_sum.add(arr[i] + arr[j])
    
    # 배열을 내림차순으로 정렬
    arr.sort(reverse=True)

    # 각 숫자에 대해 두 수의 합을 찾기
    for i in range(n):
        for j in range(i + 1, n):
            target = arr[i] - arr[j]
            if target in two_sum:
                print(arr[i])
                return

if __name__ == "__main__":
    main()