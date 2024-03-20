# Author: Sanghyeon Lee
# Date: March 20, 2024
# Description: Practice for BFS of SWEA
# Code refer: https://resilient-923.tistory.com/357

"""
Condition.
1. 아기상어는 4방향 탐색이 가능. 1초에 1칸을 움직인다.
2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
3. 1마리 보다 많다면, 가장 가까운 물고기를 먹으러 간다.
3-1) 거리는 물고기가 있는 곳 까지 이동할 때, 지나는 칸의 최소 개수
3-2) 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면,
     가장 왼쪽에 있는 물고기를 먹는다.
4. 엄마상어에게 도움을 요청하기 전까지 걸리는 시간은?

Solution.
1. 시간 == 이동거리
2. 이동이 가능한 장소를 모두 큐에 저장
3. 거리가 같은 물고기는 정렬을 사용해 우선순위를 구현
4. 방문한 곳은 0으로 변경.
"""

from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

result = 0 # 잡아먹은 물고기 수

# 시계방향
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs(i, j, shark_size):
    global board, result
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    tmp = []
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dx[d], c + dy[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if board[nr][nc] <= shark_size:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[r][c] + 1
                    if board[nr][nc] < shark_size and board[nr][nc] != 0:
                        tmp.append((nr, nc, distance[nr][nc]))

    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

if __name__ == '__main__':
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
               x, y = i, j

    cnt = 0
    size = 2
    while 1:
        shark = bfs(x, y, size)

        if len(shark) == 0:
            break

        nx, ny, dist = shark.pop()
        result += dist
        board[x][y], board[nx][ny] = 0, 0
        x, y = nx, ny

        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0

    print(result)