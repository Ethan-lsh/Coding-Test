# Author: Sanghyeon Lee
# Date: March 16, 2024
# Description: Practice for simulation of SWEA
# Code refer: https://yeon-code.tistory.com/94
"""
Condition.
1. 가운데 칸의 모래 양은 0
2. 모래바람의 이동 방향
2-1) 1번 이동하면, 진행 방향은 반시계 방향으로 바뀜
2-2) 2번 이동하면, 이동거리가 2배가 된다.

Solution.
1. 비율과 해당 비율이 y로 부터 위치좌표를 저장하는 정방향 진행 배열을 생성
2. 정방향 배열을 사용해 남은 세 방향에 대한 행렬 생성
3. 현재 좌표는 (dx, dy)를 사용해 이동, 각 좌표에서 모래의 변화량을 체크
"""


N = int(input())

desert = [list(map(int, input().split())) for _ in range(N)]

# 위치 'y'에서 (행, 열, 비율) 의 위치를 저장한 배열
left_ratio = [[-2, 0, 0.02],
              [2, 0, 0.02],
              [-1, -1, 0.1],
              [-1, 0, 0.07],
              [-1, 1, 0.01],
              [1, -1, 0.1],
              [1, 0, 0.07],
              [1, 1, 0.01],
              [0, -2, 0.05],
              [0, -1, 0]]

right_ratio = [(x, -y, z) for x, y, z in left_ratio]
down_ratio = [(-y, x, z) for x, y, z in left_ratio]
up_ratio = [(-x, y, z) for x, y, z in down_ratio]

rate = {'left': left_ratio, 'right': right_ratio,
        'down': down_ratio, 'up': up_ratio}

now = [N//2, N//2]  # 현재 (x, y)

answer = 0
def move(cnt, dx, dy, direction):
    """
    모래를 흩날리는 함수
    :param cnt: 토네이도가 이동한 횟수 (이동 범위)
    :param dx: delta x
    :param dy: delta y
    :param direction: 토네이도 이동 방향
    :return:
    """
    global answer
    for _ in range(cnt+1):
        now[0], now[1] = now[0] + dx, now[1] + dy
        if now[0] < 0 or now[1] < 0:
            break

        spreads = 0   # 퍼진 모래 누적값
        for dx, dy, r in rate[direction]:
            nx, ny = now[0] + dx, now[1] + dy
            if r == 0:  # 퍼지지 않는 모래들은 현재 자리에 누적
                sand = desert[now[0]][now[1]] - spreads
            else:
                sand = int(desert[now[0]][now[1]] * r)

            if 0 <= nx < N and 0 <= ny < N:
                desert[nx][ny] += sand
            else:
                answer += sand
            spreads += sand

for i in range(N):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')

print(answer)


