# Author: Sanghyeon Lee
# Date: March 8, 2024
# Description: 

from collections import deque

# 방향: 12, 1, 2, 3 시
# idx:  0, 1, 2, 3 ...7
gear = [deque(list(map(int, input()))) for _ in range(4)]

# turn times
K = int(input())


def left(num, way):
    if num < 0 or gear[num][2] == gear[num + 1][6]:
        return

    """
    선택된 기어와 오른쪽 기어가 서로 다른 극일 때,
    선택된 기어의 왼쪽에 있는 모든 기어는 선택된 기어와 '반대 방향'으로 회전해야 한다.
    """
    if gear[num][2] != gear[num + 1][6]:
        left(num - 1, -way)
        gear[num].rotate(way)

def right(num, way):
    if num > 3 or gear[num][6] == gear[num-1][2]:
        return

    if gear[num][6] != gear[num-1][2]:
        right(num+1, -way)
        gear[num].rotate(way)

for _ in range(K):
    x, y = map(int, input().split())
    x -= 1

    # 기준 톱니바퀴 번호에 왼쪽(-1)/오른쪽(+1) 의 회전 여부를 확인
    # 방향은 기준 톱니바퀴 회전 방향과 반대이기 때문에 음수를 취한다
    left(x-1, -y)
    right(x+1, -y)

    # 기준 톱니바퀴 회전
    gear[x].rotate(y)

result = 0
for i in range(4):
    result += (2**i) * gear[i][0]

print(result)
