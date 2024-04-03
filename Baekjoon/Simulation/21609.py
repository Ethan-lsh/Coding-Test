# Author: Sanghyeon Lee
# Date: March 10, 2024
# Description: Practice for Simulation and BFS
# Code refer: https://jennnn.tistory.com/68

"""
Condition
1. -1:검은색; 0:무지개; 1~M:일반
2. 블록 그룹: 일반 블록 >= 1, 일반 블록은 모두 같은 색; 무지개 블록은 개수 상관 x; 검은색 블록은 안됌
3. 그룹에 속한 블록의 개수 >= 2; 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 모든 칸으로 이동 가능해야 함
4. 블록 그룹 기준: 행 -> 열

"""
from collections import deque

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs(block: list, color):
    q = deque()
    q.append(block)

    block_cnt, rainbow_cnt = 1, 0 # 일반 블록, 무지개블록 갯수
    blocks, rainbows = [block], []  # 일반 블록, 무지개블록 좌표 저장 리스트

    while q:
        x, y = q.popleft()
        # 현재 칸에 대한 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not selected[nx][ny] and table[nx][ny] == color:
                selected[nx][ny] = True  # 방문 처리
                q.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])
            if 0 <= nx < N and 0 <= ny < N and not selected[nx][ny] and table[nx][ny] == 0:
                selected[nx][ny] = True
                q.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # NOTE: 무지개 블록은 다른 그룹에 속할 수도 있으니 방문처리 해제
    for x, y in rainbows:
        selected[x][y] = False

    return [block_cnt, rainbow_cnt, blocks+rainbows]


def remove(block):
    global table
    for x, y in block:
        table[x][y] = -2


def gravity():
    global table
    for i in range(N-1, -1, -1):
        for j in range(N):
            if table[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < N and table[r+1][j] == -2: # 다음행이 범위 안이고, 폭파된 블록이면
                        table[r+1][j] = table[r][j]
                        table[r][j] = -2 # 블록이 없어진 이전 자리는 -2로 채운다
                        r += 1
                    else:
                        break

def rotate():
    global table
    new_table = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_table[N-1-j][i] = table[i][j]
    return new_table

score = 0
while True:
    selected = [[False] * N for _ in range(N)]  # 방문 여부 체크  변수
    blocks = []
    #1. 테이블의 각 요소에 접근, 일반 블록을 찾으면 해당 블록을 그룹의 색으로 설정함
    for i in range(N):
        for j in range(N):
            if table[i][j] > 0 and not selected[i][j]: # 일반 블록이고 방문 안함
                selected[i][j] = True  # 망문 처리
                block_info = bfs([i, j], table[i][j])
                if block_info[0] >= 2:
                    blocks.append(block_info)

    blocks.sort(reverse=True)

    if not blocks:
        break

    #블록 제거
    # blocks[0] -> 제일 큰 블록 그룹, blocks[0][2] -> 그룹 블록들 좌표
    remove(blocks[0][2])
    score += blocks[0][0]**2

    #중력
    gravity()

    table = rotate()

    gravity()

print(score)


