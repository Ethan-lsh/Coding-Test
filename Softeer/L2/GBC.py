# Author: Sanghyeon Lee
# Date: June 17, 2024
# Description: Practice for Softeer, L2

N, M = map(int, input().split())

info = [0] * 101  # N, M 의 범위는 1 <= ~ <= 100

## 구간별 정속 데이터를 배열에 저장
now = 1
for _ in range(N):
    section, speed = map(int, input().split())
    for i in range(now, now+section):
        info[i] = speed
    now += section


## 구간별 초과한 속도를 계산
ans = 0
now = 1
for _ in range(M):
    section, speed = map(int, input().split())
    for i in range(now, now+section):
        ans = max(ans, speed - info[i])
    now += section

print(ans)