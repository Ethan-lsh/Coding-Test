# Author: Sanghyeon Lee
# Date: April 13, 2024
# Description: Table rotation technique

# [1] zip() 을 사용한 회전
# 정사각형, 직사각형 모두 적용 가능

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 시계 방향 90
arr_90 = list(map(list, zip(*arr[::-1])))
# print(arr_90)

# 시계 방향 180
arr_180 = [a[::-1] for a in arr[::-1]]
# print(arr_180)

# 시계 방향 270
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
# print(arr_270)


# [2] 인덱싱을 사용한 회전
# 회전한 후 행 번호 = 회전하기 전 열 번호
# 회전한 후 열 번호 = N - 1 - 회전하기 전 행 번호

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
new_90 = [[0] * n for _ in range(n)]

# 시계 방향 90
for i in range(n):
    for j in range(n):
        new_90[j][n - i - 1] = arr[i][j]
# print("new_90", new_90)

# 시계 방향 180
new_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n - 1 - i][n - 1 - j] = arr[i][j]
# print("new_180", new_180)

# 시계 방향 270
new_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_270[n - j - 1][i] = arr[i][j]
# print("new_270", new_270)

## 직사각형의 경우
# m = 4
nnew_90 = [[0] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        nnew_90[j][n - i - 1] = arr[i][j]

nnew_180 = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        nnew_180[n - i - 1][m - j - 1] = arr[i][j]

nnew_270 = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        nnew_270[m - j - 1][i] = a[i][j]


# [3] 부분 회전
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sy, sx = 2, 2
length = 3

# print(arr)
def rotate_90(sx, sy, length):
    global arr, new_arr
    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            oy, ox = x - sy, y - sy
            rx, ry = oy, length - ox - 1
            new_arr[sx + rx][sy + ry] = arr[x][y]

    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            arr[x][y] = new_arr[x][y]
    # print(arr)

# [4] 순열
arr = [1, 2, 3, 4]
visited = [0] * len(arr)

## backtracking 으로 직접 구현
def permutations(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0

# [5] 중복 순열
arr = [1, 2, 3, 4]
def product(n, new_arr):
    global arr
    if len(new_arr) == n:
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

# [6] 조합
arr = [1, 2, 3, 4]
def combinations(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


# [7] 중복 조합
arr = [1, 2, 3, 4]
def combinations_with_replacement(n, new_arr, c):
    if len(new_arr) == n:
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + arr[i], i)


# [8] 중력
arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
def gravity():
    n = len(arr)
    m = len(arr[0])
    for i in range(n-1):  # 마지막 행을 제외
        for j in range(m):
            p = i  # 현재 행 번호
            # 현재 행의 j가 값이 있고, 다음 행 p+1에 값이 없으면
            while 0 <= p and arr[p][j] == 1 and arr[p+1][j] == 0:
                arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
                p -= 1
    # print(arr)
gravity()

# [9] 달팽이 배열
def snake():
    # 최대 움직임 횟수, 현재 움직인 횟수, 방향 잔환 flag, 증가량, 방향
    global mx_cnt, cnt, flag, val, td

    # dx, dy 는 문제에서 주어진 이동방향
    # police는 달팽이 회전을 하는 주체
    cnt += 1
    pnx, pny = police[0] + dx[td], police[1] + dy[td]

    # 목적지에 도달하면 회전 방향과 진행방향을 바꾸는 경우
    if (pnx, pny) == GOAL:
        mx_cnt, cnt, flag, val = n, 1, 1, -1
        td = 2   # 방향을 아래 방향으로 변경

    # 최초 시작점에 도달하면 회전 방향과 진행방향을 바꾸는 경우
    elif (pnx, pny) == (CENTER_X, CENTER_Y):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0

    # 현재 움직인 횟수가 최대 움직임 횟수와 같으면
    # 현재 움직인 횟수를 초기화 하고, 방향을 전환한다.
    # 만약, flag가 0이면 1로 바꾸고, 1이면 0으로 바꿈과 동시에 최대 움직임 횟수를 1증가 시킨다.
    # 즉, 두 번의 방향 전환이 있으면 최대 움직임 횟수를 증가하는 문제에서 사용
    else:
        if cnt == mx_cnt:
            cnt = 0
            td = (td + val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    police[0], police[1] = pnx, pny

# [10] 이동 중 벽에 부딪혀서 방향이 전환되는 경우
# 물체가 x or y 축을 따라 이동하던 중, 벽을 만나 반대방향으로 튕기는 경우
# 예) 가로 길이가 1~5까지인 열이 있다면, 물체는 [1, 2, 3, 4, 5, 4, 3, 2] 를 한쪽 방향으로 진행하는 것과 같다.
# 이는, 1과 5는 튕길때 한번만 방문하고 나머지 2,3,4는 여러번 방문하게 되기 때문이다.
# 즉, 열의 길이를 C 라 가정했을 때, 2*C-2 만큼의 범위를 탐색하는 것과 동일하다.
def get_next_loc(i, j, speed, dir):

    if dir == UP or dir == DOWN:  # i
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, UP)
        return (speed, j, DOWN)

    else:  # j
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, LEFT)
        return (i, speed, RIGHT)
