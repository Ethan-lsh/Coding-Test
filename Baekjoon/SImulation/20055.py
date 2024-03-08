# Author: Sanghyeon Lee
# Date: March 4, 2024
# Description: Practice for simulation of SWEA
"""
Solution.
1. 회전을 한다 -> Deque 자료구조 사용
2. '로봇'과 '벨트'를 서로 분리하여 생각한다
3. 매 동작을 수행했을 때, 로봇을 내려주는 걸 고려한다
"""

from collections import deque

N, K = map(int, input().split())

A = deque(map(int, input().split()))
robot = deque([False]*N)

result = 0
while True:
    result += 1
    #1. 벨트를 회전
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    #2. 로봇을 이동시킴
    if sum(robot) > 0:
        for i in range(N-2, -1, -1):
            if robot[i] == True and robot[i+1] == False and A[i+1] > 0:
                robot[i+1] = True
                A[i+1] -=1
                robot[i] = False
        robot[-1] = 0

    #3. 올리는 위치 점검
    if robot[0] == False and A[0] > 0:
        robot[0] = True
        A[0] -= 1

    if A.count(0) >= K:
        break

print(result)