# Author: Sanghyeon Lee
# Date: June 16, 2024
# Description: Practice for Softeer, L2

# 바이러스가 숙주의 몸속에서 1초당 P배씩 증가한다.
# 바이러스가 K마리 있었다면 N초 후에 늘어난 바이러스를 1000000007로 나눈다면?

K, P, N = map(int, input().split())

mod_num = 1000000007

# NOTE: 단순하게 '제곱연산' 또는 그냥 곱셈을 해서는 안된다.
# Python의 곱셈 연산은 연산자의 크기가 매우 커지게 되면 O(1)을 보장하지 않기 떄문에
# 시간이 더 오래 걸릴 수 있다.
for _ in range(N):
    K = (K * P) % mod_num

print(K)