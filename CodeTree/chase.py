# Author: Sanghyeon Lee
# Date: April 12, 2024
# Description: Practice for dx/dy technique of SWEA
import copy
import sys
sys.stdin = open("./input.txt", "r")

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

right = ((-1, 0), (0, 1), (1, 0), (0, -1))
reverse = ((1, 0), (0, 1), (-1, 0), (0, -1))

n, m, h, K = map(int, input().split())

# board = [[0] * (n + 1) for _ in range(n + 1)]

CENTER_X = n // 2 + 1
CENTER_Y = n // 2 + 1

GOAL = (1, 1)

police = [CENTER_X, CENTER_Y]
p_move = [0, 0, 1, 0]   # [방향, 방향 전환 횟수, 움직여야 하는 거리, 움직인 거리]

runner = []  # 도망자
for i in range(1, m + 1):
    x, y, d = map(int, input().split())
    runner.append([i, x, y, d])

trees = [list(map(int, input().split())) for _ in range(h)]


def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

def check_route(flipped):
    global p_move
    pdir, pturn, prange, pcnt = p_move[0], p_move[1], p_move[2], p_move[3]

    pcnt += 1  # 이동 횟수를 + 1

    # if not flipped:
    if pcnt == prange:  # 움직여야하는 칸을 다 채운경우 방향을 전환
        pdir = (pdir + 1) % 4
        pturn += 1
        pcnt = 0

    if pturn == 2:  # 방향을 두번 전환 했으면, 움직여야 하는 칸을 + 1
        pturn = 0
        prange = prange + 1 if not flipped else prange - 1
        # if prange >= n: prange = n-1

    p_move = [pdir, pturn, prange, pcnt]

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
                    man[1], man[2] = tx, ty

    # init police move info
    # p_move[-1] = 0


flip = False
direction = right
def move_police():
    global flip, runner, direction, p_move
    pnx, pny = police[0] + direction[p_move[0]][0], police[1] + direction[p_move[0]][1]

    if (pnx, pny) == (1, 1):
        flip = True
        direction = reverse
        p_move = [0, 0, n-1, 0]

    if (pnx, pny) == (CENTER_X, CENTER_Y):
        flip = False

    check_route(flip)

    police[0], police[1] = pnx, pny

    # police = [pnx, pny]

    # 시야 내에 있는 범인을 추적
    cp_runner = copy.deepcopy(runner)
    catch = 0
    for i in range(3):
        catch_x, catch_y = police[0] + dx[p_move[0]]*i, police[1] + dy[p_move[0]]*i
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