# Author: Sanghyeon Lee
# Date: March 20, 2024
# Description: Practice for backtracking of SWEA
# Code refer: https://developer-ellen.tistory.com/68

"""
Condition.
1. 1x1 격자에 있는 물고기는 사이즈, 방향 데이터를 갖는다.
2. 격자에 있는 모든 물고기의 이동이 종료되면, 상어는 현재 방향에 따라 이동하며 먹을 수 있는 물고기를 먹는다.
3. 상어가 물고기를 먹으면, 사이즈가 1 증가한다.

Solution.
1. 먼저, 물고기를 이동시킨 다음 상어를 움직인다.
2. 물고기 번호가 작은 순서부터 이동할 수 있도록, for 반복문을 1~17까지 범위를 지정해 현재 번호에 맞는 물고기를 격자로 부터 찾는다.
2-1) 물고기를 찾으면 방향이 가리키는 값과 위치를 바꾼다.
3. 모든 물고기의 이동이 끝나면 상어를 이동시킨다.
"""


import copy
from collections import deque

board = [[None]*4 for _ in range(4)]
# visited = [[-1]*4 for _ in range(4)]  # 상어가 방문한 곳을 표시

N = 4

for i in range(4):
    k = 0
    row = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = row[k:k+2]
        board[i][j][1] -= 1
        k += 2

# 방향 순서, 1, 2, 3,...
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < N and 0 <= ny < N) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d] * i
        ny = sy + dy[s_d] * i
        if (0 <= nx < N and 0 <= ny < N) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)


