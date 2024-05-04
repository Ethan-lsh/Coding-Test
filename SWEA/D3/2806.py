# Author: Sanghyeon Lee
# Date: May 4, 2024
# Description: Practice for SWEA D3

# 현재 행까지 모든 열과 대각선에 위치한 값을 체크하기 위한 함수
def adjacent(x):
    for i in range(x):
        # row[i]의 값은 x 행의 column 값과 같다
        # x - i == row[x] - row[i]; '행 - 행 == 열 - 열' 이면 같은 대각선에 있다.
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    row = [0] * N
    result = 0

    dfs(0)

    print(f"#{tc} {result}")