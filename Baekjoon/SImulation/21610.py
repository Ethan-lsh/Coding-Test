# Author: Sanghyeon Lee
# Date: March 10, 2024
# Description: Practice for simulation
from collections import deque

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

move_info = [list(map(int, input().split())) for _ in range(M)]

# 시계방향
dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
# 대각선
ddx = (-1, -1, 1, 1)
ddy = (-1, 1, 1, -1)

# 초기 구름 위치 좌표
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


for direction, step in move_info:
    move_clouds = []
    # 1~3
    for x, y in clouds:
        move_x, move_y = dx[direction-1]*step, dy[direction-1]*step

        nx = (x + move_x) % N
        ny = (y + move_y) % N

        table[nx][ny] += 1
        move_clouds.append([nx, ny])

    #4
    for x, y in move_clouds:
        cnt = 0
        for k in range(4):
            nx, ny = x + ddx[k], y + ddy[k]
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            elif table[nx][ny] > 0: cnt += 1

        table[x][y] += cnt
            # if 0 <= nx < N and 0 <= ny < N and table[nx][ny] > 0:
            #     table[x][y] += 1

    #5
    # print('moved', move_clouds)
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if (i, j) in move_clouds or table[i][j] < 2:
                continue
            table[i][j] -= 2
            new_clouds.append((i, j))

    print('new', new_clouds)
    clouds = new_clouds

# 결과
result = 0
for i in range(N):
    for j in range(N):
        result += table[i][j]

print(result)
# print(result)