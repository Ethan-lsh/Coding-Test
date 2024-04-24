# Author: Sanghyeon Lee
# Date: April 12, 2024
# Description: Practice for dx/dy technique of SWEA
import copy
import sys
sys.stdin = open("./input.txt", "r")

"""
Condition.
1. 술래는 '달팽이 회전'으로 주어진 격자를 이동한다.
   격자의 중앙에서 출발하고, (1,1)에 도착하면 회전하는 방향을 반전한다.
2. 도망자는 술래와의 거리가 3이하인 경우에만 이동한다.
3. 점수는 't번 턴 * 잡힌 도망자 수'를 합산한다.

Solution.
1. 달팽이 움직임을 구현하는 것이 핵심. 나머지는 구현이 쉽다.
1-1. 최대 움직임 횟수, 현재 움직임 횟수, 방향 전환 flag, 이동량 (+1 or -1)
1-2. '현재 움직임 횟수 == 최대 움직임 횟수'이면, 현재 움직임 횟수를 초기화 하고 방향을 바꾼다.
1-2-1. If 'flag == 0', 'flag = 1' 로 변경
1-2-2. If 'flag == 1', 'flag = 0' 로 변경 과 동시에 '최대 움직임 횟수+1'
       즉, 초기 flag를 0으로 시작하고 flag가 두번 바뀌면 최대 움직임 횟수가 1 증가하는 구조
1-3. 만약, 다음 좌표가 (1,1) 또는 중앙에 도착하는 경우
1-3-1. 현재 움직임 횟수, 방향 전환 flag를 0으로 초기화, 최대 움직임 횟수는 격자 범위 따라 조절.
       이동량은 역회전 시 -1, 정회전 시 +1
1-4. 나머지는 구현이 쉽다.  
"""

# 상, 우, 하, 좌
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

n, m, h, K = map(int, input().split())

# board = [[0] * (n + 1) for _ in range(n + 1)]

CENTER_X = n // 2 + 1
CENTER_Y = n // 2 + 1

GOAL = (1, 1)

police = [CENTER_X, CENTER_Y]

runner = []  # 도망자
for i in range(1, m + 1):
    x, y, d = map(int, input().split())
    runner.append([i, x, y, d])

trees = [list(map(int, input().split())) for _ in range(h)]


def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


###################
# 달팽이 움직임 구현 #
###################
mx_cnt, cnt, flag, val = 1, 0, 0, 1
td = 0  # 술래의 방향
def check_route():
    global mx_cnt, cnt, flag, val, td

    cnt += 1
    pnx, pny = police[0] + dx[td], police[1] + dy[td]
    if (pnx, pny) == GOAL:
        mx_cnt, cnt, flag, val = n, 1, 1, -1
        td = 2   # 방향을 아래 방향으로 변경
    elif (pnx, pny) == (CENTER_X, CENTER_Y):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if cnt == mx_cnt:
            cnt = 0
            td = (td + val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    police[0], police[1] = pnx, pny

def move_runner():
    # 거리가 3이하인 도망자
    for man in runner:
        gap = abs(police[0] - man[1]) + abs(police[1] - man[2])
        if gap <= 3:
            nx, ny = man[1] + dx[man[3]], man[2] + dy[man[3]]

            # 격자 범위 안
            if in_range(nx, ny):
                if [nx, ny] == police:
                    continue
                else:
                    man[1], man[2] = nx, ny
            else:
                ndir = (man[3] + 2) % 4
                tx, ty = man[1] + dx[ndir], man[2] + dy[ndir]
                if [tx, ty] == police:
                    continue
                else:
                    man[1], man[2], man[3] = tx, ty, ndir


def move_police():

    check_route()

    # 시야 내에 있는 범인을 추적
    global runner
    cp_runner = copy.deepcopy(runner)
    catch = 0
    for i in range(3):
        catch_x, catch_y = police[0] + dx[td]*i, police[1] + dy[td]*i
        for man in cp_runner:
            cp_idx = man[0]
            if (man[1], man[2]) == (catch_x, catch_y) and [catch_x, catch_y] not in trees:
                catch += 1
                cp_runner = [sublist for sublist in cp_runner if cp_idx != sublist[0]]

    runner = cp_runner

    return catch

def simulate(t):
    # 1. m 명이 도망자가 먼저 동시에 움직임
    move_runner()

    # 2. 술래가 움직임
    catched_man = move_police()

    global ans
    ans += t * catched_man

ans = 0
for t in range(1, K+1):
    simulate(t)

print(ans)