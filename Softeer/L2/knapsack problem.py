# Author: Sanghyeon Lee
# Date: June 16, 2024
# Description: Practice for Softeer, D2
# Fractional Knapsack algorithm problem

W, N = map(int, input().split())

weight_and_profit = [list(map(int, input().split())) for _ in range(N)]

# (무게, 값어치)를 '무게/값어치' 비율에 맞춰 내림차순으로 정렬 
weight_and_profit.sort(key=lambda x: x[1], reverse=True)

ans = 0

for weight, profit in weight_and_profit:
    # 현재 배낭 무게보다 작다면, 배낭에 추가 => 이득
    if weight <= W:
        W -= weight
        ans += profit * weight
    # 현재 배낭의 무게보다 크다면, 남은 무게 만큼의 값어치를 추가
    else:
        ans += W * profit
        break

print(ans)

