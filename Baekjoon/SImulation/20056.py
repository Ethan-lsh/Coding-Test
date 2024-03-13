# Author: Sanghyeon Lee
# Date: March 13, 2024
# Description: Practice for simulation of SWEA
"""
Condition.
1. 파이어볼은 인접한 8개 칸으로 이동 가능.
2. 이동이 끝난 뒤, 2개 이상의 파이어볼이 있을때 질량, 속도, 방향이 변한 새로운 파이어볼이 생성됨
3. K번 이동 후, 남아있는 파이어볼의 질량을 구해야 한다.

Solution.
1. 먼저, 현재 존재하는 모든 파이어볼을 이동시킨다.
1-1. 파이어볼이 이동한 NxN 격자의 좌표에 (질량, 속도, 방향) 정보를 저장
2. 이동이 끝나면, 격자를 순회하면서 파이어볼이 있는 좌표를 찾는다.
2-1. 해당하는 좌표에 있는 모든 파이어볼에 대해 Condition 2를 적용한다.
3. 모든 이동이 끝난 후, 남아있는 파이어볼의 질량을 합한다
"""

N, M, K = map(int, input().split())

# 파이어볼의 정보를 저장하기 위한 격자
board = [[[] for _ in range(N)] for _ in range(N)]

# [r, c, m, s, d]
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

dx8 = (-1, -1, 0, 1, 1, 1, 0, -1)
dy8 = (0, 1, 1, 1, 0, -1, -1, -1)


for _ in range(K):
    # 모든 파이어볼을 이동
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        # next location
        nr = (cr + dx8[cd]*cs) % N
        nc = (cc + dy8[cd]*cs) % N

        board[nr][nc].append([cm, cs, cd])

    # 격자를 순회한다.
    # NOTE: 파이어볼이 이동한 좌표만을 따로 탐색하는건 비효율적임 
    for r in range(N):
        for c in range(N):
            if len(board[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even = 0, 0, 0, 0
                fireball_count = len(board[r][c])
                while board[r][c]:
                    _m, _s, _d = board[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1

                if cnt_odd == fireball_count or cnt_even == fireball_count:  # 모두 홀수 또는 짝수
                    td = [0, 2, 4, 6]
                else:
                    td = [1, 3, 5, 7]

                if sum_m//5:
                    for d in td:
                        fireballs.append([r, c, sum_m//5, sum_s//fireball_count, d])

            if len(board[r][c]) == 1:
                fireballs.append([r, c] + board[r][c].pop())

print(sum(f[2] for f in fireballs))

