# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA D2

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    print(f"#{test_case} ", 1 if string == string[::-1] else 0)

