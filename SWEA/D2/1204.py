# Author: Sanghyeon Lee
# Date: April 24, 2024
# Description: Practice for SWEA

import sys
sys.stdin = open("../input.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    test_case = int(input())
    scores: list = list(map(int, input().split()))

    # 점수를 구성하는 숫자의 종류를 획득
    # 리스트를 Set 자료형으로 변형하면 중복값이 사라진다.
    numbers = set(scores)

    # 가장 여러번 나타난 숫자를 구함
    cnt = 0  # 숫자의 개수
    ans = 0
    for num in numbers:
        # 현재 숫자 개수보다 크면, 값을 교체
        if cnt < scores.count(num):
           cnt = scores.count(num)
           ans = num

    print(f"#{test_case} {ans}")

