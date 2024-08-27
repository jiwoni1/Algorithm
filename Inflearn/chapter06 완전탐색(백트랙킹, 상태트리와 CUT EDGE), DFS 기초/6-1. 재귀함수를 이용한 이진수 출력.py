# 7-1. 재귀함수를 이용한 이진수 출력

n = int(input())


def binary(x):
    if x == 1:   # 마지막
        print(1, end='')
        return
    binary(x//2)
    print(x % 2, end='')


binary(n)


# 강사님 코드
# def DFS(x):
#     if x == 0:
#         return
#     else:
#         DFS(x//2)
#         print(x % 2, end='')
#
#
# if __name__ == "__main__":
#     n = int(input())
#     DFS(n)





