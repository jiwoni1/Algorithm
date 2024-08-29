# 6-4. 합이 같은 부분집합 구하기(DFS)
import sys

# 1. ch리스트를 밖에 두고 partial 부분집합 리스트를 구하기
def dfs(x):
    if x > n - 1:
        # 나머지 부분집합
        # remains = [x for x in nums if x not in partial]
        # if sum(partial) == sum(remains):
        if sum(partial) * 2 == sum(nums):
            ch[0] = 1
            return
        else:
            return
    else:
        # nums[x] 원소를 부분집합에 포함하는 경우
        partial.append(nums[x])
        dfs(x+1)
        # nums[x] 원소를 부분집합에 포함하지 않는 경우
        partial.pop()
        dfs(x+1)


n = int(input())
nums = list(map(int, input().split()))
partial = []
ch = [0]

dfs(0)

if ch[0] == 1:
    print("YES")
else:
    print("NO")

# 2. sys.exit() 사용
def dfs(l, sum):
    if l == n:
        if sum * 2 == sum(nums):
            print("YES")
            sys.exit(0)  # 바로 프로그램을 끝내는 함수
    else:
        dfs(l+1, sum+nums[l])
        dfs(l+1, sum)


n = int(input())
nums = list(map(int, input().split()))
dfs(0, 0)
print("NO")


# 3. flag 사용
# return문 없어도 함수의 끝에 도달하면 자동으로 함수 종료 (None을 반환)
def dfs(l, sum):
    global flag  # 글로벌 변수 선언
    if flag: return
    if l == n:
        if sum * 2 == sum(nums):
            print("YES")
            flag = 1  # flag 변수 바꾸기
    else:
        dfs(l+1, sum+nums[l])
        dfs(l+1, sum)


flag = 0
n = int(input())
nums = list(map(int, input().split()))
dfs(0, 0)
if flag == 0: print("NO")