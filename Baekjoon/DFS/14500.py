# Author: Sanghyeon Lee
# Date: March 19, 2024
# Description: Practice for dfs of SWEA

"""
Condition.
1. 주어진 격자위에 테트로미노 '한개'를 올려서 테트로미노를 구성하는 값의 최대를 구해야함.
2. 테트로미노는 4개의 정사각형으로 구성. 회전, 대칭이 가능하다.

Solution.
1. 'ㅜ' 모양 테트로미노를 제외한 나머지는 4번의 dfs 탐색으로 가능하다.
2. 'ㅜ' 모양 테트로미노를 찾기 위한 함수를 별도로 작성해야 함.
2-1) % 연산을 사용해, 현재 좌표에서 3방향 탐색을 진행
"""

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

maximum = 0

def dfs(i, j, dsum, cnt):
    global maximum

    if cnt == 4:
        maximum = max(maximum, dsum)
        return

    for d in range(4):
        ni, nj = i + dx[d], j + dy[d]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum+board[ni][nj], cnt+1)
            visited[ni][nj] = False


# ㅗ, ㅓ, ㅜ, ㅏ 모양을 확인하는 함수
def exec(i, j):
    global maximum
    for k in range(4):
        tmp = board[i][j]
        for l in range(3):
            t = (k+l)%4
            ni = i + dx[t]
            nj = j + dy[t]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]

        maximum = max(maximum, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exec(i, j)

print(maximum)




