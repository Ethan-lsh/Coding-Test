# Author: Sanghyeon Lee
# Date: March 9, 2024
# Description: Practice for simulation of SWEA

"""
Condition.
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
   => 비어있는 칸을 선택하고 (상,하,좌,우)를 탐색하여 좋아하는 학생 번호가 있는지 확인
2. 1을 만족하는 칸이 여러개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
   => (상,하,좌,우)를 탐색하여 비어있는지 확인
3. 2를 만족하는 칸도 여러 개인 경우, 행 > 열 순으로 우선순위를 정한다.

Key points: 선택한 학생에 대한 (좋아하는 친구 수, 빈칸 수)를 저장해야 함
"""

N = int(input())

table = [[0]*N for _ in range(N)]  # 자리에 학생이 있는지 체크

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


info = [0] * (N**2+1)
for _ in range(N**2):
    student_info = list(map(int, input().split()))
    # 현재 학생 번호, 좋아하는 학생 리스트
    n_student, l_student = student_info[0], student_info[1:]
    info[n_student] = l_student

    candidates = []  # 현재 학생이 앉을 수 있는 후보군
    for x in range(N):
        for y in range(N):
            if table[x][y] == 0:  # 현재 테이블이 빈칸인 경우에만
                empty = 0
                like = 0
                # 빈 칸 개수
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if table[nx][ny] == 0: # 빈칸 이라면
                            empty += 1
                        if table[nx][ny] in l_student: # 좋아하는 친구가 있다면
                            like += 1

                # 후보군에 저장; (좋아하는 학생 수, 빈 칸, 좌표)
                candidates.append((like, empty, x, y))

    # 후보군을 우선순위에 따라 정렬
    # 1.빈칸 2.좋아하는 학생 수 *내림차순*
    candidates.sort(key= lambda c: (-c[0], -c[1], c[2], c[3]))

    # 최적의 자리에 현재 학생 앉히기
    # candidates[0]는 정렬된 candidate의 가장 앞에 값.
    table[candidates[0][2]][candidates[0][3]] = n_student

sum = 0
for i in range(N):
    for j in range(N):

        times = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if table[nx][ny] in info[table[i][j]]:
                    times += 1

        if times != 0:
            sum += 10**(times-1)

print(sum)





