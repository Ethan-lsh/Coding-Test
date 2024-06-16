# Author: Sanghyeon Lee
# Date: June 16, 2024
# Description: Practice for Softeer D2

# 농사 지을 땅
board = [list(map(int, input().split())) for _ in range(3)]

# 1*3 크기의 땅의 높이가 모두 동일해야 한다.
# 특정 땅의 높이를 1의 비용으로 높이거나 낮추어 동일한 높이의 땅을 만들 수 있다.
# 이때, 농사를 지을 수 있는 최소 비용은 얼마인가?

ans = 1e3

# 횡 탐색
for row in board:
    for height in row:
        gap = sum([abs(height - h) for h in row])
        ans = min(ans, gap)

# 열 탐색
for column in list(zip(*board)):
    for height in column:
        gap = sum([abs(height - h) for h in column])
        ans = min(ans, gap)

print(ans)
