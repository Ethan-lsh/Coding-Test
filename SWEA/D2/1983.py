# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA
import sys
sys.stdin = open("../input.txt", "r")

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    sarr = []

    for i in range(n):
        m_score, h_score, task = map(int, input().split())
        score = m_score * 0.35 + h_score * 0.45 + task * 0.2
        sarr.append(score)

    answer = sarr[k - 1]
    sarr.sort(reverse=True)
    rate = n // 10
    result = sarr.index(answer) // rate

    print(f'#{t} {grades[result]}')