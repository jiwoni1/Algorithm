# 5-7. 교육과정 설계
import sys
# sys.stdin = open("input.txt", "r")

es = list(input())
n = int(input())

# stack 에 반대로 넣으면 순서대로 제거되는것을 알 수 있음
for tc in range(1, n+1):
    es_stack = es[::-1]  # stack 초기화
    subs = list(input())
    for sub in subs:
        if not es_stack:
            break
        elif sub == es_stack[-1]:
            es_stack.pop()
        elif sub != es_stack[-1] and sub in es_stack:  # 순서가 아닌데 앞에 있는 경우
            break
    if es_stack:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')


    # 간결한 버전
    for tc in range(1, n + 1):
        es_stack = es[::-1]  # stack 초기화
        subs = list(input())
        for sub in subs:
            if sub in es_stack:  # 필수과목일때
                if sub != es_stack.pop():
                    print(f'{tc} NO')
                    break
        else:
            if es_stack:
                print(f'{tc} YES')
            else:
                print(f'{tc} NO')



