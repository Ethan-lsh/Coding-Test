# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA D3

from collections import deque

def check_price(cards):
    result = 0
    weight = len(cards) - 1
    for i in range(len(cards)):
        result += pow(10, weight) * cards[i]
    return result

T = int(input())
for test_case in range(1, T + 1):
    numbers, K = map(str, input().split())

    q = deque([int(x) for x in numbers])














