# Author: Sanghyeon Lee
# Date: April 21, 2024
# Description: Pracice for SWEA

def check_price(base_price):
    global ans
    cost = [base_price - sel for sel in selected]
    ans += sum(cost)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 뒤에서 부터 탐색
    ans = 0
    base_price = prices.pop()
    selected = []
    while prices:
        price = prices.pop()
        # 만약, 전날의 금액이 선택된 날 보다 낮다면 구매
        if price < base_price:
            selected.append(price)
        # 만약, 전날의 금액이 선택한 날 보다 높다면 지금까지 구매한 모든 걸 판매
        elif price >= base_price:
            check_price(base_price)
            base_price = price
            selected = []

    # 모든 날을 순회했다면, 구매한 모든 걸 판매
    check_price(base_price)
    print(f"#{test_case} {ans}")