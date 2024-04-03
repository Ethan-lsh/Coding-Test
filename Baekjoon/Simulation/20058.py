# Author: Sanghyeon Lee
# Date: March 19, 2024
# Description: Practice for simulation and DFS for SWEA
"""
Condition.
1. 2^N 크기 격자 -> 2^L 크기의 부분 격자로 나눈다.
2. 모든 부분 격자를 시계 방향으로 90도 회전,
   이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸의 얼음의 양은 1이 줄어듬.
3. 남아있는 얼음의 합, 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수는?

Solution.
1. 부분 격자를 나누고, 회전 시키는 함수가 문제해결의 관건
2. 회전 후, 인접 칸 탐색은 이전과 동일하다.
3. 가장 큰 덩어리의 칸의 개수를 계산하기 위해 BFS를 사용한다.
"""


N, Q = map(int, input().split())
width = 2**N

board = [list(map(int, input().split())) for _ in range(2**N)] # 얼음 격자

L = list(map(int, input().split()))  # 시전 단계

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

## 부분 격자 생성
def remake(l):
    global board
    new_board = [[0] * width for _ in range(width)]

    r_size = 2**l
    for y in range(0, width, r_size):
        for x in range(0, width, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    ## NOTE: 격자를 회전시키는 코드
                    new_board[y+j][x+r_size -i -1] = board[y+i][x+j]

    board = new_board
    melting_list = []
    for y in range(width):
        for x in range(width):
            ice_count = 0
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or ny < 0 or nx >= width or ny >= width:
                    continue
                elif board[ny][nx] > 0:
                    ice_count += 1

            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))

    for y, x in melting_list:
        board[y][x] -= 1

def bfs():
    global board
    used = [[False]*width for _ in range(width)]
    ice_sum = 0
    max_area_count = 0
    for y in range(width):
        for x in range(width):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            from collections import deque
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx]
                area_count += 1

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= width or ny >= width or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count)

    print(ice_sum)
    print(max_area_count)

for l in L:
    remake(l)

bfs()


