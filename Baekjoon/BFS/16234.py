# Author: Sanghyeon Lee
# Date: April 3, 2024
# Description: Practice for BFS of SWEA

# import sys
# sys.stdin = open("input.txt", "r")

"""
Condition.
1. 각 나라와 인접한 나라와 인구 차가 (L<=, <=R) 을 만족하면 연합이라 한다.
2. 연합인 나라 사이에서만 인구이동이 발생한다.
3. 인구가 이동한 뒤, 연합의 인구수는 (연합의 모든 인구 수 // 연합 개수) 이다.
4. 총 몇 번의 인구이동이 발생하는가?

Solution.
1. BFS 알고리즘 사용.
2. 인접한 칸으로 확장하면서, 연합에 추가할 수 있는 나라인지 판별.
2-1. 연합 조건을 만족하면 연합 리스트에 추가 및 방문처리하고 다음 좌표로 추가. (큐 자료구조)
2-2. ? 만약 서로 겹치는 국경선이 없는 연합이 있다면? 또, 연합들 사이에 어디에도 속하지 않는 나라가 있다면?

"""

from collections import deque

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs(i, j):
    q = deque([])
    union = []
    q.append((i, j))
    union.append((i, j))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(board[x][y] - board[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))

    return union

if __name__ == '__main__':
    result = 0
    while True:
        visited = [[0] * N for _ in range(N)]
        flag = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = 1
                    country = bfs(i, j)

                    if len(country) > 1:
                        flag = 1
                        people = sum(board[x][y] for x, y in country) // len(country)

                        for x, y in country: board[x][y] = people

        if flag == 0:
            print(result)
            break

        result += 1