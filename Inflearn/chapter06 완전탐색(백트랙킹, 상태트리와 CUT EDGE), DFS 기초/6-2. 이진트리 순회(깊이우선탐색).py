# 6-2. 재귀함수를 이용한 이진수 출력
# 트리의 깊이우선탐색


def dfs(x):
    if x > 7:  # 처음에는 if, else 로 분기해서 문제 풀기
        return
    else:
        print(x, end=" ")  # 전위순회
        dfs(x * 2)
        # print(x, end=" ")  # 중위 순회
        dfs(x * 2 + 1)
        # print(x, end=" ")  # 후위 순회


if __name__ == "__main__":
    dfs(1)







