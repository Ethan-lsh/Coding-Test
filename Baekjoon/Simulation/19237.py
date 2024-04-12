# Author: Sanghyeon Lee
# Date: March 21, 2024
# Description: Practice for simulation of SWEA

import sys
sys.stdin = open("../input.txt", "r")

from collections import deque

# 격자 크기, 상어 수, 냄새 지속 시간
N, M, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]  # [방문한 상어 번호, 남은 냄새 시간]

direction = ["empty"] + list(map(int, input().split()))  # 상어가 바라보는 위치

rule = ["empty"]
for i in range(M):
    rule.append([list(map(int, input().split())) for _ in range(4)])

# 4방 탐색 우선순위
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

shark_info = [0] * (M+1)

# 초기 모든 상어의 현재 위치를 파악
s_x, s_y = -1, -1
for n in range(1, 5):
    for i in range(N):
        for j in range(N):
            if board[i][j] == n:
                s_x, s_y = i, j
                shark_info[n] = [s_x, s_y]
                visited[s_x][s_y] = [n, k]
    if s_x == -1 or s_y == -1:
        break

def remove_smell():
    # 격자 내 모든 상어의 냄새 값을 1 줄인다.
    global visited
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0 and visited[i][j][1] > 0:
                visited[i][j][1] -= 1
            else:
                visited[i][j] = 0

def four_way_search(sx, sy, sn):
    no_smell = []
    same_smell = []

    for d in range(4):
        s_nx, s_ny = sx + dx[d], sy + dy[d]
        if 0 <= s_nx < N and 0 <= s_ny < N:
            if not visited[s_nx][s_ny]:  # 격자 범위 안이고 무취인 칸이 있을 때
                no_smell.append([s_nx, s_ny, d])
            elif visited[s_nx][s_ny][0] == sn:
                same_smell.append([s_nx, s_ny, d])
    return no_smell, same_smell

result = 0
while shark_info:
    # 모든 상어를 움직인다(4마리는 동시에 움직인다)
    for n in range(1, len(shark_info)):
        s_x, s_y = shark_info[n]
        
        # 인접한 칸 중, 무취인 칸을 탐색
        no_smell, same_smell = four_way_search(s_x, s_y, n)

        s_nx, s_ny, s_d = 0, 0, 0

        if no_smell:
            s_nx, s_ny, s_d = no_smell[0]
        else:
            if len(same_smell) == 1:
                s_nx, s_ny, s_d = same_smell[0]
            if len(same_smell) >= 2:
                shark_direction = direction[n]  # 현재 상어가 보는 방향에 맞는 우선순위를 찾는다
                for rd in rule[n][shark_direction]:
                    for smell in same_smell:
                        if smell[2] == rd:
                            s_nx, s_ny, s_d = smell
                            direction[n] = rd
                        else:
                            continue

        visited[s_nx][s_ny] = [n, k]
        shark_info[n] = [s_nx, s_ny]
        direction[n] = s_d

        board[s_x][s_y] = 0  # 이전 좌표의 상어 존재 여부는 0으로
        board[s_nx][s_ny] += 1  # 이동한 좌표의 상어정보
        
    # 곂치는 상어가 있는지 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2:  # 2마리 이상이 있다면
                indexes = [idx for idx, value in enumerate(shark_info) if value == [i, j]]
                visited[i][j] = [indexes.pop(0), k]
                for l in indexes:
                    shark_info.pop(l)

    remove_smell()

    if len(shark_info) <= 2:
        break

    result += 1

print(result)










    













