# 5-3. 후위표기식 만들기
import sys
# sys.stdin = open("input.txt", "r")

expression = list(input())
pri = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "(": -1,
    ")": -1,
}

stack1 = []  # 출력값(피연산자)
stack2 = []  # 연산자

for ex in expression:
    if ex not in pri:
        stack1.append(ex)
    else:  # 연산자라면
        # "("
        if ex == "(":
            stack2.append(ex)

        elif ex == ")":
            while stack2[-1] != "(":
                stack1.append(stack2.pop())
            stack2.pop()  # "(" 없애기

        # stack2에 있는 것보다 내가 우선순위가 클때 append
        else:  # 나보다 우선순위가 크면 pop 하고 stack1에 넣기
            while stack2 and pri[stack2[-1]] >= pri[ex]:
                stack1.append(stack2.pop())
            stack2.append(ex)

while stack2:
    stack1.append(stack2.pop())

print(''.join(stack1))


