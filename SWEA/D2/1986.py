# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    even_sum = 0
    odd_sum = 0
    for n in range(1, N + 1):
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n

    print(f"#{test_case}", odd_sum - even_sum)