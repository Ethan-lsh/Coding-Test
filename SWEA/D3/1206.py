# Author: Sanghyeon Lee
# Date: April 29, 2024
# Description: Practice for SWEA D3

for test_case in range(1, 11):
    N = int(input())

    heights = list(map(int, input().split()))
    heights = heights

    ans = 0

    for i in range(2, N - 2):
        building_height = heights[i]

        # side building
        right_height = heights[i - 2:i]
        left_height = heights[i + 1:i + 3]

        side = right_height + left_height
        ans += building_height - max(side) if building_height > max(side) else 0

    print(f"#{test_case} {ans}")
