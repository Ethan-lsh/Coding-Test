# Author: Sanghyeon Lee
# Date: May 28, 2024
# Description: Practice for SWEA D4

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def make_string(x, y, number):
    global result
    if len(number) == 7:
        result.append(number)
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            make_string(nx, ny, number + str(board[nx][ny]))


T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    result = []
    for x in range(len(board)):
        for y in range(len(board)):
            make_string(x, y, str(board[x][y]))

    print(f"#{test_case} {len(set(result))}")