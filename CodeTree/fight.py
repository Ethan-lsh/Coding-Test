# Author: Sanghyeon Lee
# Date: April 10, 2024
# Description: Practice for simulation of SWEA (싸움땅 문제)
import copy
import sys
sys.stdin = open("./input.txt", "r")

n, m, k = map(int, input().split())

player = [[0, 0]] * (m+1)
stat = [0] * (m+1)
direction = [0] * (m+1)
gun = [0] * (m+1)
gun_list = [[[0] for _ in range(n+1)] for _ in range(n+1)]
score = [0] * (m+1)

board = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    board[i][1:] = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] > 0:
            gun_list[i][j]= [board[i][j]]

player_board = [[0] * (n+1) for _ in range(n+1)]


for idx in range(1, m+1):
    x, y, d, s = map(int, input().split())
    player[idx] = [x, y]
    player_board[x][y] = idx
    direction[idx] = d
    stat[idx] = s

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

pair_direction = {0:2, 1:3, 2:0, 3:1}

def is_inrange(x, y):
    return 1 <= x <= n and 1 <= y <= n

def check_gun(x, y, idx):
    # global gun
    player_gun = gun[idx]
    gun_list[x][y].append(player_gun)
    gun_list[x][y].sort(reverse=True)
    gun[idx] = gun_list[x][y][0]
    gun_list[x][y].pop(0)


def update_position():
    global player_board
    # temp = copy.deepcopy(player_board)
    temp = [[0] * (n+1) for _ in range(n+1)]
    for idx in range(1, m+1):
        temp[player[idx][0]][player[idx][1]] = idx
    player_board = temp

def losser_move(nr, nc, losser):
    # lx, ly = 0, 0
    for i in range(4):
        losser_dir = (direction[losser] + i) % 4
        lx, ly = nr + dx[losser_dir], nc + dy[losser_dir]
        if not is_inrange(lx, ly) or player_board[lx][ly] > 0:
            while True:
                losser_dir = (losser_dir + 1) % 4
                lx, ly = nr + dx[losser_dir], nc + dy[losser_dir]
                if is_inrange(lx, ly) and player_board[lx][ly] == 0:
                    gun_list[lx][ly].append(gun[losser])
                    gun[losser] = 0
                    check_gun(lx, ly, losser)
                    player[losser] = [lx, ly]
                    direction[losser] = losser_dir
                    break


def simulation():
    for id in range(1, m+1):
        r, c = player[id]
        nr, nc = r + dx[direction[id]], c + dy[direction[id]]

        if not is_inrange(nr, nc):  # 범위 밖이면 방향을 전환
            # direction[id] = (direction[id] + 2) % 2
            direction[id] = pair_direction[direction[id]]
            nr, nc = r + dx[direction[id]], c + dy[direction[id]]

        # 이동한 자리에 player가 없고 총이 있는 경우
        if player_board[nr][nc] == 0:
            check_gun(nr, nc, id)
            player[id] = [nr, nc]
            update_position()
        
        # 이동한 자리에 player가 있는 경우
        if player_board[nr][nc] > 0:
            comp_id = player_board[nr][nc]

            origin = stat[id] + gun[id]
            another = stat[comp_id] + gun[comp_id]

            if (origin, stat[id]) > (another, stat[comp_id]):
                score[id] += origin - another
                losser_move(nr, nc, comp_id)

                check_gun(nr, nc, id)
                player[id] = [nr, nc]
            else:
                score[comp_id] += another - origin
                losser_move(nr, nc, id)

                check_gun(nr, nc, comp_id)
                player[comp_id] = [nr, nc]

            # 패배자 케이스

            # break

            # # 승자 케이스
            # check_gun(nr, nc, winner)
            # player[winner] = [nr, nc]

            update_position()

for _ in range(k):
    simulation()
print(player_board)

for i in range(1, m+1):
    print(f"{score[i]}", end=' ')