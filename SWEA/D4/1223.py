# Author: Sanghyeon Lee
# Date: June 3, 2024
# Description: Practice for SWEA

# import sys
# sys.stdin = open('./input.txt', 'r')

priorities = {'+': 1, '*': 2}


for test_case in range(1, 11):
    _size = int(input())
    expression = list(input())

    # 후위 표기법 생성
    # 1.다음 입력 연산자의 우선순위가 큰 경우, stack에 대입한다.
    # 2.다음 입력 연산자의 우선순위가 stack에 있는 연산자보다 작은 경우.
    #   1의 경우가 될 때까지 pop 한다.
    new_expression = []
    stack = []
    for exp in expression:
        if exp.isdigit():
            new_expression.append(exp)
            continue

        while stack:
            if priorities[stack[-1]] < priorities[exp]:
                stack.append(exp)
                break
            else:
                new_expression.append(stack.pop())

        if len(stack) == 0:
            stack.append(exp)
            continue

    # 후위 표기법 재구성 마무리
    new_expression.extend(x for x in stack[::-1])

    ## 후위 표기법 계산
    # 1.숫자는 무조건 stack에 저장
    # 2.연산자가 나오면 stack에서 2개의 피연산자를 추출한다.
    #   처음 뽑는 피연산자는 후순위, 두번째로 뽑는 피연산자는 전위 피연산자
    # 3. 위 과정을 반복
    new_stack = []
    while new_expression:
        new_exp = new_expression.pop(0)
        # 숫자이면 stack에 저장
        if new_exp.isdigit():
            new_stack.append(new_exp)
        else:
            op2 = int(new_stack.pop())
            op1 = int(new_stack.pop())
            result = op1 + op2 if new_exp == '+' else op1 * op2
            new_stack.append(result)

    print(f"#{test_case} {new_stack.pop()}")






