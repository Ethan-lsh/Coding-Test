# Author: Sanghyeon Lee
# Date: March 21, 2024
# Description: Practice for simulation of SWEA

import sys

sys.stdin = open("../input.txt", "r")

from collections import deque

# 격자 크기, 상어 수, 냄새 지속 시간
N, M, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[[0, 0]] * N for _ in range(N)]  # [방문한 상어 번호, 남은 냄새 시간]

direction = list(map(int, input().split()))  # 처음 상어가 바라보는 위치

# 우선순위
rule = []
for i in range(M):
    rule.append([list(map(int, input().split())) for _ in range(4)])

# 4방 탐색 우선순위
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def update_smell():
    # 격자 내 모든 상어의 냄새 값을 1 줄인다.
    global visited
    for i in range(N):
        for j in range(N):
            if visited[i][j][1] != 0:
                visited[i][j][1] -= 1
            else:
                visited[i][j] = [0, 0]

result = 0
def exec():
    global result
    while True:
        global shark_info
        s_nx, s_ny, s_nd = -1, -1, -1  # next shark position

        for sn, sx, sy in shark_info:
            if sn == 0:
                continue
            no_smell = []
            same_smell = []
            for d in range(4):
                s_nx, s_ny = sx + dx[d], sy + dy[d]
                if 0 <= s_nx < N and 0 <= s_ny < N:
                    if visited[s_nx][s_ny][0] == 0:  # no shark at next position
                        no_smell.append((s_nx, s_ny, d))
                    elif visited[s_nx][s_ny][0] == sn:  # shark with same smell
                        same_smell.append((s_nx, s_ny, d))

            no, same = len(no_smell), len(same_smell)
            if no:
                s_nx, s_ny, s_nd = no_smell[0]
            else:
                if same == 1:
                    s_nx, s_ny, s_nd = same_smell[0]
                else:
                    priority: list = rule[sn-1][direction[sn-1]]
                    sorted_list = sorted(zip(same_smell, priority), key=lambda x: x[1])
                    s_nx, s_ny, s_nd = sorted_list[0][0]

            ## update next position
            direction[sn-1] = s_nd
            visited[s_nx][s_ny] = [sn, k]
            shark_info[sn-1] = [sn, s_nx, s_ny]

            # update shark
            # if board[s_nx][s_ny] > 0 and board[s_nx][s_ny] < sn:
            if 0 < board[s_nx][s_ny] < sn:
                shark_info[sn-1] = [0, -1, -1]

            # update shark location
            board[sx][sy] = 0
            board[s_nx][s_ny] = sn

        # update smell
        update_smell()

        result += 1

        # 1번 상어만 남는다면 break
        if shark_info[0][0] == 0:
            print(result)
            break


if __name__ == '__main__':

    shark_info: list = [0] * M  # [상어 번호, x, y]

    # 초기 모든 상어의 현재 위치를 파악
    s_x, s_y = -1, -1
    for m in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if board[i][j] == m:
                    s_x, s_y = i, j
                    shark_info[m-1] = [m, s_x, s_y]
                    visited[s_x][s_y] = [m, k]
                    break
        if s_x == -1 or s_y == -1:
            continue

    exec()