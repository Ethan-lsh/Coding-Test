# Author: Sanghyeon Lee
# Date: March 4, 2024
# Description: Practice for simulation of SWEA

"""
Condition.
1. 1초 동안, 미세먼지의 확산과 공기청정기의 작동이 일어난다.
1-1. 미세먼지는 동시에 모든 칸에서 확산된다. (미세먼지 확산 조건은 spread 함수에 있음)
2. 미세먼지의 확산이 끝나면, 공기청정기에서 바람이 나온다.
2-1. 공기청정기의 바람은 정해진 범위에서 정해진 방향을 타고 흐른다.
2-2. 바람의 영향을 받지 않는 격자의 모래는 그대로 있다.
3. 위의 두 과정이 T초 후에 끝났을 때, 남아있는 모래의 양은?

Solution.
1. 먼저 모래를 퍼뜨리는 함수 (def.spread)를 작성한다.
1-1. 다른 격자로 이동한 모래의 양을 저장하는 별도의 격자와 기존 격자의 복사본을 생성한다.
1-2. 위의 두 데이터를 사용해 모래가 이동했을 때 변화를 저장하고, 원본 격자를 업데이트한다.
2. 공기청정기를 작동시키는 함수를 작성한다.
2-1. 공기청정기는 위/아래 가 서로 다른 바람 방향을 가지기 때문에, 함수를 분리한다.
2-2. 바람의 방향은 좌표 이동 리스트를 생성하여 구현한다. (매우 중요!)
     바람의 방향이 바뀌는 조건은 다음 좌표가 격자의 범위를 벗어났을 때다.
3. 모든 움직임이 끝나면, 남아있는 모래 양을 구한다.
"""

import copy

R, C, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def spread():
    copy_board = copy.deepcopy(board)
    temp = [[0]*C for _ in range(R)]  # 날라간 모래를 저장
    # 모든 모래에 대해, 미세먼지 확산 조건을 처리
    for x, y in sand:
        amount = copy_board[x][y] // 5
        cnt = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                temp[nx][ny] += amount
                cnt += 1
        copy_board[x][y] -= amount * cnt

    for i in range(R):
        for j in range(C):
            board[i][j] = copy_board[i][j] + temp[i][j]

def wind_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    up = air_cleaner[0][0]
    x, y = up, 1
    while True:
        nx, ny = x + dx[direct], y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x, y = nx, ny

def wind_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    down = air_cleaner[1][0]
    x, y = down, 1
    while True:
        nx, ny = x + dx[direct], y + dy[direct]
        if x == down and y == 0 :
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        board[x][y], before = before, board[x][y]
        x, y = nx, ny


if __name__ == '__main__':
    # 모래가 있는 좌표 찾기
    for _ in range(T):
        sand = []
        air_cleaner = []
        for i in range(R):
            for j in range(C):
                if board[i][j] > 0 and board[i][j] != -1:
                    sand.append((i, j))
                elif board[i][j] == -1:
                    air_cleaner.append((i, j))
        spread()

        wind_up()
        wind_down()

    result = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                result += board[i][j]

    print(result)