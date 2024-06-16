# Author: Sanghyeon Lee
# Date: June 16, 2024
# Description: Practice for Softeer, L2
import copy
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs(r, c):
    q = deque([[r, c]])
    visited[r][c] = True

    count = 1  # 블록에 속하는 장애물 개수
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1:
                count += 1
                visited[nx][ny] = True
                q.append([nx, ny])

    return count

if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    visited = [[False]*N for _ in range(N)]
    cp_board = copy.deepcopy(board)

    result = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1 and not visited[x][y]:
                # bfs가 끝나면 새로운 블록이 시작
                result.append(bfs(x, y))

    print(len(result))
    for ans in sorted(result):
        print(ans)