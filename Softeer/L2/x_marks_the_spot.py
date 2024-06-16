# Author: Sanghyeon Lee
# Date: June 10, 2024
# Description: Practice for Softeer L2


N = int(input())
paragraph = [list(input().split()) for _ in range(N)]

for si, ti in paragraph:
    index = si.find('x')
    if index == -1:
        index = si.find('X')
        print(ti[index].upper(), end='')
        continue
    print(ti[index].upper(), end='')
