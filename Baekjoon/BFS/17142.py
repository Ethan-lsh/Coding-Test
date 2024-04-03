# Author: Sanghyeon Lee
# Date: March 30, 2024
# Description: Practice for BFS of SWEA
import copy
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0 ,0)
dy = (0, 0, -1, 1)

result = 0

def comb(arr, n):
    tmp = []
    if n > len(arr):
        return tmp

    if n == 1:
        for i in arr:
            tmp.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                tmp.append([arr[i]] + j)

    return tmp

def bfs(case):
    global result
    # e_board = copy.deepcopy(board)

    visited = [[False] * N for _ in range(N)]
    time_table = [[-1]*N for _ in range(N)]

    viruses = copy.deepcopy(case)
    for x, y in viruses:
        time_table[x][y] = 0
        visited[x][y] = True

    while viruses:
        virus = viruses.pop(0)
        x, y = virus

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    time_table[nx][ny] = time_table[x][y] + 1
                    result = max(result, time_table[nx][ny])
                elif board[nx][ny] == 2:
                    time_table[nx][ny] = time_table[x][y] + 1
                viruses.append((nx, ny))
                visited[nx][ny] = True

    # value = max(max(row) for row in time_table)
    # result = min(result, value)

if __name__ == '__main__':
    # Find the virus location
    position = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                position.append((i, j))

    cases = comb(position, M-1)
    for case in cases:
        bfs(case)

    print(result)