# Author: Sanghyeon Lee
# Date: April 4, 2024
# Description: Practice for SWEA D3

for _ in range(1, 11):
    test_case = int(input())
    arr = list(map(int, input().split()))

    while True:
        for weight in range(1, 6):
            first = arr.pop(0) - weight  # 첫번째 요소 값 변경
            if first < 0 or first == 0:  # 0보다 작거나 같으면 for 문을 탈출
                first = 0
                arr.append(first)
                break
            arr.append(first)  # 그렇지 않다면 그대로 진행
        if arr[-1] == 0:  # while 문을 탈출 구문
            break

    print(f"#{test_case} {' '.join(map(str, arr))}")