# Author: Sanghyeon Lee
# Date: June 9, 2024
# Description: Practice for Softeer


import sys
from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def solve():
    global ans
    visited = [[False] * n for _ in range(n)]
    for t in range(3):
        for _ in range(len(player)):
            p_x, p_y = player.popleft()
            print('init', p_x, p_y)
            current_score = 0  # 수확한 열매 스코어
            # 4방향 탐색
            for d in range(4):
                nx, ny = p_x + dx[d], p_y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:  # 격자 범위 안
                    # 방문하지 않았고, 점수가 현재 점수보다 높을 때
                    if not visited[nx][ny] and board[nx][ny] > current_score:
                        p_x, p_y = nx, ny
                        current_score = board[nx][ny]
            print('move', p_x, p_y)
            print()
            visited[p_x][p_y] = True
            player.append([p_x, p_y])

            ans += current_score  # 현재 최대 스코어를 더함


if __name__ == '__main__':
    sys.stdin = open("./input.txt", "r")

    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    player = deque([])

    for _ in range(m):
        x, y = map(int, input().split())
        player.append([x - 1, y - 1])

    print(player)
    ans = 0
    solve()
    print(ans)
