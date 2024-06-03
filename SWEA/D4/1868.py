# Author: Sanghyeon Lee
# Date: June 3, 2024
# Description: Practice for SWEA D4
import sys
sys.stdin = open('./input.txt', "r")

from collections import deque

# 8방향 탐색
dx = (-1 ,-1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

## 클릭 후, 연쇄작용을 구현한 함수
# 클릭 후에, 8인접 좌표에서 다시 8인접 탐색이 발생하는 과정을 구현
# click()과 똑같이 지뢰가 하나라도 있으면 다음 좌표에 추가하지 않는다.
def bfs(lst):
    q = deque(lst)
    while q:
        x, y = q.popleft()
        board[x][y] = 'o'
        next_next_target = []

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == '.':
                    next_next_target.append((nx, ny))
                elif board[nx][ny] == '*':
                    break
        else:
            bfs(next_next_target)

## 클릭 여부를 체크하는 함수
# 현재 좌표에서 8인접 방향에 지뢰가 하나도 없을 때만 클릭한다.
# 만약, 지뢰가 하나라도 있으면 클릭하지 않는다.
def click(x, y):
    global ans

    next_target = []
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == '.':
                next_target.append((nx, ny))
            elif board[nx][ny] == '*':
                break
    else:
        # 지뢰가 주변에 하나도 없을 때
        if next_target:
            board[x][y] = 'o'
            ans += 1
            bfs(next_target)


## 퍼지지 않은 지점을 체크
# click 과 bfs 함수가 종료되면, 연쇄반응이 가능한 모든 점은 작동했기 때문에 가능하다.
def rest():
    global ans
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                ans += 1


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    board = [list(input()) for _ in range(N)]

    ans = 0  # 최소 클릭 횟수

    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                click(i, j)

    rest()

    print(f"#{test_case} {ans}")
