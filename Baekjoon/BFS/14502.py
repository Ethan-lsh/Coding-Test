# Author: Sanghyeon Lee
# Date: March 25, 2024
# Description: Practice for BFS of SWEA

"""
Condition.
1. 바이러스의 전파를 멈추기 위해, 3곳에 벽을 세워야 한다.
2. 바이러스는 '상하좌우' 인접한 한 칸으로 이동 가능.

Solution.
1. 바이러스를 모두 퍼졌을 때, 빈칸을 체크해야 함 -> BFS
2. 벽을 3 곳 세웠을 때, BFS를 실행하는 구조
   => 벽을 세울 수 있는 모든 경우의 수에 대해 탐색해야 함
3. 원본 격자 데이터를 유지하기 위해 'deepcopy'를 사용함
"""
import copy
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

result = 0

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt+1)
                board[i][j] = 0

def bfs():
    q = deque([])
    
    # NOTE
    # BFS가 실행될 때마다, board는 초기값을 유지해야 함.
    # Deepcopy를 통해 초기 값을 유지
    extra_board = copy.deepcopy(board)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and extra_board[nx][ny] == 0:
                extra_board[nx][ny] = 2
                q.append((nx, ny))

    global result
    count = 0

    for i in range(N):
        count += extra_board[i].count(0)

    result = max(result, count)


make_wall(0)
print(result)


