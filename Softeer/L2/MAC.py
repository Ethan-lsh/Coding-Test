# Author: Sanghyeon Lee
# Date: June 17, 2024
# Description: Practice for Softeer, L2

## Diamond square algorithm question
# 알고리즘을 알고 있다면 쉽게 풀 수 있는 문제
# 반복 레벨 N에 대해 'grid size = 2**n + 1' 의 조건을 만족한다
# 이때, 이를 구성하는 모든 점의 개수는 pow((2**n)+1, 2)와 같다

N = int(input())

print(pow((2**N)+1, 2))

