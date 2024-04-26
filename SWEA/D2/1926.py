# Author: Sanghyeon Lee
# Date: April 26, 2024
# Description: Practice for SWEA

N = int(input())

for num in range(1, N+1):
    str_num = list(str(num))

    # 문자열 리스트에 있는 3, 6, 9 숫자의 개수를 체크
    total = str_num.count('3') + str_num.count('6') + str_num.count('9')

    # 3, 6, 9 중 한 글자라도 있다면 - 를 출력
    if total > 0:
        print('-'*total, end=' ')
    else:
        print(num, end=' ')
