# Author: Sanghyeon Lee
# Date: June 9, 2024
# Description: Practice for Softeer


import sys
from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def dfs(depth, current_score):
    global ans, visited

    # 모든 인원이 3칸을 이동했을 때, dfs 종료
    if depth == 3:
        ans = max(ans, current_score)
        return

    _next = []
    for _ in range(len(player)):
        p_x, p_y = player.popleft()
        visited[p_x][p_y] = True          # 현재 위치 방문 처리
        current_score += board[p_x][p_y]  # 현재 있는 위치의 열매 점수를 더함
        # 4방향 탐색
        for d in range(4):
            nx, ny = p_x + dx[d], p_y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:  # 격자 범위 안
                if not visited[nx][ny]:
                    _next.append([nx, ny])


    dfs(depth + 1, current_score)

    # dfs(time + 1, current_score)


if __name__ == '__main__':
    sys.stdin = open("L2/input.txt", "r")

    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]

    player = deque([])

    ans = 1e2
    init_score = 0
    for _ in range(m):
        x, y = map(int, input().split())
        init_score += board[x-1][y-1]
        player.append([x - 1, y - 1])

    for depth in range(3):
        dfs(depth, init_score)

    print(ans)
