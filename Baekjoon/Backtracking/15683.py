# Author: Sanghyeon Lee
# Date: April 1, 2024
# Description: Practice for backtracking of SWEA

"""
Condition.
1. CCTV는 총 5 종류가 있고, 각 CCTV마다 감시할 수 있는 방향이 다르다.
2. CCTV는 90도 방향 회전이 가능하다.
3. CCTV는 벽을 통과할 수 없다. 대신, 다른 CCTV는 통과할 수 있다.

Solution.
1. CCTV의 종류별 탐색 가능한 경우의 수를 저장한다.
2. CCTV를 각각 회전 시킬 수 있는 경우의 수를 DFS로 검색 (회전은 서로 독립적이다)
'Ex) 1번 CCTV는 정지, 2번 CCTV는 회전 할 수 있다.'
2-1. 현재 좌표에 존재하는 모든 카메라의 번호와 좌표를 저장할 'camera: list' 를 생성
2-2. 'level' 변수를 사용해 모든 카메라를 탐색
2-3. 각 레벨에 해당하는 카메라는 자신이 감시 할 수 있는 방향좌표 리스트를 갖는다.
     따라서, 각 방향 좌표 리스트를 반복문을 통해 level을 올려가며 모든 경우의 수를 체크해야 함.
3. 방향이 정해졌을 때, 방향이 일치하는 격자 내 모든 좌표를 검색해야 한다.
3-1. While 문을 통해, 범위를 벗어나기 전까지 계속 이동시킨다.
4. Level이 camera list의 끝에 위치하면, 사각지대 갯수를 구한다.
"""

import copy
from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

# 0: 빈칸; 6:벽; 1~5:CCTV
board = [list(map(int, input().split())) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)

# 각 CCTV가 탐색할 수 있는 방향
# 각 값은 (dx, dy)의 index를 가리킨다
camera1 = [[0], [1], [2], [3]]
camera2 = [[2, 3], [0, 1]]
camera3 = [[0, 3], [0, 2], [1, 2], [1, 3]]
camera4 = [[0, 2, 3], [0, 1, 2], [1, 2, 3], [0, 1, 3]]
camera5 = [[0, 1, 2, 3]]

# cctv 딕셔너리
CCTV = {1: camera1, 2: camera2, 3: camera3, 4: camera4, 5: camera5}

def check(nx, ny):
    return nx < 0 or nx >= N or ny < 0 or ny >= M

def move(x, y, direction, board_copy):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if check(nx, ny) or board_copy[nx][ny] == 6:
                break
            if board_copy[nx][ny] != 0:
                continue
            board_copy[nx][ny] = '#'

def check_zero(board_copy):
    global result
    count = 0
    for row in board_copy:
        count += row.count(0)
    result = min(result, count)


def dfs(level, board):
    board_copy = copy.deepcopy(board)

    if level == len(camera):
        check_zero(board_copy)
        return

    camera_num, x, y = camera[level]

    for d in CCTV[camera_num]:
        move(x, y, d, board_copy)
        dfs(level + 1, board_copy)
        board_copy = copy.deepcopy(board)


if __name__ == '__main__':
    result = 0
    camera = deque([])
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and board[i][j] != 6:
                camera.append((board[i][j], i, j))
            if board[i][j] == 0: result += 1

    dfs(0, board)
    print(result)
