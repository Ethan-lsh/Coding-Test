# Author: Sanghyeon Lee
# Date: May 3, 2024
# Description: Practice for SWEA D3

# 10개의 테스트 케이스
for test_case in range(1, 11):
    # 가로 길이 = 100; 1 <= 높이 <= 100
    dump = int(input())  # 덤프 횟수
    heights = list(map(int, input().split()))  # 각 상자의 높이

    for _ in range(dump):
        high = heights.index(max(heights))
        low = heights.index(min(heights))

        heights[high] -= 1
        heights[low] += 1

    print(f"#{test_case} {max(heights) - min(heights)}")