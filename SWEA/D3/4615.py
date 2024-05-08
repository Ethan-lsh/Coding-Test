# Author: Sanghyeon Lee
# Date: May 8, 2024
# Description: Practice for SWEA D3

dyx = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

def init_board(n):
    table = [[0]*N for _ in range(N)]

    _centerX = _centerY = n//2 - 1
    # 처음 행
    table[_centerX][_centerY] = 2
    table[_centerX][_centerY+1] = 1
    # 다음 행
    table[_centerX+1][_centerY] = 1
    table[_centerX+1][_centerY+1] = 2

    return table


def search_8way(j, i, c):
    reverse = []  # 뒤집어야 하는 블록 좌표
    for d in range(8):  # 현재 지점에서 무조건 8-방향 탐색 수행
        dy, dx = dyx[d]
        ny, nx = j + dy, i + dx
        while True:
            # 범위 밖이면, reverse 리스트 초기화
            # 각 방향에 따라 reverse 리스트는 구분 되어야 한다
            if ny < 0 or nx < 0 or ny > N-1 or nx > N-1:
                reverse = []
                break
            # 다음 좌표가 0이면, reverse 리스트 초기화
            if board[nx][ny] == 0:
                reverse = []
                break
            # 같은 색 블록이면, while 탈출
            if board[nx][ny] == c:
                break
            # 다른 색 블록이면, reverse 리스트에 좌표 추가
            else:
                reverse.append((nx, ny))
            # 다음 좌표 업데이트
            nx, ny = nx + dx, ny + dy
        # 블록 뒤집기
        for rx, ry in reverse:
            if c == 1:
                board[rx][ry] = 1
            else:
                board[rx][ry] = 2
    # 현재 좌표도 업데이트
    board[i][j] = c

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    board = init_board(N)  # 보드 중심 블록 초기화

    # 1=black; 2=white
    chance = [list(map(int, input().split())) for _ in range(M)]  # (y, x), color

    for y, x, color in chance:
        search_8way(y-1, x-1, color)

    black_cnt, white_cnt = 0, 0
    for row in board:
        black_cnt += row.count(1)
        white_cnt += row.count(2)

    print(f"#{test_case} {black_cnt} {white_cnt}")
