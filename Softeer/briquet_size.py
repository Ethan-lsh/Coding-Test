# Author: Sanghyeon Lee
# Date: June 10, 2024
# Description: Practice for Softeer, L2


n = int(input())

heater = list(map(int, input().split()))
heater.sort()  # 오름차순으로 정렬

cnt = 0
for i in range(2, 101):
    size_check = [x % i for x in heater]
    check = size_check.count(0)
    if check >= cnt:
        cnt = check

print(cnt)
