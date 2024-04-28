# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA D2

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))

    numbers.remove(max(numbers))
    numbers.remove(min(numbers))

    print(f"#{test_case}", round(sum(numbers)/len(numbers)))
