# Author: Sanghyeon Lee
# Date: March 20, 2024
# Description: Practice for backtracking of SWEA
# Code refer: https://developer-ellen.tistory.com/68

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


