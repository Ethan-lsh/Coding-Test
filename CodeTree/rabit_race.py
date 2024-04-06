# Author: Sanghyeon Lee
# Date: April 6, 2024
# Description: Practice for simulation of SWEA

"""
Solution.
1. 토끼의 [점프 횟수, 행+열, 행, 열, id] 정보를 저장하는 Heapq 자료 구조를 선언
2. 토끼가 이동 중, 격자의 범위를 넘어서면 반대 방향으로 이동하는 함수를 구현 (def.is_inrange)
2-1. 이때, 토끼는 여러번 반대 방향으로 이동 할 수도 있음
3. 토끼를 우선 순위에 맞게 정렬해야 함 (sort를 활용)
4. 점수를 계산할 때, 주어진 조건과 반대로 수행
4-1. 움직인 토끼의 점수를 감점. 발생한 점수를 누적해서 저장 해둠
4-2. 400번 커맨드가 나오면, '현재 토끼들 중 가장 큰 값 + 누적한 값'을 계산하면 최종 결과
5. 프로그램을 종료
"""


from heapq import heappush, heappop

def is_inrange(x, y, dist):
    cand = []
    nx = x - dist
    if nx <= 0:
        a, b = divmod(abs(dist - x + 1), N - 1)
        if a % 2 == 0:
            if b == 0:
                nx = 1
            else:
                nx = b + 1
        else:
            if b == 0:
                nx = N
            else:
                nx = N - b
    cand.append([nx, y])

    # down
    nx = x + dist
    if nx > N:
        a, b = divmod(dist - (N - x), N - 1)
        if a % 2 == 0:
            if b == 0:
                nx = N
            else:
                nx = N - b
        else:
            if b == 0:
                nx = 1
            else:
                nx = b + 1
    cand.append([nx, y])

    # left
    ny = y - dist
    if ny <= 0:
        a, b = divmod(abs(dist - y + 1), M - 1)
        if a % 2 == 0:
            if b == 0:
                ny = 1
            else:
                ny = b + 1
        else:
            if b == 0:
                ny = M
            else:
                ny = M - b
    cand.append([x, ny])


    # right
    ny = y + dist
    if ny > M:
        a, b = divmod(dist - (M - y), M - 1)
        if a % 2 == 0:
            if b == 0:
                ny = M
            else:
                ny = M - b
        else:
            if b == 0:
                ny = 1
            else:
                ny = b + 1
    cand.append([x, ny])

    return cand


Q = int(input())

commands = [list(map(int, input().split())) for _ in range(Q)]

N, M = 0, 0
P = 0
rabbits = []
K = 0
cnt = 0

for cmd in commands:
    # 경주 시작 준비
    if cmd[0] == 100:
        N, M, P, pid = cmd[1], cmd[2], cmd[3], cmd[4:]

        rabbits = []  # [총 점프 횟수, 행 번호 + 열 번호, 행 번호, 열 번호, 고유 번호]
        rabbit_move = {}  # [토끼 번호: 거리]
        score = {}
        for i in range(0, P):
            rabbit_move[pid[2*i]] = pid[2*i+1]
            score[pid[2*i]] = 0
            heappush(rabbits, [0, 2, 1, 1, pid[2*i]])

    # 경주 진행
    elif cmd[0] == 200:
        K, S = cmd[1:]
        cand2 = []
        for k in range(K):
            jump, _, x, y, id = heappop(rabbits)

            dist = rabbit_move[id]  # 토끼가 가진 거리
            direction = is_inrange(x, y, dist)  # 토끼가 움직였을 때, 좌표 계산
            direction.sort(key= lambda x: (-(x[0]+x[1]), -x[0], -x[1]))

            ri, ci = direction[0]   # 움직인 좌표
            heappush(rabbits, [jump+1, ri+ci, ri, ci, id])
            cand2.append([ri, ci, id])

            # 점수 계산
            score[id] -= ri + ci
            cnt += ri + ci

        # K번 턴이 끝나고, 조건에 맞는 토끼에 점수를 더해준다.
        cand2.sort(key= lambda x: (x[0]+x[1], x[0], x[1], x[2]), reverse=True)
        id = cand2[0][-1]
        score[id] += S

    # 이동거리 변경
    if cmd[0] == 300:
        pid, L = cmd[1:]
        rabbit_move[pid] *= L

    # 최고의 토끼 선정
    if cmd[0] == 400:
        print(max(score.values()) + cnt)
