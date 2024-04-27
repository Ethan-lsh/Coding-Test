# Author: Sanghyeon Lee
# Date: April 27, 2024
# Description: Practice for SWEA


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # If N == 1
    if N == 1:
        print(f"#{test_case}")
        print(1)
        continue

    # If N > 1
    triangle = [[1]]
    for n in range(1, N):
        # 두 번째 줄의 경우, 연산을 없애고 간단히 출력
        if n + 1 == 2:
            triangle.append([1, 1])
            continue

        # 줄이 3개를 넘어가는 경우
        line = [0] * (n + 1)
        line[0] = line[-1] = 1

        # 이전 줄의 값을 참조하여 새로운 리스트를 생성
        for i in range(1, n):
            line[i] = triangle[n - 1][i-1] + triangle[n - 1][i]
        triangle.append(line)

    print(f"#{test_case}")
    for row in triangle:
        print(*row)

