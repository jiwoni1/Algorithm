# 6-3. 부분집합 구하기(DFS)
# 상태트리
def dfs(v):
    if v > n:
        for i in range(n+1):
            if check[i] == 1:  # 포함된 것들 출력
                print(i, end=" ")
        print()
        return
    else:
        check[v] = 1   # v 포함
        dfs(v+1)
        check[v] = 0   # v 미포함
        dfs(v+1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n+1)
    dfs(1)


# 2번째 방법 (부분집합 원소를 list 에 넣기)
# 6-3. 부분집합 구하기(DFS)
# def dfs(v):
#     if v > n:
#         if len(check) == 0:
#             return
#         else:
#             print(*check, end=" ")
#             print()
#             return
#     else:
#         check.append(v)  # v 포함
#         dfs(v+1)
#         check.pop()  # v 미포함
#         dfs(v+1)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     check = []
#     dfs(1)